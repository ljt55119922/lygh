#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: provs_toll_rules
# Author  : yuanzhou
# Date    : 2018/8/16
# Description: 各省收费规则


def truck_type(truck_weight):
    if truck_weight < 2:
        return 1
    elif truck_weight >= 2 and truck_weight < 5:
        return 2
    elif truck_weight >= 5 and truck_weight < 10:
        return 3
    elif truck_weight >= 10 and truck_weight < 15:
        return 4
    else:
        return 5


def Beijing_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G1京哈高速', 'G6京藏高速', 'G7京新高速', 'G45大广高速', 'G4501六环路', 'G102通燕高速', 'G106京广线',
              'S15京津高速', 'S36机场北线', 'S46京平高速', '京哈高速', '京藏高速', '京新高速', '大广高速', '六环路', '通燕高速',
              '京广线', '京津高速', '机场北线', '京平高速', 'G1', 'G6', 'G7', 'G45', 'G4501', 'G102', 'G106',
              'S15', 'S36', 'S46', None]
    road_2 = ['G2京沪高速', '京沪高速', 'G2']
    road_3 = ['G4京港澳高速', '京港澳高速', 'G4']
    road_4 = ['S46京平高速', 'S51机场第二高速', '京平高速', '机场第二高速', 'S46', 'S51']
    road_5 = ['G103京塘线', 'S12机场高速', '京塘线', '机场高速', 'G103', 'S12']
    if road_name in road_2:
        if _type == 1:
            return [1, 0.34, None]
        elif _type == 2:
            return [1.382, 0.47, None]
        elif _type == 3:
            return [1.794, 0.61, None]
        elif _type == 4:
            return [2.382, 0.81, None]
        elif _type == 5:
            return [2.382, 0.81, None]
    elif road_name in road_3:
        if _type == 1:
            return [1, 0.33, None]
        elif _type == 2:
            return [2, 0.66, None]
        elif _type == 3:
            return [3, 0.99, None]
        elif _type == 4:
            return [5.97, 1.97, None]
        elif _type == 5:
            return [7.58, 2.5, None]
    elif road_name in road_4:
        if _type == 1:
            return [1, None, 10]
        elif _type == 2:
            return [2, None, 20]
        elif _type == 3:
            return [3, None, 30]
        elif _type == 4:
            return [3, None, 30]
        elif _type == 5:
            return [3, None, 30]
    elif road_name in road_5:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [2, 1, None]
        elif _type == 3:
            return [3, 1.5, None]
        elif _type == 4:
            return [4, 2, None]
        elif _type == 5:
            return [4, 2, None]
    else:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [2, 1, None]
        elif _type == 3:
            return [3, 1.5, None]
        elif _type == 4:
            return [3.6, 1.8, None]
        elif _type == 5:
            return [4, 2, None]


def Tianjin_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = [None]
    road_2 = ['S40京津塘高速', '京津塘高速', 'S40']
    road_3 = ['S3津滨高速', '津滨高速', 'S3']
    if road_name in road_2:
        if _type == 1:
            return [1, 0.34, None]
        elif _type == 2:
            return [1.382, 0.47, None]
        elif _type == 3:
            return [1.794, 0.61, None]
        elif _type == 4:
            return [2.382, 0.81, None]
        elif _type == 5:
            return [2.382, 0.81, None]
    elif road_name in road_3:
        if truck_weight <= 1:
            _type = 1
        elif truck_weight > 1 and truck_weight <= 7:
            _type = 2
        elif truck_weight > 7 and truck_weight <= 15:
            _type = 3
        else:
            _type = 4

        if _type == 1:
            return [1, 0.36, None]
        elif _type == 2:
            return [0.54/0.36, 0.54, None]
        elif _type == 3:
            return [0.71/0.36, 0.71, None]
        elif _type == 4:
            return [1.07/0.36, 1.07, None]
    else:
        if _type == 1:
            return [1, 0.55, None]
        elif _type == 2:
            return [0.95 / 0.55, 0.95, None]
        elif _type == 3:
            return [1.55 / 0.55, 1.55, None]
        elif _type == 4:
            return [1.75 / 0.55, 1.75, None]
        elif _type == 5:
            return [1.9 / 0.55, 1.9, None]


def Hebei_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = [None, 'G5京昆高速', 'G0401石家庄绕城高速', 'G6京藏高速', 'S12张承高速', 'S010张石高速', 'G22青兰高速',
              'S2511唐曹高速', 'G18荣乌高速', 'G2京沪高速', 'G3京台高速', 'G20青银高速', 'S009邢临高速', '京昆高速',
              '石家庄绕城高速', '京藏高速', '张承高速', '张石高速', '青兰高速',
              '唐曹高速', '荣乌高速', '京沪高速', '京台高速', '青银高速', '邢临高速', 'G5', 'G0401', 'G6', 'S12',
              'S010', 'G22', 'S2511', 'G18', 'G2', 'G3', 'G20', 'S009']
    road_2_1 = ['G45大广高速', '大广高速', 'G45']
    road_2_2 = ['G1京哈高速', '京哈高速', 'G1']
    road_2_3 = ['G2502唐山绕城高速', 'G25长深高速', '唐山绕城高速',
              '长深高速', 'G2502', 'G25']
    road_3 = ['G5京昆高速石家庄段', '京昆高速石家庄段', 'G5']
    road_4 = ['S004唐港高速', '唐港高速', 'S004']
    road_5 = ['G106京开高速', 'G205津晋高速', '京开高速', '津晋高速', 'G106', 'G205']
    road_6 = ['S003宣大高速', '宣大高速', 'S003']
    road_7 = ['G1811黄石高速', 'G45大广高速', 'S006衡德高速', '黄石高速', '大广高速', '衡德高速', 'G1811', 'G45', 'S006']
    if road_name in road_2_1:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [2, 1, None]
        elif _type == 3:
            return [3, 1.5, None]
        elif _type == 4:
            return [3.6, 1.8, None]
        elif _type == 5:
            return [0.075*int(truck_weight)/0.5, 0.075*int(truck_weight), None]
    elif road_name in road_2_2:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [2, 1, None]
        elif _type == 3:
            return [3, 1.5, None]
        elif _type == 4:
            return [3.6, 1.8, None]
        elif _type == 5:
            return [4.2, 2.1, None]
    elif road_name in road_2_3:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [1.76, 0.88, None]
        elif _type == 3:
            return [2.76, 1.38, None]
        elif _type == 4:
            return [3.4, 1.7, None]
        elif _type == 5:
            return [0.11*int(truck_weight)/0.5, 0.11*int(truck_weight), None]
    elif road_name in road_3:
        if _type == 1:
            return [1, 0.36, None]
        elif _type == 2:
            return [2, 0.72, None]
        elif _type == 3:
            return [4, 1.44, None]
        elif _type == 4:
            return [1.73/0.36, 1.73, None]
        elif _type == 5:
            return [0.1*int(truck_weight)/0.36, 0.1*int(truck_weight), None]
    elif road_name in road_4:
        if _type == 1:
            return [1, None, 5]
        elif _type == 2:
            return [2, None, 10]
        elif _type == 3:
            return [3, None, 15]
        elif _type == 4:
            return [4, None, 20]
        elif _type == 5:
            return [5, None, 25]
    elif road_name in road_5:
        if _type == 1:
            return [1, None, 10]
        elif _type == 2:
            return [1.5, None, 15]
        elif _type == 3:
            return [2.5, None, 25]
        elif _type == 4:
            return [3, None, 30]
        elif _type == 5:
            return [3.4, None, 34]
    elif road_name in road_6:
        if _type == 1:
            return [1, 0.35, None]
        elif _type == 2:
            return [0.6/0.35, 0.6, None]
        elif _type == 3:
            return [1/0.35, 1, None]
        elif _type == 4:
            return [1.2/0.35, 1.2, None]
        elif _type == 5:
            return [0.07*int(truck_weight)/0.35, 0.07*int(truck_weight), None]
    elif road_name in road_7:
        if _type == 1:
            return [1, 0.3, None]
        elif _type == 2:
            return [0.5/0.3, 0.5, None]
        elif _type == 3:
            return [1/0.3, 1, None]
        elif _type == 4:
            return [1.2/0.3, 1.2, None]
        elif _type == 5:
            return [0.07*int(truck_weight)/0.3, 0.07*int(truck_weight), None]
    else:
        if _type == 1:
            return [1, 0.4, None]
        elif _type == 2:
            return [0.7/0.4, 0.7, None]
        elif _type == 3:
            return [1.1/0.4, 1.1, None]
        elif _type == 4:
            return [1.36/0.4, 1.36, None]
        elif _type == 5:
            return [0.08*int(truck_weight)/0.4, 0.08*int(truck_weight), None]


def Neimenggu_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G6京藏高速', 'G65包茂高速', '京藏高速', '包茂高速', 'G6', 'G65', None]
    if truck_weight <= 2:
        _type = 1
    elif truck_weight > 2 and truck_weight <= 5:
        _type = 2
    elif truck_weight > 5 and truck_weight <= 10:
        _type = 3
    elif truck_weight >10 and truck_weight <= 15:
        _type = 4
    elif truck_weight >15 and truck_weight <= 25:
        _type = 5
    elif truck_weight > 25:
        _type = 6

    mile = 150
    if _type == 1:
        return [1, 0.4, 15]
    elif _type == 2:
        return [(mile*0.4+20)/(mile*0.4+15), 0.4, 20]
    elif _type == 3:
        return [(mile*0.85+35)/(mile*0.4+20), 0.85, 35]
    elif _type == 4:
        return [(mile*1.1+45)/(mile*0.85+35), 1.1, 45]
    elif _type == 5:
        return [(mile * 1.3 + 60) / (mile * 1.1 + 45), 1.3, 60]
    elif _type == 6:
        return [(mile * (1.3 + (truck_weight - 25) * 0.1) + 60 + (truck_weight - 25) * 2) / (mile * 1.3 + 60),
                1.3 + (truck_weight - 25) * 0.1,
                60 + (truck_weight - 25) * 2]


def Shanxi_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G040二河线', '二河线', 'G040']
    road_2 = ['G20青银高速', '青银高速', 'G20']
    road_3 = ['G5501大同绕城高速', '大同绕城高速', 'G5501']
    road_4 = ['S83运风高速', '运风高速', 'S83']
    if axle == 2 and wheels == 4 and front_length <= 1.3:
        _type = 'A'
    elif axle == 2 and wheels == 4 and front_length > 1.3:
        _type = 'B'
    elif axle == 2 and wheels == 6 and front_length <= 2.5:
        _type = 'C'
    elif (axle == 2 and wheels == 6) or (axle == 3 and wheels <= 8) and front_length > 2.5:
        _type = 'D'
    elif axle <= 4 and wheels > 8 and wheels <= 10 and front_length > 2.5:
        _type = 'E'
    elif axle <= 4 and wheels > 10 and wheels <= 14 and front_length > 2.5:
        _type = 'F'
    elif axle <= 5 and front_length > 2.5:
        _type = 'G'

    if road_name in road_1:
        if _type == 'A':
            return [1, 0.33, None]
        if _type == 'B':
            return [0.45/0.33, 0.45, None]
        if _type == 'C':
            return [0.7/0.33, 0.7, None]
        if _type == 'D':
            return [1.28/0.33, 1.28, None]
        if _type == 'E':
            return [1.76/0.33, 1.76, None]
        if _type == 'F':
            return [2.41/0.33, 2.41, None]
        if _type == 'G':
            return [3.39/0.33, 3.39, None]
    elif road_name in road_2:
        if _type == 'A':
            return [1, 0.36, None]
        if _type == 'B':
            return [0.54/0.36, 0.54, None]
        if _type == 'C':
            return [0.87/0.36, 0.87, None]
        if _type == 'D':
            return [1.41/0.36, 1.41, None]
        if _type == 'E':
            return [1.96/0.36, 1.96, None]
        if _type == 'F':
            return [2.68/0.36, 2.68, None]
        if _type == 'G':
            return [3.77/0.36, 3.77, None]
    elif road_name in road_3:
        if _type == 'A':
            return [1, 0.36, None]
        if _type == 'B':
            return [0.54/0.36, 0.54, None]
        if _type == 'C':
            return [0.87/0.36, 0.87, None]
        if _type == 'D':
            return [1.41/0.36, 1.41, None]
        if _type == 'E':
            return [1.86/0.36, 1.86, None]
        if _type == 'F':
            return [2.41/0.36, 2.41, None]
        if _type == 'G':
            return [3.2/0.36, 3.2, None]
    elif road_name in road_4:
        if _type == 'A':
            return [1, 0.36, None]
        if _type == 'B':
            return [0.54/0.36, 0.54, None]
        if _type == 'C':
            return [0.87/0.36, 0.87, None]
        if _type == 'D':
            return [1.41/0.36, 1.41, None]
        if _type == 'E':
            return [1.86/0.36, 1.86, None]
        if _type == 'F':
            return [2.41/0.36, 2.41, None]
        if _type == 'G':
            return [3.2/0.36, 3.2, None]
    else:
        if _type == 'A':
            return [1, 0.33, None]
        if _type == 'B':
            return [0.45/0.33, 0.45, None]
        if _type == 'C':
            return [0.7/0.33, 0.7, None]
        if _type == 'D':
            return [1.28/0.33, 1.28, None]
        if _type == 'E':
            return [1.76/0.33, 1.76, None]
        if _type == 'F':
            return [2.41/0.33, 2.41, None]
        if _type == 'G':
            return [3.39/0.33, 3.39, None]


def Shandong_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.4, None]
    elif _type == 2:
        return [1.8, 0.72, None]
    elif _type == 3:
        return [2.5, 1, None]
    elif _type == 4:
        return [3, 1.2, None]
    elif _type == 5:
        return [3.5, 1.4, None]


def Shanghai_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.6, None]
    elif _type == 2:
        return [1.5, 0.9, None]
    elif _type == 3:
        return [1.02/0.6, 1.02, None]
    elif _type == 4:
        return [1.315/0.6, 1.315, None]
    elif _type == 5:
        return [1.428/0.6, 1.428, None]


def Anhui_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.4, None]
    elif _type == 2:
        return [0.72/0.4, 0.72, None]
    elif _type == 3:
        return [1/0.4, 1, None]
    elif _type == 4:
        return [1.2/0.4, 1.2, None]
    elif _type == 5:
        return [1.4/0.4, 1.4, None]


def Zhejiang_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.4, None]
    elif _type == 2:
        return [2, 0.8, None]
    elif _type == 3:
        return [3, 1.2, None]
    elif _type == 4:
        return [4, 1.6, None]
    elif _type == 5:
        return [5, 2, None]


def Jiangsu_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['南京机场高速闸道站']
    road_2 = ['南京机场高速主线站']
    road_3 = ['南京二桥']
    road_4 = ['江阴大桥']
    road_5 = ['沪苏浙高速']
    road_6 = ['苏通大桥']
    road_7 = ['苏通大桥南北岸接线高速']
    road_8 = ['润扬长江公路大桥接线高速']
    road_9 = ['宁合高速']

    if road_name in road_1:
        if _type == 1:
            return [1, None, 10]
        elif _type == 2:
            return [1, None, 10]
        elif _type == 3:
            return [1.5, None, 15]
        elif _type == 4:
            return [3, None, 30]
        elif _type == 5:
            return [4.5, None, 45]
    elif road_name in road_2:
        if _type == 1:
            return [1, None, 20]
        elif _type == 2:
            return [1, None, 20]
        elif _type == 3:
            return [1.5, None, 30]
        elif _type == 4:
            return [3, None, 60]
        elif _type == 5:
            return [4.5, None, 90]
    elif road_name in road_3:
        if _type == 1:
            return [1, None, 20]
        elif _type == 2:
            return [1.5, None, 30]
        elif _type == 3:
            return [2.5, None, 50]
        elif _type == 4:
            return [2.5, None, 50]
        elif _type == 5:
            return [4, None, 80]
    elif road_name in road_4:
        if _type == 1:
            return [1, None, 25]
        elif _type == 2:
            return [35/25, None, 35]
        elif _type == 3:
            return [60/25, None, 60]
        elif _type == 4:
            return [95/25, None, 95]
        elif _type == 5:
            return [4, None, 100]
    elif road_name in road_5:
        if _type == 1:
            return [1, 0.55, None]
        elif _type == 2:
            return [0.83/0.55, 0.83, None]
        elif _type == 3:
            return [1.1/0.55, 1.1, None]
        elif _type == 4:
            return [1.1/0.55, 1.1, None]
        elif _type == 5:
            return [1.93/0.55, 1.93, None]
    elif road_name in road_6:
        if _type == 1:
            return [1, None, 30]
        elif _type == 2:
            return [40/30, None, 40]
        elif _type == 3:
            return [60/30, None, 60]
        elif _type == 4:
            return [60/30, None, 60]
        elif _type == 5:
            return [4, None, 120]
    elif road_name in road_7:
        if _type == 1:
            return [1, 0.45, None]
        elif _type == 2:
            return [0.68/0.45, 0.68, None]
        elif _type == 3:
            return [0.9/0.45, 0.9, None]
        elif _type == 4:
            return [1.35/0.45, 1.35, None]
        elif _type == 5:
            return [1.58/0.45, 1.58, None]
    elif road_name in road_8:
        if _type == 1:
            return [1, 0.45, None]
        elif _type == 2:
            return [0.68/0.45, 0.68, None]
        elif _type == 3:
            return [0.9/0.45, 0.9, None]
        elif _type == 4:
            return [1.35/0.45, 1.35, None]
        elif _type == 5:
            return [1.58/0.45, 1.58, None]
    elif road_name in road_9:
        if _type == 1:
            return [1, None, 15]
        elif _type == 2:
            return [20/15, None, 20]
        elif _type == 3:
            return [25/15, None, 25]
        elif _type == 4:
            return [40/15, None, 40]
        elif _type == 5:
            return [55/15, None, 55]
    else:
        if _type == 1:
            return [1, 0.45, None]
        elif _type == 2:
            return [0.68/0.45, 0.68, None]
        elif _type == 3:
            return [0.9/0.45, 0.9, None]
        elif _type == 4:
            return [1.35/0.45, 1.35, None]
        elif _type == 5:
            return [1.58/0.45, 1.58, None]


def Guangdong_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if axle == 2 and (wheels >= 2 or wheels < 4) and front_length < 1.3:
        _type = 1
    elif axle == 2 and (wheels == 4) and front_length >= 1.3:
        _type = 2
    elif axle == 2 and (wheels == 6) and front_length >= 1.3:
        _type = 3
    elif axle == 3 and (wheels >= 6 or wheels < 10) and front_length >= 1.3:
        _type = 4
    elif axle > 3 and (wheels > 10) and front_length >= 1.3:
        _type = 5

    road_1 = ['G94梅观高速', 'G15机荷高速', 'G25盐排高速', '梅观高速', '机荷高速', '盐排高速', 'G94', 'G15', 'G25']

    if road_name in road_1:
        if _type == 1:
            return [1, 0.6, None]
        elif _type == 2:
            return [2, 1.2, None]
        elif _type == 2:
            return [3, 1.8, None]
        elif _type == 2:
            return [4, 2.4, None]
        elif _type == 2:
            return [5, 3, None]
    else:
        if _type == 1:
            return [1, 0.6, None]
        elif _type == 2:
            return [1.5, 0.9, None]
        elif _type == 3:
            return [2, 1.2, None]
        elif _type == 4:
            return [3, 1.8, None]
        elif _type == 5:
            return [3.5, 2.1, None]


def Fujian_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.6, None]
    elif _type == 2:
        return [2, 1.2, None]
    elif _type == 3:
        return [3, 1.8, None]
    elif _type == 4:
        return [3.5, 2.1, None]
    elif _type == 5:
        return [4.5, 2.7, None]


def Guangxi_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.4, None]
    elif _type == 2:
        return [2, 0.8, None]
    elif _type == 3:
        return [3, 1.2, None]
    elif _type == 4:
        return [1.44/0.4, 1.44, None]
    elif _type == 5:
        return [1.68/0.4, 1.68, None]


def Hubei_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.6, None]
    elif _type == 2:
        return [1.5, 0.9, None]
    elif _type == 3:
        return [2, 1.2, None]
    elif _type == 4:
        return [2.5, 1.5, None]
    elif _type == 5:
        return [3, 1.8, None]


def Henan_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if truck_weight < 2:
        _type = 'A'
    elif truck_weight >= 2 and truck_weight < 5:
        _type = 'B'
    elif truck_weight >= 5 and truck_weight < 8:
        _type = 'C'
    elif truck_weight >= 8 and truck_weight < 20:
        _type = 'D'
    elif truck_weight >= 20 and truck_weight < 40:
        _type = 'E'
    elif truck_weight >= 40:
        _type = 'F'

    if _type == 'A':
        return [1, 0.45, None]
    elif _type == 'B':
        return [0.7/0.45, 0.7, None]
    elif _type == 'C':
        return [1.3/0.45, 1.3, None]
    elif _type == 'D':
        return [1.65/0.45, 1.65, None]
    elif _type == 'E':
        return [2/0.45, 2, None]
    elif _type == 'F':
        return [truck_weight*0.08/0.45, truck_weight*0.08, None]


def Hunan_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G56杭瑞高速', 'G60上昆高速', '杭瑞高速', '上昆高速', 'G56', 'G60']

    if road_name in road_1:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [0.8/0.5, 0.8, None]
        elif _type == 3:
            return [1.1/0.5, 1.1, None]
        elif _type == 4:
            return [1.3/0.5, 1.3, None]
        elif _type == 5:
            return [1.5/0.5, 1.5, None]
    else:
        if _type == 1:
            return [1, 0.4, None]
        elif _type == 2:
            return [0.7/0.4, 0.7, None]
        elif _type == 3:
            return [1/0.4, 1, None]
        elif _type == 4:
            return [1.2/0.4, 1.2, None]
        elif _type == 5:
            return [1.4/0.4, 1.4, None]


def Jiangxi_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if truck_weight <= 10:
        _type = 1
    elif truck_weight > 10 and truck_weight <= 40:
        _type = 2
    else:
        _type = 3

    if _type == 1:
        truck_weight = 5
        return [truck_weight*0.08/0.4, 0.4, None]
    elif _type == 2:
        return [(-0.001*truck_weight + 0.07)*truck_weight/0.4, -0.001*truck_weight + 0.07, None]
    else:
        return [1.2/0.4, 1.2, None]


def Liaoning_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.45, None]
    elif _type == 2:
        return [0.8/0.45, 0.8, None]
    elif _type == 3:
        return [1.15/0.45, 1.15, None]
    elif _type == 4:
        return [1.45/0.45, 1.45, None]
    elif _type == 5:
        return [1.7/0.45, 1.7, None]


def Heilongjiang_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G10绥满高速', '绥满高速', 'G10']
    road_2 = ['G1011哈同高速', '哈同高速', 'G1011']
    road_3 = ['G11鹤大高速', '鹤大高速', 'G11']
    if road_name in road_1:
        if _type == 1:
            return [1, 0.37, None]
        elif _type == 2:
            return [0.52/0.37, 0.52, None]
        elif _type == 3:
            return [0.68/0.37, 0.68, None]
        elif _type == 4:
            return [0.82/0.37, 0.82, None]
        elif _type == 5:
            return [0.93/0.37, 0.93, None]
    elif road_name in road_2:
        if _type == 1:
            return [1, 0.35, None]
        elif _type == 2:
            return [0.5/0.35, 0.5, None]
        elif _type == 3:
            return [0.7/0.35, 0.7, None]
        elif _type == 4:
            return [0.8/0.35, 0.8, None]
        elif _type == 5:
            return [1.2/0.35, 1.2, None]
    elif road_name in road_3:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [0.9/0.5, 0.9, None]
        elif _type == 3:
            return [1.2/0.5, 1.2, None]
        elif _type == 4:
            return [1.3/0.5, 1.3, None]
        elif _type == 5:
            return [1.6/0.5, 1.6, None]
    else:
        if _type == 1:
            return [1, 0.45, None]
        elif _type == 2:
            return [0.85/0.45, 0.85, None]
        elif _type == 3:
            return [1.1/0.45, 1.1, None]
        elif _type == 4:
            return [1.2/0.45, 1.2, None]
        elif _type == 5:
            return [1.4/0.45, 1.4, None]


def Jilin_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G1京哈高速', '京哈高速', 'G1', 'G0102长春绕城高速', '长春绕城高速', 'G0102']
    road_2 = ['G12晖乌高速', '晖乌高速', 'G12']
    if road_name in road_1:
        if _type == 1:
            return [1, 0.4, None]
        elif _type == 2:
            return [0.6/0.4, 0.6, None]
        elif _type == 3:
            return [0.8/0.4, 0.8, None]
        elif _type == 4:
            return [1.2/0.4, 1.2, None]
        elif _type == 5:
            return [1.4/0.4, 1.4, None]
    elif road_name in road_2:
        if _type == 1:
            return [1, 0.3, None]
        elif _type == 2:
            return [0.5/0.3, 0.5, None]
        elif _type == 3:
            return [0.8/0.3, 0.8, None]
        elif _type == 4:
            return [1.2/0.3, 1.2, None]
        elif _type == 5:
            return [1.4/0.3, 1.4, None]
    else:
        if _type == 1:
            return [1, 0.4, None]
        elif _type == 2:
            return [0.6/0.4, 0.6, None]
        elif _type == 3:
            return [0.8/0.4, 0.8, None]
        elif _type == 4:
            return [1.2/0.4, 1.2, None]
        elif _type == 5:
            return [1.4/0.4, 1.4, None]


def Shananxi_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.4, None]
    elif _type == 2:
        return [0.7 / 0.4, 0.7, None]
    elif _type == 3:
        return [0.9 / 0.4, 0.9, None]
    elif _type == 4:
        return [1.12 / 0.4, 1.12, None]
    elif _type == 5:
        return [1.3 / 0.4, 1.3, None]


def Xinjiang_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G045吐乌大公路', '吐乌大公路', 'G045']
    road_2 = ['G045乌奎公路', 'G045']

    if _type == 1:
        return [1, None, 10]
    elif _type == 2:
        return [1.5, None, 15]
    elif _type == 3:
        return [2, None, 20]
    elif _type == 4:
        return [3.5, None, 35]
    elif _type == 5:
        return [4, None, 40]


def Gansu_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    return [truck_weight*0.09/0.4, truck_weight*0.09, None]


def Ningxia_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.3, None]
    elif _type == 2:
        return [0.5 / 0.3, 0.5, None]
    elif _type == 3:
        return [0.7 / 0.3, 0.7, None]
    elif _type == 4:
        return [0.85 / 0.3, 0.85, None]
    elif _type == 5:
        return [1 / 0.3, 1, None]


def Qinghai_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    if _type == 1:
        return [1, 0.45, None]
    elif _type == 2:
        return [0.6 / 0.45, 0.6, None]
    elif _type == 3:
        return [0.9 / 0.45, 0.9, None]
    elif _type == 4:
        return [1 / 0.45, 1, None]
    elif _type == 5:
        return [1.2 / 0.45, 1.2, None]


def Chongqing_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G85渝昆高速', '渝昆高速', 'G85', '渝涪高速', 'G65包茂高速', '包茂高速', 'G65',
              'G75兰海高速', '兰海高速', 'G75', 'G50沪渝高速', '沪渝高速', 'G50',
              'G42沪蓉高速', '沪蓉高速', 'G42', 'G93成渝环线高速', '成渝环线高速', 'G93']
    road_2 = ['G75兰海高速', '兰海高速', 'G75', 'G65包茂高速', '包茂高速', 'G65', '綦万高速']
    road_3 = ['G42沪蓉高速', '沪蓉高速', 'G42']
    road_4 = ['中梁山隧道', '铁山坪隧道', '黄草山隧道', '沙溪庙大桥', '大学城隧道', '铁峰山1号隧道', '南山隧道',
              '太平隧道', '石龙隧道', '明月山隧道', '宝鼎山隧道', '谭家寨隧道', '忠县长江大桥', '方斗山隧道',
              '庙梁隧道', '人和隧道']
    road_5 = ['缙云山隧道', '华山隧道', '云雾山隧道', '铁峰山2号隧道', '吕家梁隧道']
    if road_name in road_1:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [1 / 0.5, 1, None]
        elif _type == 3:
            return [1.5 / 0.5, 1.5, None]
        elif _type == 4:
            return [2 / 0.5, 2, None]
        elif _type == 5:
            return [2.5 / 0.5, 2.5, None]
    elif road_name in road_2:
        if _type == 1:
            return [1, 0.6, None]
        elif _type == 2:
            return [1.2 / 0.6, 1.2, None]
        elif _type == 3:
            return [1.8 / 0.6, 1.8, None]
        elif _type == 4:
            return [2.4 / 0.6, 2.4, None]
        elif _type == 5:
            return [3 / 0.6, 3, None]
    elif road_name in road_3:
        if _type == 1:
            return [1, 0.9, None]
        elif _type == 2:
            return [1.8 / 0.9, 1.8, None]
        elif _type == 3:
            return [2.7 / 0.9, 2.7, None]
        elif _type == 4:
            return [3.6 / 0.9, 3.6, None]
        elif _type == 5:
            return [4.5 / 0.9, 4.5, None]
    elif road_name in road_4:
        if _type == 1:
            return [1, None, 5]
        elif _type == 2:
            return [2, None, 10]
        elif _type == 3:
            return [3, None, 15]
        elif _type == 4:
            return [4, None, 20]
        elif _type == 5:
            return [5, None, 25]
    elif road_name in road_5:
        if _type == 1:
            return [1, None, 10]
        elif _type == 2:
            return [2, None, 20]
        elif _type == 3:
            return [3, None, 30]
        elif _type == 4:
            return [4, None, 40]
        elif _type == 5:
            return [5, None, 50]
    else:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [1 / 0.5, 1, None]
        elif _type == 3:
            return [1.5 / 0.5, 1.5, None]
        elif _type == 4:
            return [2 / 0.5, 2, None]
        elif _type == 5:
            return [2.5 / 0.5, 2.5, None]


def Sichuan_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G5京昆高速', '京昆高速', 'G5', 'G42沪蓉高速', '沪蓉高速', 'G42', 'G318成温邛高速', '成温邛高速', 'G318']
    road_2 = ['G5京昆高速', '京昆高速', 'G5', 'G42沪蓉高速', '沪蓉高速', 'G42', 'G75兰海高速', '兰海高速', 'G75',
              'G76厦蓉高速', '厦蓉高速', 'G76', 'G93成渝环线公路', '成渝环线公路', 'G93']
    road_3 = ['G65包茂高速', '包茂高速', 'G65']
    road_4 = ['G4201成都绕城高速', '成都绕城高速', 'G4201']
    road_5 = ['机场高速']
    road_6 = ['环城高速', '龙泉山隧道']
    if road_name in road_1:
        if _type == 1:
            return [1, 0.45, None]
        elif _type == 2:
            return [0.9 / 0.45, 0.9, None]
        elif _type == 3:
            return [1.35 / 0.45, 1.35, None]
        elif _type == 4:
            return [1.8 / 0.45, 1.8, None]
        elif _type == 5:
            return [2.25 / 0.45, 2.25, None]
    elif road_name in road_2:
        if _type == 1:
            return [1, 0.35, None]
        elif _type == 2:
            return [0.7 / 0.35, 0.7, None]
        elif _type == 3:
            return [1.05 / 0.35, 1.05, None]
        elif _type == 4:
            return [1.4 / 0.35, 1.4, None]
        elif _type == 5:
            return [1.75 / 0.35, 1.75, None]
    elif road_name in road_3:
        if _type == 1:
            return [1, 0.5, None]
        elif _type == 2:
            return [1 / 0.5, 1, None]
        elif _type == 3:
            return [1.5 / 0.5, 1.5, None]
        elif _type == 4:
            return [2 / 0.5, 2, None]
        elif _type == 5:
            return [2.5 / 0.5, 2.5, None]
    elif road_name in road_4:
        if _type == 1:
            return [1, None, 4]
        elif _type == 2:
            return [2, None, 8]
        elif _type == 3:
            return [3, None, 12]
        elif _type == 4:
            return [4, None, 16]
        elif _type == 5:
            return [5, None, 20]
    elif road_name in road_5:
        if _type == 1:
            return [1, None, 20]
        elif _type == 2:
            return [2, None, 40]
        elif _type == 3:
            return [3, None, 60]
        elif _type == 4:
            return [4, None, 80]
        elif _type == 5:
            return [5, None, 100]
    elif road_name in road_6:
        if _type == 1:
            return [1, None, 5]
        elif _type == 2:
            return [2, None, 10]
        elif _type == 3:
            return [3, None, 15]
        elif _type == 4:
            return [4, None, 20]
        elif _type == 5:
            return [5, None, 25]
    else:
        if _type == 1:
            return [1, 0.45, None]
        elif _type == 2:
            return [0.9 / 0.45, 0.9, None]
        elif _type == 3:
            return [1.35 / 0.45, 1.35, None]
        elif _type == 4:
            return [1.8 / 0.45, 1.8, None]
        elif _type == 5:
            return [2.25 / 0.45, 2.25, None]


def Yunnan_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['曲胜高速']
    road_2 = ['砚平高速']
    road_3 = ['平锁高速', '思小高速', '昆安高速', '安楚高速']
    road_4 = ['嵩待高速']
    road_5 = ['昆石高速']
    road_6 = ['玉元高速']
    road_7 = ['大保高速', '楚大高速']

    if truck_weight <= 1:
        _type = 1
    elif truck_weight > 1 and truck_weight <= 3:
        _type = 2
    elif truck_weight > 3 and truck_weight <= 6:
        _type = 3
    elif truck_weight > 6 and truck_weight <= 9:
        _type = 4
    elif truck_weight > 9 and truck_weight <= 12:
        _type = 5
    else:
        _type = 6

    if road_name in road_1:
        if _type == 1:
            return [0.56 / 0.28, 0.56, None]
        elif _type == 2:
            return [0.84 / 0.28, 0.84, None]
        elif _type == 3:
            return [1.12 / 0.28, 1.12, None]
        elif _type == 4:
            return [1.4 / 0.28, 1.4, None]
        elif _type == 5:
            return [1.68 / 0.28, 1.68, None]
        elif _type == 6:
            return [1.96 / 0.28, 1.96, None]
    elif road_name in road_2:
        if _type == 1:
            return [0.64 / 0.32, 0.64, None]
        elif _type == 2:
            return [0.96 / 0.32, 0.96, None]
        elif _type == 3:
            return [1.28 / 0.32, 1.28, None]
        elif _type == 4:
            return [1.6 / 0.32, 1.6, None]
        elif _type == 5:
            return [1.92 / 0.32, 1.92, None]
        elif _type == 6:
            return [2.24 / 0.32, 2.24, None]
    elif road_name in road_3:
        if _type == 1:
            return [0.86 / 0.43, 0.86, None]
        elif _type == 2:
            return [1.29 / 0.43, 1.29, None]
        elif _type == 3:
            return [1.72 / 0.43, 1.72, None]
        elif _type == 4:
            return [2.15 / 0.43, 2.15, None]
        elif _type == 5:
            return [2.58 / 0.43, 2.58, None]
        elif _type == 6:
            return [3.01 / 0.43, 3.01, None]
    elif road_name in road_4:
        if _type == 1:
            return [0.7 / 0.35, 0.7, None]
        elif _type == 2:
            return [1.05 / 0.35, 1.05, None]
        elif _type == 3:
            return [1.4 / 0.35, 1.4, None]
        elif _type == 4:
            return [1.75 / 0.35, 1.75, None]
        elif _type == 5:
            return [2.1 / 0.35, 2.1, None]
        elif _type == 6:
            return [2.45 / 0.35, 2.45, None]
    elif road_name in road_5:
        if _type == 1:
            return [0.9 / 0.45, 0.9, None]
        elif _type == 2:
            return [1.35 / 0.45, 1.35, None]
        elif _type == 3:
            return [1.8 / 0.45, 1.8, None]
        elif _type == 4:
            return [2.25 / 0.45, 2.25, None]
        elif _type == 5:
            return [2.7 / 0.45, 2.7, None]
        elif _type == 6:
            return [3.15 / 0.45, 3.15, None]
    elif road_name in road_6:
        if _type == 1:
            return [0.52 / 0.26, 0.52, None]
        elif _type == 2:
            return [0.78 / 0.26, 0.78, None]
        elif _type == 3:
            return [1.04 / 0.26, 1.04, None]
        elif _type == 4:
            return [1.3 / 0.26, 1.3, None]
        elif _type == 5:
            return [1.56 / 0.26, 1.56, None]
        elif _type == 6:
            return [1.82 / 0.26, 1.82, None]
    elif road_name in road_7:
        if _type == 1:
            return [0.8 / 0.4, 0.8, None]
        elif _type == 2:
            return [1.2 / 0.4, 1.2, None]
        elif _type == 3:
            return [1.6 / 0.4, 1.6, None]
        elif _type == 4:
            return [2 / 0.4, 2, None]
        elif _type == 5:
            return [2.4 / 0.4, 2.4, None]
        elif _type == 6:
            return [2.8 / 0.4, 2.8, None]
    else:
        if _type == 1:
            return [0.56 / 0.28, 0.56, None]
        elif _type == 2:
            return [0.84 / 0.28, 0.84, None]
        elif _type == 3:
            return [1.12 / 0.28, 1.12, None]
        elif _type == 4:
            return [1.4 / 0.28, 1.4, None]
        elif _type == 5:
            return [1.68 / 0.28, 1.68, None]
        elif _type == 6:
            return [1.96 / 0.28, 1.96, None]


def Guizhou_toll_rule(truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    _type = truck_type(truck_weight)
    road_1 = ['G60沪昆高速', '沪昆高速', 'G60']
    road_2 = ['G75兰海高速', '兰海高速', 'G75', 'S55百茅线', '百茅线', 'S55', 'S01南环线', '南环线', 'S01']
    if road_name in road_1:
        if _type == 1:
            return [0.52 / 0.35, 0.52, None]
        elif _type == 2:
            return [1.22 / 0.35, 1.22, None]
        elif _type == 3:
            return [2.1 / 0.35, 2.1, None]
        elif _type == 4:
            return [2.62 / 0.35, 2.62, None]
        elif _type == 5:
            return [3.32 / 0.35, 3.32, None]
    elif road_name in road_2:
        if _type == 1:
            return [0.75 / 0.5, 0.75, None]
        elif _type == 2:
            return [1.75 / 0.5, 1.75, None]
        elif _type == 3:
            return [3 / 0.5, 3, None]
        elif _type == 4:
            return [3.75 / 0.5, 3.75, None]
        elif _type == 5:
            return [4.75 / 0.5, 4.75, None]
    else:
        if _type == 1:
            return [0.75 / 0.5, 0.75, None]
        elif _type == 2:
            return [1.75 / 0.5, 1.75, None]
        elif _type == 3:
            return [3 / 0.5, 3, None]
        elif _type == 4:
            return [3.75 / 0.5, 3.75, None]
        elif _type == 5:
            return [4.75 / 0.5, 4.75, None]


def provs_toll_rules(prov_name, truck_weight, road_name=None, axle=None, wheels=None, front_length=None):
    if prov_name in ['北京', '北京市']:
        return Beijing_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['天津', '天津市']:
        return Tianjin_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['河北', '河北省']:
        return Hebei_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['内蒙古', '内蒙古自治区']:
        return Neimenggu_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['山西', '山西省']:
        return Shanxi_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['山东', '山东省']:
        return Shandong_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['上海', '上海市']:
        return Shanghai_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['安徽', '安徽省']:
        return Anhui_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['浙江', '浙江省']:
        return Zhejiang_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['江苏', '江苏省']:
        return Jiangsu_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['广东', '广东省']:
        return Guangdong_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['福建', '福建省']:
        return Fujian_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['广西', '广西省', '广西壮族自治区']:
        return Guangxi_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['湖北', '湖北省']:
        return Hubei_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['河南', '河南省']:
        return Hubei_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['湖南', '湖南省']:
        return Hunan_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['江西', '江西省']:
        return Jiangxi_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['辽宁', '辽宁省']:
        return Liaoning_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['黑龙江', '黑龙江省']:
        return Heilongjiang_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['吉林', '吉林省']:
        return Jilin_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['陕西', '陕西省']:
        return Shananxi_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['新疆', '新疆省', '新疆维吾尔自治区']:
        return Xinjiang_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['甘肃', '甘肃省']:
        return Gansu_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['宁夏', '宁夏省', '宁夏回族自治区']:
        return Ningxia_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['青海', '青海省']:
        return Qinghai_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['重庆', '重庆市']:
        return Chongqing_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['四川', '四川省']:
        return Sichuan_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['云南', '云南省']:
        return Yunnan_toll_rule(truck_weight, road_name, axle, wheels, front_length)
    elif prov_name in ['贵州', '贵州省']:
        return Guizhou_toll_rule(truck_weight, road_name, axle, wheels, front_length)


if __name__ == '__main__':
    truck_weight = 10.4
    axle = 3
    wheels = 8
    front_length = 2.6
    prov_name = '北京'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '天津'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '河北'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '内蒙古'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '山西'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '山东'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '上海'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '安徽'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '浙江'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '江苏'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '广东'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '福建'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '广西'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '湖北'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '河南'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '湖南'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '江西'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '辽宁'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '吉林'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '陕西'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '新疆'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '甘肃'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '宁夏'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '青海'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '重庆'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '四川'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '云南'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
    prov_name = '贵州'
    print(provs_toll_rules(prov_name, truck_weight, axle=axle, wheels=wheels, front_length=front_length))
