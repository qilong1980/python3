#!/usr/bin/env python
#-*- coding:utf-8 -*-
#FileName:平均两个数列
#CreateDate: 2016/6/15 17:01
"""
有两个序列a,b,大小都为N,序列元素的值为任意整数,无序;
要求:通过交换a,b中的元素,使序列a与b的元素中之间的差值最小
a = [7058, 4720, 9419, 9979, 4069, 3191, 3158, 3958, 3870, 1967]
b = [4242, 7299, 6784, 1170, 3650, 1886, 626, 3923, 4168, 8938]
解:
1,将两个序列合并为一个序列,并排序.为序列new
2,拿出最大元素Big,次大元素Small
3,在余下的序列new[:-2]进行评分,得到序列max,min
4,将Small加到max序列,Big加到min序列,重新进行计算新序列和,和大的为max,和小的为min


"""
def mean(sorted_list):
    if not sorted_list:
        return (([],[]))
    big = sorted_list[-1]
    small = sorted_list[-2]
    big_list, small_list = mean(sorted_list[:-2])
    big_list.append(small)
    small_list.append(big)
    big_list_sum = sum(big_list)
    small_list_sum = sum(small_list)
    if big_list_sum > small_list_sum:
        return ((big_list,small_list))
    else:
        return ((small_list,big_list))


if __name__ == "__main__":
    a = [7058, 4720, 9419, 9979, 4069, 3191, 3158, 3958, 3870, 1967]
    b = [4242, 7299, 6784, 1170, 3650, 1886, 626, 3923, 4168, 8938]
    new = a + b
    print("a序列为:%s" % a)
    print("b序列为:%s" % b)
    new.sort()
    a ,b = mean(new)
    print("交换后.")
    print("a序列为:%s" % a)
    print("b序列为:%s" % b)
    minus = sum(a) - sum(b)
    print("两序列差为:%d" % minus)