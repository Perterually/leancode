#!/usr/bin/env python3
# encoding: utf-8


import functools


#偏函数
def par_int(n,b):
    return int(n,b)
a = par_int('101010101',2)
print(a)

#定义好的偏函数方法
int1 = functools.partial(int,base=2)
print(int1('11010101'))
print(int1('11101010',base=10))
