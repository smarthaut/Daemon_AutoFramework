#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 14:01
# @Author  : huanghe
# @Site    : 
# @File    : test_ad_position.py
# @Software: PyCharm
import unittest

from src.test.suit.aquapaasADV.login_page import LoginPage
from src.utils.browser import Browser
from src.utils.config import Config
import time

class AquaPaasAdvTest(unittest.TestCase):
    def setUp(self):
        self.driver = Browser().get_browserdriver()
        login_page = LoginPage(self.driver)
        login_page.url = Config().get('URL')
        login_page.visit()
        # time.sleep(10)
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(), text=Config().get('USER'))
        login_page.set_value(element=login_page.rec_passwd_input(), text=Config().get('PASSWORD'))
        login_page.click_login_btn()
        self.main_page = login_page.get_main_page()

    def tearDown(self):
        self.driver.quit()

    def test_create_tuwen_ad_position(self):
        now = time.strftime("%Y%m%d%H%M%S")
        self.adposition_oage = self.main_page.click_ad_position_btn()
