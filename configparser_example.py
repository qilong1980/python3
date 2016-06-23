#!/usr/bin/env python
#-*- coding:utf-8 -*-
#FileName:configparser_example
#CreateDate: 2016/6/21 15:08
import configparser

conf = configparser.ConfigParser()
conf.read('mysite.conf')

#遍历conf文件
secs = conf.sections()
# print(secs)
for sec in secs:
    print("[%s]" %sec)
    for opt in conf.options(sec):
        test = conf.get(sec, opt)
        print("%s = %s" % (opt, test))
    # print("\n")
for i in conf.items():
    print("[%s]" % i[0])
    for j in conf.items(i[0]):
        print("%s = %s" % (j[0], j[1]))

#增加,修改section

if conf.has_section("add"):         #判断section是否存在,不存在则增加
    print("add section已经存在!")
else:
    conf.add_section("add")         #增加add这个section
    conf.set("add","name","测试")  #增加add下面的值
    conf.set("add","人数", "10")

if conf.has_option("nginx", 'port'):    #判断nginx下如果有port则修改或删除
    conf.set("nginx", "port", "88") #修改nginx下的port值为88
#    conf.remove_option("nginx", "port") #删除option

conf.remove_option("nginx", 'process') #删除nginx下的process项
conf.remove_section("nginx")            #删除nginx这个section
conf.write(open("new.conf","w",encoding="utf8"))