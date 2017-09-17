# -*- coding: utf-8 -*-

# print("hello world")

def insertion_sort1(list):
    for i in range(len(list)-1):
        j = i + 1
        k = j - 1
        while(k >= 0 and list[j] < list[k]):
            tmp = list[j]
            list[j] = list[k]
            list[k] = tmp
            j = k
            k -= 1

def insertion_sort2(list):
    for i in range(1, len(list)):
        j = i - 1 # 排好序的最后一个下标
        while(j >= 0 and list[i] < list[j]):
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp
            i = j
            j -= 1

def insertion_sort3(list):
    for i in range(1, len(list)):
        j = i - 1 # 排好序的最后一个下标
        while(j >= 0 and list[i] < list[j]):
            list[i], list[j] = list[j], list[i]
            i = j
            j -= 1

def insertion_sort4(list):
    for i in range(1, len(list)):
        j = i - 1 # 排好序的最后一个下标
        while(j >= 0):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
                i = j
                j -= 1
            else:
                break # 前面已经是排好序的了


def insertion_sort5(list):
    for i in range(1, len(list)):
        value = list[i] # 用来比较的值
        j = i - 1 # 排好序的最后一个下标
        while(j >= 0):
            if value < list[j]:
                list[j+1] = list[j] # value小就插入到与之比较的前面 即交换
                list[j] = value
                j -= 1
            else:
                break

def insertion_sort6(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while(j >= 0):
            if value < list[j]:
                list[j+1], list[j] = list[j], value
                j -= 1
            else:
                break

# 最终版 插入排序 稳定
def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while(j >= 0 and value < list[j]):
            list[j+1], list[j] = list[j], value
            j -= 1

# 最终版 快排
def quick_sort(arr, i, j):
    pivot_index = quick_sort_helper(arr, i, j)
    if i < pivot_index:
        quick_sort(arr, i, pivot_index-1)
    elif pivot_index < j:
        quick_sort(arr, pivot_index+1, j)

def quick_sort_helper(arr, i, j):
    pivot_value = arr[i]
    while i < j:
        if arr[j] >= pivot_value:
            j -= 1
        else:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = pivot_value
    return i



# def quick_sort(arr, i, j):
#     #递归停止条件是i=j
#     pivot_index = quick_sort_helper(arr, i, j) # 处理完一趟快排后基准值所在的下标
#     if i < pivot_index:
#         quick_sort(arr, i, pivot_index-1)
#     elif pivot_index < j:
#         quick_sort(arr, pivot_index+1, j)
#
# # 处理一趟快排的过程 返回pivot下标
# def quick_sort_helper(arr, i, j):
#     pivot_value = arr[i] #取第一个为对比的基准值
#     while i < j: # i=j 表示处理完
#         # j 作为活动指针来比较
#         if arr[j] >= pivot_value: # arr[j]大于pivot_value，不作处理 j--
#             j -= 1
#         else: # arr[j]小，j值放到i i+1值放到j
#             arr[i] = arr[j]
#             i += 1
#             arr[j] = arr[i]
#     # 得到i=j 此下标存放基准值pivot_value
#     arr[i] = pivot_value
#     return i

# a = [7, 4, 1, 3, 6, 2, 5]
# a = [5,5,4,3,2,2,1]
a = [1, 2, 2, 3, 4, 5, 5]
quick_sort(a, 0, len(a)-1)
print(a)