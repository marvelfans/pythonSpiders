# -*- coding:utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

# 导入自己的类
import MSCHINA
import REDIS
import FILE
import SELENIUM
#######################################################################
# 点击更多，让所有的url暴漏出来
def ClickMore(mySelenium, ind):
    while True:
        more_button_xpath = ".//*[@id='recipeindex_living_loading']/a"
        more_button_text = mySelenium.getText(more_button_xpath)

        if more_button_text == '没有了~':
            break;
        elif more_button_text == '查看更多':
            mySelenium.buttonClick(more_button_xpath)
            # 菜单的数量
            xpath = ".//*[@id='recipeindex_living']/ul[" + str(ind) + "]//li"
            menu_block = mySelenium.getContentByXpath(xpath)
            print ("more_button:<%s>  number:<%d>" %(more_button_text, len(menu_block)))

    # 搞不懂python是传值还是传引用, 暂且这么处理
    # return mySelenium

# 获取当前标签页的所有url
def getUrl(mySelenium, tagPos):
    xpath = ".//*[@id='recipeindex_living']/ul[" + str(tagPos) + "]//li/a[1]"
    urls = mySelenium.getContentByXpath(xpath)

    # Redis对象
    redis_service = REDIS.REDIS()
    redis_service.ConnectRedis()

    for url in urls:
        # 从webElement对象中获取属性
        _url = url.get_attribute('href')
        # 将url放入redis
        if _url != '':
            redis_service.sadd('menu_url_1', _url)         
            print ("redis_url_num:<%d> now_url:<%s>" %(redis_service.scard('menu_url_1'), _url))

    # return mySelenium

# 获取所有的url
def getMenuUrl(url, ind):
    # 创建对象
    mySelenium = SELENIUM.SELENIUM(url)
    #
    # 点击导航
    xpath = ".//*[@id='recipeindex_info_wrap']/div/div/h3[" + str(ind) + "]/a"
    mySelenium.buttonClick(xpath)
    # 点击更多
    ClickMore(mySelenium, ind)
    # 抓取当前标签页url
    getUrl(mySelenium, ind)

#######################################################################
if __name__ == "__main__":

    url = 'http://home.meishichina.com/recipe.html'

    if len(sys.argv) != 2:
        print ("python producer.py number[ 1 <= number <= 10 ]")
        sys.exit(1)

    getMenuUrl(url, sys.argv[1])
    sys.exit(1)
