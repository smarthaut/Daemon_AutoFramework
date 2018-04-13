#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:32
# @Author  : huanghe
# @Site    : 
# @File    : search_page.py
# @Software: PyCharm
from src.utils.log import Logger
from src.test.common.base_page import Basepage

class SearchPage(Basepage):

    def rec_search_input(self):
        self.logger = Logger(loggername=self.__class__.__name__).get_logger()
        self.logger.debug(u'找到搜索Input.')
        return self.find_element(selector='id=>kw')

    def rec_search_btn(self):
        self.logger = Logger(loggername=self.__class__.__name__).get_logger()
        self.logger.debug(u'找到百度一下Input.')
        return self.find_element(selector='id=>su')

    def click_search_btn(self):
        self.rec_search_btn().click()
        self.logger = Logger(loggername=self.__class__.__name__).get_logger()
        self.logger.debug(u'点击"立即登录 "按钮.')

