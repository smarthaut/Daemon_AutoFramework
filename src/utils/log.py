#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 14:51
# @Author  : huanghe
# @Site    : 
# @File    : log.py
# @Software: PyCharm
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from src.utils.config import Config
from src.utils.config import LOG_PATH


class Logger(object):

    def __init__(self,loggername):
        self.logger = logging.getLogger(loggername)
        logging.root.setLevel(logging.NOTSET)
        c = Config().get('log')
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test.log'  # 日志文件
        self.backup_count = c.get('backup') if c and c.get('backup') else 5  # 保留的日志数量
        # 日志输出级别
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        # 日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        我们这里添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
        两个句柄的日志级别不同，在配置文件中可设置。
        """
        if  not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

if __name__ == '__main__':

    logger = Logger(loggername='he').get_logger()
    logger.info('info message')
    logger.debug('debug message')
    logger.critical('ce message')
    logger.error('error meaagse')
