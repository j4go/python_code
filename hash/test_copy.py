# coding: utf-8

a = [1, 2, ['a', 'b']]

# 测试赋值 赋值是引用
# b = a
# a.append('test1')
# print a, b

# 测试浅拷贝  切片和copy.copy
# 浅拷贝只拷贝父对象，不会拷贝对象的内部的子对象
# 深拷贝 拷贝对象及其子对象
c = a[:]
from copy import copy, deepcopy
d = copy(a)
e = deepcopy(a)
a.append('test2')
a[2].append('test3')
print 'a: ', a
print 'c: ', c
print 'd: ', d
print 'e: ', e
print deepcopy()

import urllib

# 深度拷贝中有两个相同的对象时
a = [1, 2]
b = [a, a]
c = deepcopy(b)

print b is c
print b[0] is b[1]
print c[0] is c[1]
print id(b[0]), id(c[0])


# 特别要注意的是 不可变的数、字符串、元组等没有拷贝的概念
# 此时 obj is copy.deepcopy(obj)
