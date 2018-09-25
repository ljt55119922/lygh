# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 11:41
# @Author  : ljt
# @Site    : 
# @File    : test.py
# @Software: PyCharm

"""
基于边界数据的地理围栏算法，用于坐标位置所属确认
"""
import requests
from main.SqlHelper import insert_data, read_table_by_sql, execute_sql
from math import radians, cos, sin, asin, sqrt
import operator
import time
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import copy
import json


def get_all_county_info():
    keywords = '中国'
    url = "http://restapi.amap.com/v3/config/district?" \
          "keywords=%s&key=a0402bea88287c7ee36020fabd995539&subdistrict=3&extensions=all" % keywords

    temp = str(requests.get(url).content, 'utf-8')
    temp = eval(temp)

    province_list = temp["districts"][0]["districts"]
    p_list = []
    for province in province_list:
        p_adcode = province["adcode"]
        p_center = province["center"]
        p_citycode = str(province["citycode"])
        p_level = province["level"]
        p_name = province["name"]
        p_data = {"adcode": p_adcode, "center": p_center, "citycode": p_citycode, "level": p_level, "name": p_name}
        p_list.append(p_data)
        city_list = province["districts"]
        c_list = []
        for city in city_list:
            c_adcode = city["adcode"]
            c_center = city["center"]
            c_citycode = str(city["citycode"])
            c_level = city["level"]
            c_name = city["name"]
            c_data = {"adcode": c_adcode, "center": c_center, "citycode": c_citycode, "level": c_level, "name": c_name}
            c_list.append(c_data)
            district_list = city["districts"]
            d_list = []
            print(c_name)
            for district in district_list:
                d_adcode = district["adcode"]
                d_center = district["center"]
                d_citycode = str(district["citycode"])
                d_level = district["level"]
                d_name = district["name"]
                d_data = {"adcode": d_adcode, "center": d_center, "citycode": d_citycode, "level": d_level,
                          "name": d_name,"city":c_name,"province":p_name}
                print(d_data)
                # d_list.append(d_data)
            #     sql = """UPDATE boundary_data  SET city='%s',province='%s' WHERE adcode = '%s'""" % (str(c_name), str(p_name), str(d_adcode))
            #     execute_sql(sql)
            # sql = """UPDATE boundary_data  SET city='%s',province='%s' WHERE adcode = '%s'""" % (str(c_name), str(p_name), str(c_adcode))
            # execute_sql(sql)
    #         insert_data('db_algorithms', 'boundary_data', d_list)
    #     insert_data('db_algorithms', 'boundary_data', c_list)
    # insert_data('db_algorithms', 'boundary_data', p_list)


def get_poly_line():
    sql = """SELECT * FROM boundary_data"""
    sql = """select adcode from boundary_data WHERE LENGTH(polyline)>=65000;"""
    rows = read_table_by_sql(sql)
    for row in rows:
        keywords = row[0]
        # print(row[3])
        url = "http://restapi.amap.com/v3/config/district?" \
              "keywords=%s&key=a0402bea88287c7ee36020fabd995539&subdistrict=0&extensions=all" % keywords
        temp = str(requests.get(url).content, 'utf-8')
        temp = eval(temp)
        if len(temp["districts"]) == 1:
            polyline = temp["districts"][0]["polyline"]
            # print(polyline)
            print(temp["districts"][0]["name"])
            sql = """UPDATE boundary_data  SET polyline='%s' WHERE adcode = '%s'""" % (str(polyline), str(row[0]))
            execute_sql(sql)
        else:
            print("error")


def IsPtInPoly(aLon, aLat, pointList):
    """
    :param aLon: double 经度
    :param aLat: double 纬度
    :param pointList: list [(lon, lat)...]
    """

    iSum = 0
    iCount = len(pointList)

    if iCount < 3:
        return False
    for i in range(iCount):
        pLon1 = pointList[i][0]
        pLat1 = pointList[i][1]
        if i == iCount - 1:
            pLon2 = pointList[0][0]
            pLat2 = pointList[0][1]
        else:
            pLon2 = pointList[i + 1][0]
            pLat2 = pointList[i + 1][1]

        if ((aLat >= pLat1) and (aLat < pLat2)) or ((aLat >= pLat2) and (aLat < pLat1)):
            if abs(pLat1 - pLat2) > 0:
                pLon = pLon1 - ((pLon1 - pLon2) * (pLat1 - aLat)) / (pLat1 - pLat2);
                if pLon < aLon:
                    iSum += 1
    if iSum % 2 != 0:
        return True
    else:
        return False


def haversine(point1, point2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    (lon1, lat1) = point1
    (lon2, lat2) = point2
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def center_distance(point,level_mode='city'):
    if level_mode=='city':
        sql = """select adcode,citycode,center,`level` from boundary_data WHERE `level`='city';"""
    elif level_mode=='district':
        sql = """select adcode,citycode,center,`level` from boundary_data WHERE `level`='district' UNION ALL
                 select adcode,citycode,center,`level` from boundary_data GROUP BY city HAVING COUNT(city)=1 AND `level`= 'city';"""
    else:
        raise ValueError
    time_1 = time.time()
    rows = read_table_by_sql(sql)
    time_2 = time.time()
    # print('sql', time_2 - time_1)
    L = []
    for row in rows:
        if len(row[2]) >= 5:
            point1 = (float(str(row[2]).split(',')[0]), float(str(row[2]).split(',')[1]))
            d = haversine(point, point1)
            row = row.values()
            row.append(d)
            L.append(row)
    L.sort(key=operator.itemgetter(4))
    l = []
    for v in L[:10]:
        l.append(v[0])
    return l


def get_boundary_data(level_mode='district'):
    engine = create_engine('mysql+pymysql://hcb_algorithms_w:Nkdls1029dsk2z@10.6.1.52:3306/db_algorithms')
    Session = sessionmaker(bind=engine)
    session = Session()
    if level_mode == 'city':
        sql = """select adcode,citycode,center,`level`,polyline,province,city from boundary_data WHERE `level`='city';"""
    elif level_mode == 'district':
        sql = """select adcode,citycode,center,`level`,polyline,province,city from boundary_data WHERE `level`='district' UNION ALL
                 select adcode,citycode,center,`level`,polyline,province,city from boundary_data GROUP BY city HAVING COUNT(city)=1 AND `level`= 'city';"""
    elif level_mode == 'province':
        sql = """select adcode,citycode,center,`level`,polyline,`name`,city from boundary_data WHERE `level`='province';"""
    else:
        raise ValueError
    rows = session.execute(sql)
    rows = rows.fetchall()
    session.close()

    rows = [x.values() for x in rows]

    rows = json.dumps(rows)
    with open('boundary_data_district.json', 'w', encoding='utf-8') as f:
        f.write(rows)

    return rows


def get_boundary_data_by_file():
    with open('./main/BaseData/boundary_data_city.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def get_boundary_data_by_file_new():
    with open('./BaseData/boundary_data_province.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def main_func_batch_True(point_list, boundary_data):
    old_boundary = copy.deepcopy(boundary_data)
    final_result_list = []
    for point in point_list:
        L = []
        for row in boundary_data:
            row = copy.deepcopy(row)
            try:
                del row[4]
            except:
                print(row)
            if len(row[2]) >= 2:
                point1 = (float(str(row[2]).split(',')[0]), float(str(row[2]).split(',')[1]))
                d = haversine(point, point1)
                row.append(d)
                # print(row)
                L.append(row)
        L.sort(key=operator.itemgetter(6))
        area_id_list = []
        for v in L[:10]:
            area_id_list.append(v[0])
        aLon, aLat = point
        poly_data = list(filter(lambda x: x[0] in area_id_list, old_boundary))
        flag = 0
        for data in poly_data:
            if data:
                try:
                    l_group = data[4].split('|')
                    result_list = []
                    for group_ in l_group:
                        pointList = []
                        group = group_.split(';')
                        for item in group:
                            if ',' in item:
                                coor = (float(item.split(',')[0]), float(item.split(',')[1]))
                                pointList.append(coor)
                            else:
                                pass
                        result = IsPtInPoly(aLon, aLat, pointList)
                        result_list.append(result)
                    if True in result_list:
                        data = list(data)
                        del data[4]
                        final_result_list.append(data)
                        flag = 1
                except:
                    print(data)
                    raise KeyError
        if flag == 0:
            print(point)
            final_result_list.append('None')

    if len(final_result_list) == 0:
        return None
    else:
        return final_result_list


def main_func_batch_False(point_list, level_mode):
    if len(point_list) == 1:
        point = point_list[0]
        aLon, aLat = point
        area_id_list = center_distance(point, level_mode=level_mode)
        str_ = str(tuple(area_id_list))
        sql = """SELECT * FROM boundary_data WHERE adcode IN %s""" % str_
        rows = read_table_by_sql(sql)
        for row in rows:
            if row:
                l_group = row[5].split('|')
                result_list = []
                for group_ in l_group:
                    pointList = []
                    group = group_.split(';')
                    for item in group:
                        if ',' in item:
                            try:
                                coor = (float(item.split(',')[0]), float(item.split(',')[1]))
                                pointList.append(coor)
                            except:
                                pass
                        else:
                            pass
                    result = IsPtInPoly(aLon, aLat, pointList)
                    result_list.append(result)
                # print(result_list)
                if True in result_list:

                    row = list(row)
                    del row[5]
                    return [row]
        return None
    else:
        raise ValueError


def main_func_lonlat2ad(point_list, level_mode='city', batch=True):
    if batch:
        if level_mode == 'province':
            boundary_data= get_boundary_data_by_file_new()
            result = main_func_batch_True(point_list, boundary_data)
            return result
        # boundary_data = get_boundary_data(level_mode)
        boundary_data = get_boundary_data_by_file()
        result = main_func_batch_True(point_list, boundary_data)
        return result
    else:
        result = main_func_batch_False(point_list, level_mode)
        return result


if __name__ == '__main__':
    """
    main参数说明
    # level_mode='district' 以区县粒度计算，默认以市级单位计算
    # level_mode='city' 以市级粒度计算，可不传，默认以市级单位计算
    # batch 批量开关，True为打开，False为关闭，默认为True，40个点以下建议False，否则强烈建议True

    传入数据格式
    point_in = [(112.463715, 24.905329), (113.750382, 23.045811)]
    batch=False 时, len(point_in)必须等于1 否则返回None
    """
    t_start = time.time()
    point_in = [(112.463715, 24.905329), (113.750382, 23.045811),(105.753304, 28.567266)]
    # point_in = [(113.750382, 23.045811)]
    result = main_func_lonlat2ad(point_in, level_mode='city', batch=True)
    # result = main_func(point_in, level_mode='city', batch=False)
    t_end = time.time()
    print(t_end-t_start)
    print(result)

