# -*- coding:utf-8 -*-

import os

# 
from lxml import etree

# 中文
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
###### 引入自己的文件
sys.path.append("../libs/")
import REDIS
import FILE
import MSCHINA
import SELENIUM

#######################################################################################################################################
# 批量抓取时候，放倒redis里边
def getUrls():

    mschina = MSCHINA.MSCHINA()

    base = 'http://home.meishichina.com/'

    page_num = 1
    while True:
        if page_num > 1500:
            sys.exit(-1)
        if page_num == 1:
            url = base + 'pai.html'
            print ("now_page:<%d>   html_page:<%d>  page_url:<%s>" %(1, 1, str(url)))
            page_num += 1
            continue
        
        url = base + 'pai-index-page-' + str(page_num) + '.html'
        html_code = mschina.getCodeByBaseUrl(url)
        xpath = 'body/div[5]/div/div[1]/div[3]/div//a[@class="now_page"]/text()'
        res = mschina.getResByXpathExpr(html_code, xpath)
        # 如果当前页不再发生变化，证明已经达到最大的页码，停止
        if int(res[0]) != page_num:
            break;

        print ("now_page:<%d>   html_page:<%d>  page_url:<%s>" %(page_num, int(res[0]), str(url)))
        page_num += 1


# 批量抓取时候，从redis里边获取
def getContent():

    mschina = MSCHINA.MSCHINA()

    f = open('./topic_url', 'r')
    for line in f:
        url = line.strip()
        html_code = mschina.getCodeByBaseUrl(url)
        # print etree.tostring(html_code)
        for li_tag in range(1, 11):
            # 名字
            xpath = './/*[@id=\'J_list\']/ul/li[' + str(li_tag) + ']/div[1]/div[1]/a[1]/text()'
            li_code = mschina.getResByXpathExpr(html_code, xpath)
            print li_code[0]
            # 话题
            xpath = './/*[@id=\'J_list\']/ul/li[' + str(li_tag) + ']/div[2]/div[1]/a[1]/text()'
            a_code = mschina.getResByXpathExpr(html_code, xpath)
            print a_code[0]
            # 话题url
            xpath = './/*[@id=\'J_list\']/ul/li[' + str(li_tag) + ']/div[2]/a[1]/@href'
            href_code = mschina.getResByXpathExpr(html_code, xpath)
            if len(href_code) > 0:
                print href_code[0]
            # 分隔符
            print '+' * 100
        # 先抓一页做个实验
        break;

    f.close()

#######################################################################################################################################
if __name__ == "__main__":
    cmd_len = len(sys.argv)
    if cmd_len < 2:
        print ("Error, parameter number error!")
        print ("python spider.py [url | content]")
        sys.exit(1)

    if sys.argv[1] == 'url':
        getUrls()
    elif sys.argv[1] == 'content':
        getContent()
    else:
        print ("Error, parameter error!")
        print ("python spider.py [url | content]")

