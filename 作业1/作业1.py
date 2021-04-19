#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pyhive
import datetime
import pymongo

def get_hive():
  conn = connect()#输入hive连接信息
  cursor = conn.cursor()
  cursor.execute('')#填入取数的sql
  for result in cursor.fetchall():
    print(result)

def add_database(result):
  myclient = pymongo.MongoClient('')   #填入mongodb的地址
  mydb  = myclient['']  #填入数据库名字
  mycol = mydb['']   #填入集合名字
  x = mycol.insert_marry(result)  # 插入hive数据
  for i in mycol.find():
    print(i)
