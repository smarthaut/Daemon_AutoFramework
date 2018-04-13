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

class SearchTest(unittest.TestCase):
    excel = DATA_PATH

    def setUp(self):
        self.driver =Browser(timeout=60)
        self.search_page = SearchPage(self.driver)
        self.search_page.url = Config().get('BaiDuURl')
        self.search_page.visit()

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.search_page.set_value(element=self.search_page.rec_search_input(), text='huanghe')
        self.search_page.click_search_btn()
        self.search_page.get_windows_img()





