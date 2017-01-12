# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class FILE:

    __output = ''


    def __init__(self, file_path, mode = 'a+'):
        self.__output = open(file_path, mode)
        return
    # 打开文件，默认追加方式打开
    def openFile(self, file_path, mode = 'a+'):
        self.__output = open(file_path, mode)
        return
    # 将字符串输出到文件
    def writeFile(self, aString):
        self.__output.write(aString)
    # 关闭文件
    def closeFile(self):
        self.__output.close()
