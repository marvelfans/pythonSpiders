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
def Click():
    a = ''

def getMenuUrl():
    a = ''

def getMenuContent():
    a = ''

def getAllMenuContent():
    a = ''

#######################################################################
if __name__ == "__main__":
    url = 'http://home.meishichina.com/recipe.html'

    # while True:
    #     more_button_text = driver.find_elements_by_xpath(".//*[@id='recipeindex_living_loading']/a")[0].text.strip().encode('utf-8')
    #     more_button = driver.find_elements_by_xpath(".//*[@id='recipeindex_living_loading']/a")

    #     if more_button_text == '没有了~':
    #         break;
    #     else:
    #         more_button[0].click()
    #         time.sleep(1)

    #     # 菜单的数量
    #     menu_block = driver.find_elements_by_xpath(".//*[@id='recipeindex_living']/ul[1]//li")
    #     print ("more_button:<%s>  number:<%d>" %(more_button_text, len(menu_block)))


    mySelenium = SELENIUM.SELENIUM(url)
    while True:
        more_button_xpath = ".//*[@id='recipeindex_living_loading']/a"
        more_button_text = mySelenium.getText(more_button_xpath)

        if more_button_text == '没有了~':
            break;
        else:
            mySelenium.buttonClick(more_button_xpath)
            # 菜单的数量
            xpath = ".//*[@id='recipeindex_living']/ul[1]//li"
            menu_block = mySelenium.getContentByXpath(xpath)
            print ("more_button:<%s>  number:<%d>" %(more_button_text, len(menu_block)))
