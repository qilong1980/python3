#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
s = u'这是一段汉字。'
ss = u"11820: ['Server.exe', 错误警告]"

print('s',s)
print ss.decode("utf8").encode("gbk"),'python'

