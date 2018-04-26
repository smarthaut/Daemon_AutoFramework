#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 13:45
# @Author  : huanghe
# @Site    : 
# @File    : ad_position_page.py
# @Software: PyCharm
from src.utils.log import Logger
from src.test.common.base_page import Basepage

class AdPosition(Basepage):
    def rec_picture_btn(self):
        self.logger = Logger(loggername=self.__class__.__name__).get_logger()
        self.logger.debug(u'找到图文按钮')
        return self.find_element('css_selector=>div#adPos_adKind_tuwen')

    def click_picture_btn(self):
        self.rec_picture_btn().click()
        self.logger.debug(u'点击图文按钮')
        return Picture(self.driver)

class Picture(Basepage):
    def rec_create_btn(self):
        self.logger = Logger(loggername=self.__class__.__name__).get_logger()
        self.logger.debug(u'找到新建广告位按钮')
        return self.find_element('css_selector=>div.panel_page_button_text')
    def click_create_btn(self):
        self.rec_create_btn().click()
        self.logger.debug(u'点击新建广告位按钮')
