#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: get_toll_to_ljt_0828
# Author  : yuanzhou
# Date    : 2018/8/28
# Description:


import requests
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import time
import functools
import os
from lonlat2adinfo_new2 import main_func_lonlat2ad, main_func_batch_True, get_boundary_data_by_file
from provs_toll_rules import provs_toll_rules
plt.rcParams['font.family'] = ['FangSong_GB2312']


def truck_type(truck_weight):
    if truck_weight < 2:
        return 1
    elif 2 <= truck_weight < 5:
        return 2
    elif 5 <= truck_weight < 10:
        return 3
    elif 10 <= truck_weight < 15:
        return 4
    else:
        return 5


def oil_expend(truck_weight, prov, road_level):
    if truck_weight < 15:
        result = 25
    elif truck_weight >= 15 and truck_weight <= 49:
        result = (truck_weight - 15) * 0.5 + 25
    else:
        result = 42

    if prov in ['贵州省', '云南省']:
        result *= 1.1

    if road_level == 0:
        result *= 1.15
    return result



def get_oil_price():
    oil_price = pd.read_excel('在线油站&价格（第二版）.xlsx')
    oil_city_price = pd.DataFrame(oil_price.groupby(['市'])['企业采购价']
                                  .apply(lambda x: np.nanmean(x))).reset_index()
    oil_prov_price = pd.DataFrame(oil_price.groupby(['省'])['企业采购价']
                                  .apply(lambda x: np.nanmean(x))).reset_index()
    return oil_city_price, oil_prov_price


def ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=None, wheels=None, front_length=None):
    """

    Using the ETC price of car to calculate the ETC price of truck
    :param start_GPS: tuple (start_x, start_y)
    :param end_GPS: tuple (end_x, end_y)
    :param truck_weight: float
    :return: dict {0:(price, time), ...}
    """
    # start_x, start_y = 106.550464, 29.563761
    # end_x, end_y = 111.286451, 30.69187
    # truck_weight = 40.1
    truck_weight = int(truck_weight)
    type_ = truck_type(truck_weight)

    start_x, start_y = start_GPS
    end_x, end_y = end_GPS
    key = 'a0402bea88287c7ee36020fabd995539'
    url = 'https://restapi.amap.com/v3/direction/driving?' \
          'key=%s&' \
          'origin=%s,%s&' \
          'destination=%s,%s&' \
          'originid=&' \
          'destinationid=&' \
          'extensions=base&' \
          'strategy=10&' \
          'waypoints=&' \
          'avoidpolygons=&' \
          'avoidroad=' % (key, start_x, start_y, end_x, end_y)

    html = requests.get(url)
    data = str(html.content, 'utf-8')
    data = eval(data)
    if data['status'] == '0':
        print('Oops! Maybe the key is wrong')
    else:
        n_lines = len(data['route']['paths'])
        result = {}
        batch_size = 20
        # 油价数据
        oil_city_price, oil_prov_price = get_oil_price()
        # 推荐线路计算
        for l in range(n_lines):
            temp = data['route']['paths'][l]['steps']
            df = pd.DataFrame(data=temp)
            df['last_point'] = df.polyline.apply(lambda x: x.split(';')[-1])
            df['last_point_tuple'] = df.last_point.apply(lambda x: tuple([float(i) for i in x.split(',')]))

            point_in = df['last_point_tuple'].tolist()
            temp_result = main_func_lonlat2ad(point_in, level_mode='city', batch=True)
            # temp1 = df['last_point_tuple'].apply(lambda x: main_func(x, level_mode='city'))
            df['curr_prov'] = [i[-2] for i in temp_result]
            df['curr_city'] = [i[-1] for i in temp_result]

            price_times = df.apply(lambda x: provs_toll_rules(x.curr_prov, truck_weight, road_name=x.road, axle=axle,
                                                              wheels=wheels, front_length=front_length)[0], axis=1)
            temp = df.copy()
            temp['price_times'] = price_times

            temp['tolls'] = temp['tolls'].astype(float)
            price_temp = int(np.sum(temp['tolls'] * temp['price_times']))
            temp.distance = temp.distance.astype(int)
            time_temp = np.sum(temp.distance[temp.tolls > 0]) / 1000 / 70 + \
                np.sum(temp.distance[temp.tolls == 0]) / 1000 / 35
            length_temp = np.round(np.sum(temp.distance) / 1000, decimals=2)

            # 百公里油耗
            temp['oil_standard'] = temp.apply(lambda x: oil_expend(truck_weight, x.curr_prov, x.tolls), axis=1)

            # 各路段油耗
            temp['oil_spend'] = temp['distance'] / (1000 * 100) * temp['oil_standard']
            oil_spend_temp = np.round(np.sum(temp['oil_spend']), decimals=2)

            # 油价
            price_dict = {}
            temp['curr_city'] = temp['curr_city'].astype(str)
            temp['curr_prov'] = temp['curr_prov'].astype(str)
            cities_temp = list(temp['curr_city'][temp['curr_city'] != '[]'].unique())
            for j in cities_temp:
                index_city = oil_city_price.apply(lambda x: True if j[:2] in x.市 else False, axis=1)
                if np.sum(index_city) == 0:
                    continue
                else:
                    p = oil_city_price.loc[index_city, '企业采购价'].values[0]
                    price_dict[j] = np.round(p, decimals=2)

            provs_temp = list(temp['curr_prov'][temp['curr_prov'].apply(lambda x: len(x)) != 0].unique())
            for j in provs_temp:
                index_city = oil_prov_price.apply(lambda x: True if j[:2] in x.省 else False, axis=1)
                if np.sum(index_city) == 0:
                    continue
                else:
                    p = oil_prov_price.loc[index_city, '企业采购价'].values[0]
                    price_dict[j] = np.round(p, decimals=2)

            temp['oil_city'] = temp['curr_city'].map(price_dict)
            temp['oil_prov'] = temp['curr_prov'].map(price_dict)
            temp['oil_final'] = temp.apply(lambda x: x.oil_prov if np.isnan(x.oil_city) else x.oil_city, axis=1)

            oil_spend_price_temp = np.round(np.sum(temp['oil_final'] * temp['oil_spend']))
            result[l] = {'length': length_temp, 'time': time_temp, 'ETC': price_temp, 'diesel_spend': oil_spend_temp,
                         'diesel_price': oil_spend_price_temp}
        # print(result)
        return result


if __name__ == '__main__':
    truck_weight = 49
    axle = 3
    wheels = 12
    front_length = 2.6
    # 东莞-娄底
    start_GPS = (113.746262, 23.046237)
    end_GPS = (112.008497, 27.728136)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('东莞-娄底: ', result)

    # 东莞-昆明
    start_GPS = (113.746262, 23.046237)
    end_GPS = (102.833722, 24.881539)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('东莞-昆明: ', result)

    # 南宁-东莞
    start_GPS = (108.36637, 22.817746)
    end_GPS = (113.746262, 23.046237)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('南宁-东莞: ', result)

    # 南宁-成都
    start_GPS = (108.36637, 22.817746)
    end_GPS = (104.066143, 30.573095)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('南宁-成都: ', result)

    # 南宁-贵阳
    start_GPS = (108.36637, 22.817746)
    end_GPS = (106.630153, 26.647661)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('南宁-贵阳: ', result)

    # 襄阳-南宁
    start_GPS = (112.144146, 32.042426)
    end_GPS = (108.36637, 22.817746)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('襄阳-南宁: ', result)

    # 襄阳-宜昌
    start_GPS = (112.144146, 32.042426)
    end_GPS = (111.286451, 30.69187)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('襄阳-宜昌: ', result)

    # 长沙-宜昌
    start_GPS = (112.938888, 28.228272)
    end_GPS = (111.286451, 30.69187)
    result = ETC_for_truck(start_GPS, end_GPS, truck_weight, axle=axle, wheels=wheels, front_length=front_length)
    print('长沙-宜昌: ', result)
