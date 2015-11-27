#!/usr/bin/env python3
# encoding: utf-8


' a test module '

__anthor__ = 'Sky Blue'

import sys


def test():
    args = sys.argv
    if len(args)==1:
        print('hello, world!')
    elif len(args)==2:
        print('hello, %s!' & args[1])
    else:
        print('Too mant aruments!')
if __name__=='__main__':
    test()




