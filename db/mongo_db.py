#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 13:11
# @Author  : huanghe
# @Site    : 
# @File    : mongo_db.py
# @Software: PyCharm
import pymongo
from src.utils.config import Config

class DB:
    def __init__(self):
        cf = Config().get('mongodb')
        self.host = cf.get('host')
        self.port = cf.get('port')
        self.user = cf.get('user')
        self.password = cf.get('password')
        try:
            self.client = pymongo.MongoClient(self.host, port=int(self.port))
        except:
            print('数据库连接失败')

    def getConnection(self, table_name, connection_name):
        db = self.client.get_database(table_name)
        svod = db.get_collection(connection_name)
        return svod


if __name__ =='__main__':
    db =DB()
    print(db.host)