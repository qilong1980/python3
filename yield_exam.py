#!/usr/bin/env python
#-*- coding:utf-8 -*-
#FileName:yield_exam

def mrange(arg):
    seed = 0
    while True:
        if seed >= arg:
            return
        else:
            yield seed
        seed +=1

for i in mrange(10):
    print(i)
