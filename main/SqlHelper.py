# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 16:09
# @Author  : ljt
# @Site    : 
# @File    : SqlHelper.py
# @Software: PyCharm

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Date, Integer, String, ForeignKey, Text, TIMESTAMP, CHAR, Float
from sqlalchemy.orm import sessionmaker


# 创建表
def create_table():
    engine = create_engine('mysql+pymysql://hcb_algorithms_w:Nkdls1029dsk2z@10.6.1.52:3306/db_algorithms')
    metadata = MetaData(engine)

    # 定义表格
    user_table = Table('boundary_data', metadata,
                       Column('adcode', String(50), index=True),
                       Column('citycode', String(50), index=True),
                       Column('center', String(50)),
                       Column('name', String(100), index=True),
                       Column('level', String(50), index=True),
                       Column('polyline', Text)
                       )

    metadata.create_all()
    print('create table success!')


def read_table_by_sql(sql):
    engine = create_engine('mysql+pymysql://hcb_algorithms_w:Nkdls1029dsk2z@10.6.1.52:3306/db_algorithms')
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.execute(sql)
    session.close()
    return row.fetchall()


def execute_sql(sql):
    engine = create_engine('mysql+pymysql://hcb_algorithms_w:Nkdls1029dsk2z@10.6.1.52:3306/db_algorithms')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(sql)
    session.commit()
    session.close()


def insert_data(db_name, table_name, data):
    engine = create_engine('mysql+pymysql://hcb_algorithms_w:Nkdls1029dsk2z@10.6.1.52:3306/%s' % db_name)
    metadata = MetaData(engine)
    user_table = Table(table_name, metadata, autoload=True)

    conn = engine.connect()

    conn.execute(user_table.insert(), data)
    conn.close()


def is_null(text):
    if text == 'NULL':
        return ''
    else:
        return text


def insert_instance():
    with open('oil_station_info.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            col = line.strip().split('	')
            print(col)
            data = [{'station_id': int(col[0]),
                     'station_name': is_null(col[1]),
                     'enterprise_mark': is_null(col[2]),
                     'province': is_null(col[3]),
                     'city': is_null(col[4]),
                     'address': is_null(col[5]),
                     'longitude': is_null(col[6]),
                     'latitude': is_null(col[7]),
                     'online_mark': is_null(col[8]),
                     'qy_station_mark': is_null(col[9]),
                     'main_road_mark': is_null(col[10]),
                     'retail_price_pt': is_null(col[11]),
                     'settlement_price_pt': is_null(col[12]),
                     'discount_pt': is_null(col[13]),
                     'service_rate_pt': is_null(col[14]),
                     'purchase_price_qy': is_null(col[15]),
                     'purchase_discount_qy': is_null(col[16]),
                     'profit_rate_qy': is_null(col[17])}]

            insert_data('db_algorithms', 'oil_station_info', data)


def update():
    sql = """UPDATE boundary_data  SET polyline='0' WHERE adcode = '440523'"""
    execute_sql(sql)
    pass

if __name__ == '__main__':
    # sql_query = """select * from price_yard"""
    # sql_create_table = """CREATE TABLE test(id SERIAL,gov_id INT4,gov_name VARCHAR(255),year INT4,area VARCHAR(255))"""
    # sql_delete = """DELETE FROM buildings WHERE building_no = 2;"""

    # sql = """SELECT * FROM oil_station_info"""
    # rows = read_table_by_sql(sql)
    # for row in rows:
    #     print(row)
    # create_table()
    # update()
    pass