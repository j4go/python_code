# 一些online judge题目python3解法

n = int(input())
lst = [int(i) for i in input().split()]

lst = sorted(list(set(lst)))

if len(lst) >= 3:
    print(lst[2])
else:
    print(-1)
