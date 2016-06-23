#!/usr/bin/env python
#-*- coding:utf-8 -*-

l =[11,33,22,55,77,10,30]
print(l)
print("-"*30)
num=0
for i in range(1,len(l)-1):
    for j in range(len(l)-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        # print(l)
        num +=1
    # print("*"*30)
# print("-"*30)
print(l)
print("循环了%d次"%num)