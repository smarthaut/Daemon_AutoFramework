#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 10:46
# @Author  : huanghe
# @Site    : 
# @File    : browser.py
# @Software: PyCharm
import os
from selenium.webdriver.ie.webdriver import WebDriver as IeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

_DRIVERS = {
    'ie': [IeWebDriver, 'IEDriverServer.exe'],
    'firefox': [FirefoxWebDriver],
    # 'remote': RemoteWebDriver,
    'chrome': [ChromeWebDriver, 'chromedriver.exe'],
    # 'phantomjs': PhantomJSWebDriver,
}


def Browser(driver_name='firefox', *args, **kwargs):
    driver = _DRIVERS[driver_name]
    if driver_name != 'firefox':
        CURRENT_DIR = os.path.dirname(__file__)
        executable_path = os.path.abspath(os.path.join(CURRENT_DIR , r'drivers', driver[1]))
        return driver[0](executable_path=executable_path, *args, **kwargs)
    return driver[0](*args, **kwargs)

