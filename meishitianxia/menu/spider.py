#coding: utf-8

from scrapy.spiders import Spider  
from scrapy.http import Request
import sys
import re
import urllib2
from selenium import webdriver
import time
import json

reload(sys)
sys.setdefaultencoding('utf-8')

class WinescoreSpider(Spider):  
    name = "award"  
    allowed_domains = [
	"wine-world.com", 
	"mall.wine-world.com"
    ]  

    fp = open("url_list")
    start_urls = [line.strip() + "/hj" for line in fp.readlines()]
    #start_urls = ["http://www.wine-world.com/winery/chateau-lafite-rothschild/ad679838-5304-4973-be95-0162fa5d2d7c/hj"]
    
    def parse(self, response):
            url = response.url
            driver = webdriver.PhantomJS(executable_path="/data/rd/liucan/tools/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
            driver.get(url)
            time.sleep(1)

            curr_page = driver.find_elements_by_xpath('//div[@class="pages"]/span[@class="current"][text()]')
            data_list = []
            self.score_parse(driver, data_list)
            while True:
                next_page = driver.find_elements_by_xpath('//div[@class="pages"]/a[text()="下一页"]')
                if len(next_page) == 0:
                        break
                else:
                    next_page[0].click()
                    time.sleep(1)
                    self.score_parse(driver, data_list)
            
            if len(data_list) != 0:
                url_list = response.url.split("/")
                filename = url_list[-3] + "---" + url_list[-2]
                open("huojiang/" + filename, "w").write(json.dumps(data_list).decode('unicode_escape'))
            
    def score_parse(self, driver, data_list):
            contents = driver.find_elements_by_xpath('//div[@id="content"]/table/tbody/tr')
            for content in contents:
                    info = {}
                   
                   #葡萄酒年份
                    wine_year = content.find_elements_by_xpath('./td[1][text()]')[0].text.strip().encode('utf-8')
                    info['wine_year'] = wine_year
                    
                    #颁奖组织
                    orgnization = content.find_elements_by_xpath('./td[2][text()]')[0].text.strip().encode('utf-8')
                    info['orgnization'] = orgnization

                    #获奖时间
                    award_year = content.find_elements_by_xpath('./td[3][text()]')[0].text.strip().encode('utf-8')
                    info['award_year'] = award_year
                    
                    #奖级
                    level = content.find_elements_by_xpath('./td[4][text()]')[0].text.strip().encode('utf-8')
                    info['level'] = level
                    data_list.append(info)

    def get_contents(self, url):
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            contents =  response.read().decode('utf-8')
            return contents

    def page_parse(self, response):
            pass


