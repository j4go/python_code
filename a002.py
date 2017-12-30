# -*- coding: utf-8 -*-

# 单向链表
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


L = Node("a", Node("b", Node("c", Node("d"))))


print(L.next.next.value)


# 传统的列表是列表的意思 python的list是数组的概念

# 数组访问某个索引值 快 直接定位内存
# 链表需要遍历这个

# insert 链表直接插入 效率最高
# 数组要挪动，动态数组