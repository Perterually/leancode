#!/usr/bin/env python
# encoding: utf-8

def is_odd(n):
    return n % 2 == 1
l = range(100)
print(list(filter(is_odd,l)))
