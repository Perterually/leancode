#!/usr/bin/env python
# encoding: utf-8

def test_args(*args):
    print(args)
print(test_args('admin','admin'))

def test_args2(**args):
    print(args)
print(test_args2(a='admin'))
