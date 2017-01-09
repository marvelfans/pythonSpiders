# import urllib
# _*_ coding:utf-8
# import re
import urllib2
from lxml import etree


import sys
reload(sys)
sys.setdefaultencoding("utf-8")



# 抓取地址
url = 'http://www.meishichina.com/'
# 代理
user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0"
headers = {'User-Agent' : user_agent}

try:
    # 获取网页源代码
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    html = etree.HTML(content);

    # xpath解析 获取标签导航
    # result_gps = html.xpath('body/div[2]/div[3]/a/@href')
    # gps_url = open('gps_url', 'w+')
    # for _url in result_gps:
    #     gps_url.write(_url)
    #     gps_url.write("\n")
    # gps_url.close()

    # xpath 解析 获取循环导航栏数据
    # 获取href
    # result_cir_h = html.xpath('body/div[3]/div/div[2]//a/@href')
    # cir_url = open('cir_url', 'w+')
    # for _url in result_cir_h:
    #     cir_url.write(_url)
    #     cir_url.write("\n")
    # cir_url.close()
    # 获取标题
    # result_cir_t = html.xpath('body/div[3]/div/div[2]//a/text()')
    # title = []
    # for _t in result_cir_t:
    #     title.append(_t.strip('\n'))
    # # 获取内容
    # result_cir_p = html.xpath('body/div[3]/div/div[2]//p/text()')
    # plain_t = []
    # for _t in result_cir_p:
    #     plain_t.append(_t.strip('\n'))
    # # 获取**的菜单
    # result_cir_s = html.xpath('body/div[3]/div/div[2]//span/text()')
    # seller = []
    # for _t in result_cir_s:
    #     seller.append(_t.strip('\n'))
    # # 去掉空串
    # plain = []
    # _len = len(plain_t)
    # for _i in range(0, _len):
    #     if plain_t[_i].strip() != '':
    #         plain.append(plain_t[_i])
    # # 存入文件
    # cir_content = open('cir_content', 'w+')
    # _len = len(title)
    # for _ind in range(0, _len):
    #     cir_content.write(title[_ind] + "\t")
    #     cir_content.write(seller[_ind] + "\t")
    #     cir_content.write(plain[_ind] + "\n")
    # cir_content.close()
    # 健康 烘焙 收藏
    result_html = html.xpath('body/div[3]/div/div[3]//div/div[2]/ul//li/a/@href')
    health_bake_coll_url = open('health_bake_coll_url', 'w+')
    for _url in result_html:
        health_bake_coll_url.write(_url.strip('\n'.lstrip()))
        health_bake_coll_url.write('\n')
    health_bake_coll_url.close()

    # 新秀菜谱 一周热门 最受欢迎的家常菜
    # result_J = html.xpath('body/div[3]/div/div[4]/div[2]//ul//li/a[1]/@href')
    # menu_url = open('menu_url', 'w+')
    # for _url in result_J:
    #     menu_url.write(_url.strip('\n').lstrip())
    #     menu_url.write('\n')
    # menu_url.close()




except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
