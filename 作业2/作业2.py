#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import pymongo
app = Flask(__name__)

def get_mongo():
    myclient = pymongo.MongoClient('mongodb://localhost:27017')  # 填入mongodb的地址
    mydb = myclient['rb']  # 填入数据库名字
    mycol = mydb['rb']  # 填入集合名字
    for x in mycol.find(): #取数
        print(x)

@app.route('/')
def index():
    return render_template('index.html',x=x) #插入web中的表格

if __name__ == '__main__':
    app.run(debug=True)