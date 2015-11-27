#!/usr/bin/env python
# encoding: utf-8

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
a = calc_sum(1,2,3)
print(a)
