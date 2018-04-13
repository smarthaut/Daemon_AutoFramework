#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 10:46
# @Author  : huanghe
# @Site    : 
# @File    : browser.py
# @Software: PyCharm
import os
from selenium import webdriver
from src.utils.config import DRIVER_PATH

CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'geckodriver', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get_browserdriver(self,*args,**kwargs):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type],*args,**kwargs)
        return self.driver


    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


class UnSupportBrowserTypeError(Exception):
    pass


if __name__ == '__main__':
    driver = Browser().get_browserdriver()
    driver.get('http://www.baidu.com')
    elem = driver.find_element_by_id('kw')
    print(elem.text)

