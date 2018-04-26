#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 11:21
# @Author  : huanghe
# @Site    : 
# @File    : run.py
# @Software: PyCharm

import time
import unittest
from htmltestrunner.HTMLTestRunner import HTMLTestRunner

test_dir = './src/test/case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_ad_*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Aquapaas WEB ADV Test Report',
                            description='Implementation Example with: '

                            )
    run = HTMLTestRunner()
    runner.run(discover)
    fp.close()