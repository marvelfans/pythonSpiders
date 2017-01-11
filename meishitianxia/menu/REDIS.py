# -*- coding:utf-8 -*-
import redis

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class REDIS:

    __redis = ''
    # 连接redis 默认参数
    def ConnectRedis(self, host='localhost', port=6379, db=0):
        self.__redis = redis.Redis(host='localhost', port=6379, db=0)
    # set
    def set(self, key, value):
        self.__redis.set(key, value)
    # get
    def get(self, key):
        return self.__redis.get(key)
    # sadd 集合
    def sadd(self, myset, value):
        return self.__redis.sadd(myset, value)
    # spop 集合
    def spop(self, myset):
        return self.__redis.spop(myset)
    # scard 集合中value的数目
    def scard(self, myset):
        return self.__redis.scard(myset)
    # flushall 清空redis
    def flushall(self):
        return self.__redis.flushall()
