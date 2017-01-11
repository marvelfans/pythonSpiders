# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import json

import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

class SELENIUM:
    __url = ''
    __driver = ''

    # 构造函数 获取网页源代码
    def __init__(self, url):
        self.__url = url
        self.__driver = webdriver.PhantomJS(executable_path="/data/zhaojingzhen/tools/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
        self.__driver.get(self.__url)
        time.sleep(1)

        # 浏览网页HTML代码
        # print self.__driver.page_source
        # sys.exit(1)
    
    # 通过xpath获取指定文本
    def getText(self, xpath):
        text = self.__driver.find_elements_by_xpath(xpath)[0].text.strip().encode('utf-8')
        return text

    # 对指定xpath的按钮进行一次点击
    # 通过xpath对指定按钮进行一次点击
    def buttonClick(self, xpath):
        button = self.__driver.find_elements_by_xpath(xpath)
        button[0].click() 
        time.sleep(1)

    # 根据xpath获取指定内容
    def getContentByXpath(self, xpath):
        element = self.__driver.find_elements_by_xpath(xpath)
        return element 
