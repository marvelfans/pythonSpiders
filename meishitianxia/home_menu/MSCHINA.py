# -*- coding:utf-8 -*-
#import urllib
#import re
import urllib2
from lxml import etree
#################################
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class MSCHINA:

    __url = ''
    __user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0"
    __headers = {'user-agent' : __user_agent}

    # 根据url获取可供xpath解析的源代码
    def getCodeByBaseUrl(self, url):
        self.__url = url
        try:
            # 获取网页源代码
            request = urllib2.Request(self.__url, headers = self.__headers)
            response = urllib2.urlopen(request)
            content = response.read()
            html = etree.HTML(content);
            return html
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
        #
        return ''

    # 根据xpath表达式和源代码获取解析结果，返回数组
    def getResByXpathExpr(self, html, expr):
        try:
            result = html.xpath(expr)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
        return result
