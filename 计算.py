#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
test_str = "(1+(40-3*5))-4*5*((30+30)/2)*4"

re_str = re.compile("[^(]+?\)")
print(re_str.search(test_str))
test1 = re_str.search(test_str)
print(test1.group().strip(")"))
test2 = test1.group().strip(")")
print(re.split("[-+/*]",test2))
print(re.split("[0-9]+",test2))
