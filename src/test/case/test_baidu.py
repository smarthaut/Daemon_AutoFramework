#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:29
# @Author  : huanghe
# @Site    : 
# @File    : test_baidu.py
# @Software: PyCharm
import time
import unittest
from src.test.suit.baidu.search_page import SearchPage
from src.utils.browser import Browser
from src.utils.config import Config
from src.utils.file_reader import ExcelReader
from src.utils.config import DATA_PATH

excel = DATA_PATH
dates = ExcelReader(DATA_PATH).data

class SearchTest(unittest.TestCase):


    def setUp(self):
        self.driver =Browser().get_browserdriver()
        self.search_page = SearchPage(self.driver)
        self.search_page.url = Config().get('BaiDuURl')
        self.search_page.visit()

    def tearDown(self):
        self.search_page.quit_browser()

    def test_search(self):
        self.search_page.set_value(element=self.search_page.rec_search_input(), text=dates[1]['search'])
        self.search_page.click_search_btn()
        self.search_page.get_windows_img()





