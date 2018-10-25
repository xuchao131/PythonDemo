#-*- coding:UTF-8 -*-
'''
Created on 2018年10月23日

@author: bingw
'''
from enum import unique, Enum

#@unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6