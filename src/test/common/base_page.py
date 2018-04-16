#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 14:38
# @Author  : huanghe
# @Site    : 
# @File    : base_page.py
# @Software: PyCharm
import time
from selenium.common.exceptions import NoSuchElementException
from src.utils.log import Logger

class Basepage(object):
    url = None
    ''''
    定义一个基类，封装常用的页面方法
    '''
    def __init__(self,driver):
        self.driver = driver
        self.classname = self.__class__.__name__

    #浏览器最大化
    def max_browser(self):
        self.driver.maximize_window()

    #设置浏览器的宽,高
    def set_width(self,width,height):
        self.driver.set_window_size(width,height)

    #关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    #浏览器前进
    def forward(self):
        self.driver.forward()

    #浏览器后退
    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)

    # 关闭当前窗口
    def close(self):
        try:
            self.driver.close()
        except NameError as e:
            print('Failed to close')

    def visit(self):
        self.driver.get(self.url)


    # 保存图片
    def get_windows_img(self):
        file_path = r'D:/python/Daemon_/report/screenpicture/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            self.logger.info("Had take screenshot and save to folder : /screenshots")
            print(screen_name)
        except NameError as e:
            self.logger.error("Failed to take screenpicture! {}".format(e))
            self.get_windows_img()

    # 定位元素方法
    def find_element(self,selector):
        self.logger = Logger(loggername=self.classname).get_logger()
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                self.logger.info("Had find the element {}successful "
                            "by {} via value: {} ".format(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                self.logger.error("NoSuchElementException: {}".format(e))
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                self.logger.info("Had find the element {} successful "
                            "by {} via value: {} ".format(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                self.logger.error("NoSuchElementException: {}".format(e))
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 文本框输入
    def set_value(self,element,text):
        self.logger = Logger(loggername=self.classname).get_logger()
        element.clear()
        try:
            element.send_keys(text)
            self.logger.info("Had type {} in inputBox".format(text))
        except NameError as e:
            self.logger.error("Failed to type in input box with {}".format(e))
            self.get_windows_img()

    # 文本框清除
    def clear(self,selector):
        self.logger = Logger(loggername=self.classname).get_logger()
        el = self.find_element(selector)
        try:
            el.clear()
            self.logger.info("Clear text in input box before typing.")
        except NameError as e:
            self.logger.error("Failed to clear in input box with {}".format(e))
            self.get_windows_img()

    # 点击元素
    def click_sel(self, selector):
        self.logger = Logger(loggername=self.classname).get_logger()
        el = self.find_element(selector)
        try:
            self.logger.info("The element {} was clicked." .format(el.text))
            el.click()
        except NameError as e:
            self.logger.error("Failed to click the element with {}".format(e))

    # 获取网页标题
    def get_page_title(self):
        self.logger = Logger(loggername=self.classname).get_logger()
        self.logger.info("Current page title is {}".format(self.driver.title))
        return self.driver.title

    #sleep
    def sleep(self,seconds):
        self.logger = Logger(loggername=self.classname).get_logger()
        time.sleep(seconds)
        self.logger.info("Sleep for {} seconds" .format(seconds))

    #
    def switch_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()

    #frame切换
    def switch_frame(self,elem):
        pass

