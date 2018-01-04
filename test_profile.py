# coding: utf-8
"""A simple profile test."""

from random import randint
from time import perf_counter as pc
import cProfile
import pstats


def insertion_sort(data):
    """从列表data取出数据，有顺序地插入新的列表并返回"""
    result = []
    for value in data:
        insert_value(result, value)
    return result




def insert_value(array, value):
    """按照从小到大插入array"""
    for i, d in enumerate(array):
        if d > value:
            array.insert(i, value)
            return
    # array中没有元素比value大，插到最后
    array.append(value)

# 优化
# from bisect import bisect_left
# def insert_value(array, value):
#     i = bisect_left(array, value)
#     array.insert(i, value)

# 随机生成data
MAX_SIZE = 10 ** 5
data = [randint(0, MAX_SIZE) for _ in range(MAX_SIZE)]

# 用来被测试的函数
test = lambda: insertion_sort(data)

# 直接运行 time|python -m cProfile + filename.py
# test()

# 利用Python3 time.perf_counter来输出程序运行时间
# t = pc()
# test()
# print(pc() - t)

# 用cProfile进行性能分析
cProfile.run('test()')

"""
ncalls：函数运行次数

tottime： 函数的总的运行时间，减去函数中调用子函数的运行时间

第一个percall：percall = tottime / nclalls

cumtime:函数及其所有子函数调整的运行时间，也就是函数开始调用到结束的时间。

第二个percall：percall = cumtime / nclalls
"""

# cProfile配合pstats使用
# cProfile.run('test()', 'profile_with_pstats')  # 为profile取名
# p = pstats.Stats('profile_with_pstats')
# p.strip_dirs().sort_stats(-1).print_stats()
# strip_dirs() 移除模块名之前的路径信息
# sort_stats(-1) 按filename:lineno(function)排序

# 按time排序并显示前10行
# p.sort_stats('time').print_stats(10)

#先按time排序再按cum排序，只输出50%
# p.sort_stats('time', 'cumtime').print_stats(.5)














