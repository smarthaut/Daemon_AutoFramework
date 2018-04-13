#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 10:58
# @Author  : huanghe
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os

from src.utils.file_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
LOG_PATH = os.path.join(BASE_PATH, 'log')
PIR_PATH = os.path.join(BASE_PATH,'report','screenpicture\\')
DATA_PATH = os.path.join(BASE_PATH,'data','baidu.xlsx')

class Config:
    def __init__(self,config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self,element,index=0):
        return self.config[index].get(element)


if __name__ == '__main__':
    c = Config()
    print(BASE_PATH)