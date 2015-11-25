#!/usr/bin/env python
# encoding: utf-8

def clac_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(clac_sum(1,9))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
             ax = ax + n
             return ax

f = lazy_sum(1,2,3,4,5)

