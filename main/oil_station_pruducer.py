# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 15:02
# @Author  : ljt
# @Site    : 
# @File    : city_code_pruducer.py
# @Software: PyCharm

import re
import requests
from main import config
import time
import string
from main import SqlHelper,lonlat2adinfo_new2



def getHtml_with_proxy(ip, url, cookie):
    proxy = {
        'http': 'http://' + ip,
        'https': 'https://' + ip
    }
    count = 1
    while count > 0:
        _header = {
            'Host': "www.amap.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/67.0.3396.62 Safari/537.36",
            'Cookie': cookie
        }

        try:
            html = requests.get(url, headers=_header, timeout=10, proxies=proxy)
            if html:
                data = str(html.content, 'utf-8')
                data = data.replace("/**/ typeof jsonp_476699_ === 'function' && jsonp_476699_(", '')[:-2]
                data = data.replace("/**/ typeof jsonp_490825_ === 'function' && jsonp_490825_(", '')
                data = re.sub(r"/\*\*/ typeof jsonp_\d{0,6}_ === 'function' && jsonp_\d{0,6}_\(", "", data)
                data = eval(data)
                if data['data'] == "too fast":
                    return None  # ip被封
                else:
                    data = data['data']
                    if data['message'] == 'Successful.':
                        return data
            else:
                if html.status_code == 403:
                    continue
                count -= 1
                continue
        except Exception as e:
            # print(e)
            return None
    return None


def get_citycode_by_db(start, end):
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]

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
    # print(url)
    html = requests.get(url)
    data = str(html.content, 'utf-8')
    data = eval(data)
    if data['status'] == '0':
        return print('Oops! Maybe the key is wrong')
    else:
        lines_list = data['route']['paths']
        all_point = []
        for line_index in range(len(lines_list)):
            line = lines_list[line_index]
            steps = line['steps']
            l_point_list = []
            for step in steps:
                # print(step)
                polyline = step['polyline']  # "113.746101,23.046467;113.746346,23.046621"
                point_ = polyline.split(';')[-1]
                l_point_list.append(point_)
            point_list = [x.split(',') for x in l_point_list]
            point_data = []                 # 这里可以根据两点距离缩小计算点数量
            for point in point_list:
                p = tuple(map(eval, point))
                if p not in all_point:
                    all_point.append(p)
                # point_data.append()
        city_info = lonlat2adinfo_new2.main_func_lonlat2ad(all_point, level_mode='city', batch=True)
        result = []
        for info in city_info:
            d = {'name': info[5], 'citycode': info[1]}
            if d not in result:
                result.append(d)
        return result

def City_OilStation(CityCodeList, station_type=0):
    """
    各city下的所有油站信息
    :param CityCodeList:
    :return:
    """
    if len(CityCodeList) > 0:
        code_list = []
        for _CityCode in CityCodeList:
            _CityCode = _CityCode['citycode']
            code_list.append(_CityCode)

        oil_station_list = []
        if station_type == 1:
            sql = """SELECT * FROM oil_station_info"""
        else:
            sql = """SELECT * FROM oil_station_info where qy_station_mark = 1 and online_mark = 1 and purchase_price_qy != ''"""
        rows = SqlHelper.read_table_by_sql(sql)
        for row in rows:
            _city = row[4]
            _province = row[3]
            with open('./BaseData/province&city.txt', 'r', encoding='utf-8') as fp:
                for line in fp.readlines():
                    line = line.strip()
                    if len(line) > 0:
                        qh = line.split('	')[2]
                        city = line.split('	')[1]
                        province = line.split('	')[0]
                        if qh[0] == '0':
                            pass
                        else:
                            if qh[-1] not in [word for word in string.ascii_letters.upper()]:
                                qh = '0' + qh
                            else:
                                qh = '0' + qh[:-1]
                        if _province in province:
                            if _city in city:
                                if qh in code_list:
                                    # print(row)
                                    oil_station_list.append(row)
        return oil_station_list
    else:
        print('none CityCodeList')
        return None


def get_oil_station(start, end, station_type):
    print("start up process of getting oil station information ...")
    city_list = get_citycode_by_db(start, end)
    oil_station_list = City_OilStation(city_list, station_type)
    print("get oil station information success ...")
    return oil_station_list
