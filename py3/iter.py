#!/usr/bin/env python3
# encoding: utf-8
it = iter([x * 1 for x in range(1000)])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

