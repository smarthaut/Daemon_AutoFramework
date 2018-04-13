#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:43
# @Author  : huanghe
# @Site    : 
# @File    : test.py
# @Software: PyCharm
'''a =3
c =1
b = 2
d =b if b and a else c
print(d)
print(a and b)
and 操作，a and b   a为真输出b  a为假输出a
'''
'''import logging

# 创建一个logger
logger = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('/tmp/test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#定义一个filter
#filter = logging.Filter('mylogger.child1.child2')
#fh.addFilter(filter)

# 给logger添加handler
#logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)



# 记录一条日志
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')'''

do = 'D:/python/Test_framework/report/screenpicture/20180412140429.png'
a = do.find('screenpicture')
print(a)
