#!/usr/bin/env python
#-*- coding:utf-8 -*-
#FileName:装饰器
#CreateDate: 2016/6/17 14:32

def auth_decorate(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

def multi_decorator(before_func, after_func):
    def wrapper(main_func):
        def inter(*args, **kwargs):
            before_func()
            main_func(*args, **kwargs)
            after_func()
        return inter
    return wrapper

@auth_decorate
def home(name):
    print("Welcome %s to my site!!!!" % name)
    return "page return"


home("eric")