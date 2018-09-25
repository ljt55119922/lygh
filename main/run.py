# -*- coding: utf-8 -*-
# @Time    : 2018/8/14
# @Author  : ljt
# @Site    : 
# @File    : main_.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from main import oil_station_pruducer
import requests
import math, copy
import operator
import hashlib
from main.lonlat2adinfo_new2 import main_func_lonlat2ad, main_func_batch_True, get_boundary_data_by_file
from main.provs_toll_rules import provs_toll_rules
from main.etc_cards_info import etc_cards


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


def md5(text):
    hl = hashlib.md5()
    hl.update(text.encode(encoding='utf-8'))
    str_md5 = hl.hexdigest()
    return str_md5


def bd09togcj02(bd_lon, bd_lat):
    """
    百度——>高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x_pi = 3.14159265358979324 * 3000.0 / 180.0
    pi = 3.1415926535897932384626  # π
    a = 6378245.0  # 长半轴
    ee = 0.00669342162296594323  # 扁率

    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def oil_expend(truck_weight, prov, road_level):
    if truck_weight < 15:
        result = 25
    elif 15 <= truck_weight <= 49:
        result = (truck_weight - 15) * 0.5 + 25
    else:
        result = 42

    if prov in ['贵州省', '云南省']:
        result *= 1.1

    if road_level == 0:
        result *= 1.15
    return result


def cost_by_api(start, end, fuel_mileage, oil_price, truck_weight, axle, wheels, front_length, boundary_data_111):
    truck_weight = int(truck_weight)
    start_x, start_y = start
    end_x, end_y = end
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
        return print('Oops! Maybe the key is wrong')
    else:
        lines_list = data['route']['paths']
        cost_list = []
        for line_index in range(len(lines_list)):
            line = lines_list[line_index]
            distance = line['distance']
            duration = line['duration']
            strategy = line['strategy']
            toll_distance = line['toll_distance']
            steps = line['steps']

            polyline_list = []
            for step in steps:
                polyline = step['polyline']  # "113.746101,23.046467;113.746346,23.046621"
                polyline_list.extend(str(polyline).strip().split(';'))

            if oil_price != '':
                oil_cost = float(oil_price) * float(fuel_mileage) * 0.01 * float(distance) * 0.001
            else:
                oil_cost = 'null'

            temp = data['route']['paths'][line_index]['steps']
            df = pd.DataFrame(data=temp)
            df['last_point'] = df.polyline.apply(lambda x: x.split(';')[-1])
            df['last_point_tuple'] = df.last_point.apply(lambda x: tuple([float(i) for i in x.split(',')]))
            point_in = df['last_point_tuple'].tolist()
            # temp_result = main_func_lonlat2ad(point_in, level_mode='city', batch=True)
            temp_result = main_func_batch_True(point_in, boundary_data_111)
            df['curr_prov'] = [i[-2] for i in temp_result]
            df['curr_city'] = [i[-1] for i in temp_result]
            price_times = df.apply(lambda x: provs_toll_rules(x.curr_prov, truck_weight, road_name=x.road, axle=axle,
                                                              wheels=wheels, front_length=front_length)[0], axis=1)
            temp = df.copy()
            temp['price_times'] = price_times
            temp['tolls'] = temp['tolls'].astype(float)
            etc_cost = int(np.sum(temp['tolls'] * temp['price_times']))
            # ---------------------------------------------------------------

            temp['e_cost'] = temp['tolls'] * temp['price_times']
            temp_df = temp.loc[temp.tolls != 0]
            if temp_df.empty:
                single_card_top3 = "None"
                group_cards = 'None'
            else:
                value = temp_df.groupby(['curr_prov'])[['e_cost']].sum()
                value = value.reset_index()
                toll_dict = value.set_index('curr_prov').T.to_dict()
                toll_dict_old = copy.deepcopy(toll_dict)
                key_list_ = [key for key in toll_dict_old.keys()]
                key_list = copy.deepcopy(key_list_)
                temp_dis = []
                for dis_info in etc_cards:
                    for pro in toll_dict.keys():
                        e_cost = toll_dict[pro]['e_cost']
                        if pro == dis_info[1]:
                            dis_info_ = copy.deepcopy(dis_info)
                            dis_cost = float(e_cost)*(1-float(dis_info_[2]))
                            dis_info_.append(round(dis_cost, 2))
                            temp_dis.append(dis_info_)
                temp_dis.sort(key=operator.itemgetter(3), reverse=True)
                temp_dis_new=copy.deepcopy(temp_dis)

                df_temp_cards = pd.DataFrame(temp_dis_new, columns=["cards", "province", "dis_p", "dis_cost"])
                df_temp_cards = df_temp_cards.groupby(['cards'])[['dis_cost']].sum()
                df_temp_cards = df_temp_cards.reset_index()
                df_temp_cards = df_temp_cards.sort_values(by='dis_cost', ascending=False)
                single_card_top3 = df_temp_cards.to_dict('records')

                dis_result = []
                for pro in key_list:
                    dis_data = {"province": pro}
                    dis_flag = 0
                    for info in temp_dis_new:
                        if pro == info[1]:
                            dis_data["dis_cost"] = info[3]
                            dis_data["etc_cards"] = info[0]
                            dis_flag = 1
                            break
                    if dis_flag == 0:
                        dis_data["dis_cost"] = "None"
                        dis_data["etc_cards"] = "None"

                    dis_result.append(dis_data)

                df_temp = pd.DataFrame(dis_result)
                df_temp_dis = df_temp.groupby(['etc_cards', 'province'])[['dis_cost']].sum()
                df_temp_dis = df_temp_dis.reset_index()
                df_temp_dis = df_temp_dis.sort_values(by='dis_cost', ascending=False)
                group_cards = df_temp_dis.to_dict('records')

            if oil_cost != 'null':
                oc = oil_cost
            else:
                oc = 0

            cost_list.append({"distance": distance,
                              "strategy": strategy,
                              "total_cost": oc + etc_cost,
                              "toll_distance": toll_distance,
                              "drive_time": duration,
                              "oil_cost": oc,
                              "etc_cost": etc_cost,
                              "single_card_top3":single_card_top3,
                              "group_cards": group_cards,
                              "road_path": polyline_list})
        return cost_list


def main_fuc(start, end, fuel_mileage, truck_weight, station_type, axle=None, wheels=None, front_length=None):  # fuel_mileage, oil_price, truck_weight
    print('边界数据加载..')
    boundary_data_111 = get_boundary_data_by_file()
    print('油站数据加载..')
    oil_station_info_ = oil_station_pruducer.get_oil_station(start, end, station_type)
    n = len(oil_station_info_)
    text = str(start[0]) + ',' + str(start[1]) + ';' + str(end[0]) + ',' + str(end[1])
    print("The total number of waiting stations is %s..." % n)
    data_list = []
    for info in oil_station_info_:
        oil_price = info[15]
        coordinates = bd09togcj02(float(info[6]), float(info[7]))
        coordinates = (coordinates[0], coordinates[1])
        zb_path = [start, coordinates, end, start]
        zb_path_list = []
        for i in range(len(zb_path)):
            if i <= len(zb_path) - 2:
                zb_path_list.append(([zb_path[i], zb_path[i + 1]]))
        time_min_cost_list = []

        zb_path_list = zb_path_list[:-1]
        for item in zb_path_list:
            start_ = item[0]
            end_ = item[1]
            cost_list = cost_by_api(start_, end_, fuel_mileage, oil_price, truck_weight, axle, wheels, front_length, boundary_data_111)
            # l_cost_.sort(key=operator.itemgetter(0))   # 按总成本排序
            cost_list.sort(key=operator.itemgetter('drive_time'))  # 按驾驶时间排序
            # print(l_cost_)
            min_cost_ = cost_list[0]
            del min_cost_['road_path']
            # print(min_cost_)
            time_min_cost_list.append(min_cost_)
        single_card_data = []
        group_card_data = []
        for part in time_min_cost_list:
            if part['single_card_top3'] != "None":
                single_card_data.append(part['single_card_top3'])
            if part['group_cards'] != "None":
                group_card_data.append(part['group_cards'])
        single_card_data_ = []
        for x_ in single_card_data:
            single_card_data_.extend(x_)
        group_card_data_ = []
        for y_ in group_card_data:
            group_card_data_.extend(y_)

        single_card_data_ = [[x['cards'], x['dis_cost']] for x in single_card_data_]
        single_card_data_df = pd.DataFrame(single_card_data_, columns=['cards', 'dis_cost'])
        single_card_data_df = single_card_data_df.groupby(['cards'])[['dis_cost']].sum()
        single_card_data_df = single_card_data_df.reset_index()
        single_card_data_df = single_card_data_df.sort_values(by='dis_cost', ascending=False)
        single_card_top3 = single_card_data_df[:3].to_dict('records')

        # 最优卡组
        # group_card_data_ = [[x['etc_cards'], x['province'], x['dis_cost']] for x in group_card_data_]
        # group_card_data_df = pd.DataFrame(group_card_data_, columns=['etc_cards', 'province', 'dis_cost'])
        # group_card_data_df = group_card_data_df.groupby(['etc_cards', 'province'])[['dis_cost']].sum()
        # group_card_data_df = group_card_data_df.reset_index().to_dict('records')
        # print(group_card_data_df)

        data = {'Line_ID': md5(text),
                'start': start,
                'end': end,
                'station_id': info[0],
                'station_name': info[1],
                'address': info[5],
                'is_online': info[8],
                'is_qy': info[9],
                'coor': coordinates,
                'oil_price': oil_price,
                'total_cost': sum([float(x['total_cost']) for x in time_min_cost_list]),
                'etc_cost': sum([float(x['etc_cost']) for x in time_min_cost_list]),
                'oil_cost': sum([float(x['oil_cost']) for x in time_min_cost_list]),
                'mile': sum([int(x['distance']) for x in time_min_cost_list]) / 1000,
                'drivetime': sum([int(x['drive_time']) for x in time_min_cost_list]) / (60 * 60),
                'single_card_top3': single_card_top3,
                # 'group_cards': group_card_data_df,
                'away_from_start': int(time_min_cost_list[0]["distance"]),
                'away_from_end': int(time_min_cost_list[1]["distance"])}
                # 'polyline_list': polyline_list}
        data_list.append(data)
        # insert_data('db_algorithms', '', data_list)
        print(data)
    data_list.sort(key=operator.itemgetter('total_cost'))
    cost_sort = data_list[:5]
    data_list.sort(key=operator.itemgetter('drivetime'))
    time_sort = data_list[:5]
    data_list.sort(key=operator.itemgetter('away_from_start'))
    d_start_sort = data_list[:5]
    data_list.sort(key=operator.itemgetter('away_from_end'))
    d_end_sort = data_list[:5]
    print(cost_sort)
    print(time_sort)
    print(d_start_sort)
    print(d_end_sort)

    result = {"cost_sort": cost_sort,
              "time_sort": time_sort,
              "d_start_sort": d_start_sort,
              "d_end_sort": d_end_sort}
    return result


if __name__ == '__main__':

    """ test demo """
    # 东莞-娄底
    truck_weight = 49   # 载重
    axle = 3            # 轴数
    wheels = 12         # 轮数
    front_length = 2.6  # 车长
    fuel_mileage = 30   # 油耗

    start_GPS = (113.746262, 23.046237)
    end_GPS = (112.008497, 27.728136)
    station_type = 0  # 1为全量， 0为上线的企业油
    main_fuc(start_GPS, end_GPS, fuel_mileage, truck_weight, station_type, axle=axle, wheels=wheels, front_length=front_length)
    pass
