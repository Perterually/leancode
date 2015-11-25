#!/usr/bin/env python
# encoding: utf-8

def fib(max):
    n, a, b = 0, 0, 1
    while n < max :
        a, b = b, a + b
        n = n + 1
        print(b)
print(fib(6))

