#!/usr/bin/env python
# encoding: utf-8

def f(x,y):
    return x * y
r = reduce(f,[1,2,3,4,5,6,7,8])
print(r)
