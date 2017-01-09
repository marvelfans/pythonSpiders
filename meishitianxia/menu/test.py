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
def ClickMore(mySelenium):
    while True:
        more_button_xpath = ".//*[@id='recipeindex_living_loading']/a"
        more_button_text = mySelenium.getText(more_button_xpath)

        if more_button_text == '没有了~':
            break;
        elif more_button_text == '查看更多':
            mySelenium.buttonClick(more_button_xpath)
            # 菜单的数量
            xpath = ".//*[@id='recipeindex_living']/ul[1]//li"
            menu_block = mySelenium.getContentByXpath(xpath)
            print ("more_button:<%s>  number:<%d>" %(more_button_text, len(menu_block)))

    # 搞不懂python是传值还是传引用, 暂且这么处理
    return mySelenium

# 获取当前标签页的所有url
def getUrl(mySelenium, tagPos):
    xpath = ".//*[@id='recipeindex_living']/ul[" + str(tagPos + 1) + "]//li/a[1]"
    urls = mySelenium.getContentByXpath(xpath)

    for url in urls:
        print "--->   "  +  url.getattr('href')

    return mySelenium

# 获取所有的url
def getMenuUrl(url):
    # 创建对象
    mySelenium = SELENIUM.SELENIUM(url)
    #
    for ind in range(0, 10):
        # 点击导航
        xpath = ".//*[@id='recipeindex_info_wrap']/div/div/h3[" + str(ind + 1) + "]/a"
        mySelenium.buttonClick(xpath)
        # 点击更多
        mySelenium = ClickMore(mySelenium)
        # 抓取当前标签页url


#######################################################################
if __name__ == "__main__":
    url = 'http://home.meishichina.com/recipe.html'

    mySelenium = SELENIUM.SELENIUM(url) 
    getUrl(mySelenium, 1)
