#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 10:36
# @Author  : huanghe
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
import unittest

from src.test.suit.aquapaasADV.login_page import LoginPage
from src.utils.browser import Browser
from src.utils.config import Config


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().get_browserdriver()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.url = Config().get('URL')
        login_page.visit()
        # time.sleep(10)
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(), text=Config().get('USER'))
        login_page.set_value(element=login_page.rec_passwd_input(), text=Config().get('PASSWORD'))
        login_page.click_login_btn()
        login_page.get_windows_img()


if __name__ == '__main__':
    LoginTest()


