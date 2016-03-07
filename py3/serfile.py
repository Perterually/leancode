#-*- coding:utf-8 -*-
import os

def search(name,path):
   for dir, dirname, filename in os.walk(path):
        for f in filename:
            if name in f:
                print(f)
search('ubu','/Users/perterually/Downloads')