# coding: utf-8
# 网易2017春招笔试真题编程题集合--Python

"""
http://blog.csdn.net/zy_dream/article/details/73457948

1.

一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，
假设已知CPU的每个核1秒可以处理1kb，每个核同时只能处理一项任务。
n个任务可以按照任意顺序放入CPU进行处理，现在需要设计一个方案让CPU处理完这批任务所需的时间最少，
求这个最小的时间。

输入描述:
输入包括两行：
第一行为整数n(1 ≤ n ≤ 50)
第二行为n个整数length[i](1024 ≤ length[i] ≤ 4194304)，
表示每个任务的长度为length[i]kb，每个数均为1024的倍数。


输出描述:
输出一个整数，表示最少需要处理的时间

输入例子:
5
3072 3072 7168 3072 1024

输出例子:
9216



# python3实现

n = int(input())
lst = [int(i) for i in input().split()]

tasksets = set(lst) # 不同的任务组合之和的集合

# 找出所有不同任务组合之和
for i in lst:
    for j in list(tasksets): # 对每个i 把当前的tasksets生成列表用来遍历
        tasksets.add(i + j) # 针对每个i 计算包含任务i的不同组合

# 拿到所有不同任务组合之和 时间大于 sum(lst)/2 的都是可能解，取最小值

half_sum = sum(lst) / 2

results = [i for i in tasksets if i >= half_sum]

# print(n)
# print(lst)
print(min(results))



# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例


2.

终于到周末啦！小易走在市区的街道上准备找朋友聚会，突然服务器发来警报,小易需要立即回公司修复这个紧急bug。
假设市区是一个无限大的区域，每条街道假设坐标是(X，Y)，小易当前在(0，0)街道，办公室在(gx,gy)街道上。
小易周围有多个出租车打车点，小易赶去办公室有两种选择，一种就是走路去公司，另外一种就是走到一个出租车打车点，
然后从打车点的位置坐出租车去公司。每次移动到相邻的街道(横向或者纵向)走路将会花费walkTime时间，
打车将花费taxiTime时间。小易需要尽快赶到公司去，现在小易想知道他最快需要花费多少时间去公司。

输入描述:
输入数据包括五行:
 第一行为周围出租车打车点的个数n(1 ≤ n ≤ 50)
 第二行为每个出租车打车点的横坐标tX[i] (-10000 ≤ tX[i] ≤ 10000)
 第三行为每个出租车打车点的纵坐标tY[i] (-10000 ≤ tY[i] ≤ 10000)
 第四行为办公室坐标gx,gy(-10000 ≤ gx,gy ≤ 10000),以空格分隔
 第五行为走路时间walkTime(1 ≤ walkTime ≤ 1000)和taxiTime(1 ≤ taxiTime ≤ 1000),以空格分隔

输出描述:
输出一个整数表示，小易最快能赶到办公室的时间

输入例子1:
2
-2 -2
0 -2
-4 -2
15 3

输出例子1:
42



# python3 实现

taxi_num = int(input())
taxi_x = [int(i) for i in input().split()]
taxi_y = [int(i) for i in input().split()]
taxi_xy_lst = [[i, j] for i, j in zip(taxi_x, taxi_y)]
company_xy = [int(i) for i in input().split()]
walk_time, taxi_time = [int(i) for i in input().split()]

# print(taxi_xy_lst)
# print(company_xy)


# 原点到xy点 走路消耗时间
def walk_to_xy(xy_lst):
    return (abs(xy_lst[0]) + abs(xy_lst[1])) * walk_time

# x0y0点到x1y1点 打车消耗时间
def taxi_to_xy(x0y0_lst, x1y1_lst):
    return (abs(x1y1_lst[0] - x0y0_lst[0]) + abs(x1y1_lst[1] - x0y0_lst[1])) * taxi_time

# 原点到xy点再到公司 走路+打车消耗时间
def taxi_to_com(taxi_xy, company_xy):
    walk_to_taxi = walk_to_xy(taxi_xy)
    taxi_to_com = taxi_to_xy(taxi_xy, company_xy)
    return walk_to_taxi + taxi_to_com

total_time_lst = [taxi_to_com(i, company_xy) for i in taxi_xy_lst]

total_time_lst.append(walk_to_xy(company_xy))

print(min(total_time_lst))

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例



3.

在幼儿园有n个小朋友排列为一个队伍，从左到右一个挨着一个编号为(0~n-1)。其中有一些是男生，
有一些是女生，男生用'B'表示，女生用'G'表示。小朋友们都很顽皮，当一个男生挨着的是女生的时候就会发生矛盾。
作为幼儿园的老师，你需要让男生挨着女生或者女生挨着男生的情况最少。你只能在原队形上进行调整，
每次调整只能让相邻的两个小朋友交换位置，现在需要尽快完成队伍调整，
你需要计算出最少需要调整多少次可以让上述情况最少。例如：
GGBBG -> GGBGB -> GGGBB
这样就使之前的两处男女相邻变为一处相邻，需要调整队形2次

输入描述:
输入数据包括一个长度为n且只包含G和B的字符串.n不超过50.

输出描述:
输出一个整数，表示最少需要的调整队伍的次数

输入例子:
GGBBG

输出例子:
2

思路：index相差多少就挪动多少步，最终是男女各一半，男在左或女在左，取较小值

# python3 实现

s = input()

s_boy_index_sum = 0 # s中所有G的下标之和
s_girl_index_sum = 0 # s中所有B的下标之和
for i, v in enumerate(s):
    if v == 'B':
        s_boy_index_sum += i
    elif v == 'G':
        s_girl_index_sum += i

boy_num = s.count('B')
girl_num = s.count('G')

# 男左 排序完所有B的下标之和
final_boy_left_index_sum = int(boy_num * (boy_num - 1) / 2)

# 女左 排序完所有B的下标之和
final_girl_left_index_sum = int(girl_num * (girl_num - 1) / 2)

delta_boy = s_boy_index_sum - final_boy_left_index_sum
delta_girl = s_girl_index_sum - final_girl_left_index_sum

# 取较小值
print(min(delta_girl, delta_boy))


# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例



4.

易有一个长度为n序列，小易想移除掉里面的重复元素，但是小易想是对于每种元素保留最后出现的那个。
小易遇到了困难,希望你来帮助他。

输入描述:
输入包括两行：
第一行为序列长度n(1 ≤ n ≤ 50)
第二行为n个数sequence[i](1 ≤ sequence[i] ≤ 1000)，以空格分隔

输出描述:
输出消除重复元素之后的序列，以空格分隔，行末无空格

输入例子:
9
100 100 100 99 99 99 100 100 100

输出例子:
99 100

思路：
用set来去重，翻转列表，把最后出现变成最先出现，结果再翻转回去，用list保存结果保证有序


# python 3 实现

_ = input() # 第一个输入 用不到

lst = [int(i) for i in input().split()]

lst = lst[::-1] # 翻转

tmp_set = set()
result_lst = []

for i in lst:
    if i not in tmp_set:
        tmp_set.add(i)
        result_lst.append(i)

result = ''
for i in result_lst[::-1]:
    result += str(i) + ' '

# 注意结果的格式
print(result[:-1])

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例

# 思路2
# 用set去重 用原来的数组index当做key排序set

_ = input() # 第一个输入 用不到

lst = [int(i) for i in input().split()]

lst.reverse() # 翻转 为了lst.index取到的是翻转前的最后一个下标

lst2 = list(set(lst)) # 去重 但无序

lst2.sort(key=lst.index) # 排序 lst中下标大的在后面

lst2.reverse() # 翻转回去 容易忽略

result = ''
for i in lst2:
    result += str(i) + ' '

# 注意结果的格式
print(result[:-1])

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例


5.

小易拥有一个拥有魔力的手环上面有n个数字(构成一个环),当这个魔力手环每次使用魔力的时候就会
发生一种奇特的变化：每个数字会变成自己跟后面一个数字的和(最后一个数字的后面一个数字是第一个),
一旦某个位置的数字大于等于100就马上对100取模(比如某个位置变为103,就会自动变为3).
现在给出这个魔力手环的构成，请你计算出使用k次魔力之后魔力手环的状态。
输入描述:
输入数据包括两行：
第一行为两个整数n(2 ≤ n ≤ 50)和k(1 ≤ k ≤ 2000000000),以空格分隔
第二行为魔力手环初始的n个数，以空格分隔。范围都在0至99.

输出描述:
输出魔力手环使用k次之后的状态，以空格分隔，行末无空格。

输入例子:
3 2
1 2 3

输出例子:
8 9 7




# python 3

n, k = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]

def magic(lst):
    first = lst[0]
    for i, v in enumerate(lst):
        if i != n - 1:
            lst[i] = v + lst[i + 1]
        else:
            lst[i] = v + first  # 这里的lst[0]是修改之前的值 注意
        if lst[i] >= 100:
            lst[i] = lst[i] % 100
    return lst

while k:
    lst = magic(lst)
    k -= 1

result = ''
for i in lst:
    result += str(i) + ' '

print(result[:-1])

# 您的代码已保存
# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为30.00%运行超时



6.

现在有n位工程师和6项工作(编号为0至5)，现在给出每个人能够胜任的工作序号表(用一个字符串表示，比如：045，表示某位工程师能够胜任0号，4号，5号工作)。现在需要进行工作安排，每位工程师只能被安排到自己能够胜任的工作当中去，两位工程师不能安排到同一项工作当中去。如果两种工作安排中有一个人被安排在的工作序号不一样就被视为不同的工作安排，现在需要计算出有多少种不同工作安排计划。
输入描述:
输入数据有n+1行：
第一行为工程师人数n(1 ≤ n ≤ 6)
接下来的n行，每行一个字符串表示第i(1 ≤ i ≤ n)个人能够胜任的工作(字符串不一定等长的)


输出描述:
输出一个整数，表示有多少种不同的工作安排方案

输入例子:
6
012345
012345
012345
012345
012345
012345

输出例子:
720


7.

小易最近在数学课上学习到了集合的概念,集合有三个特征：1.确定性 2.互异性 3.无序性.
小易的老师给了小易这样一个集合：
S = { p/q | w ≤ p ≤ x, y ≤ q ≤ z }
需要根据给定的w，x，y，z,求出集合中一共有多少个元素。小易才学习了集合还解决不了这个复杂的问题,需要你来帮助他。
输入描述:
输入包括一行：
一共4个整数分别是w(1 ≤ w ≤ x)，x(1 ≤ x ≤ 100)，y(1 ≤ y ≤ z)，z(1 ≤ z ≤ 100).以空格分隔


输出描述:
输出集合中元素的个数

输入例子:
1 10 1 1

输出例子:
10



# python 3

w, x, y, z = [int(i) for i in input().split()]
p_lst = list(range(w, x+1))
q_lst = list(range(y, z+1))

result = set()
for p in p_lst:
    for q in q_lst:
        result.add(p/q)

print(len(result))

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例



8.

常规的表达式求值，我们都会根据计算的优先级来计算。比如*/的优先级就高于+-。
但是小易所生活的世界的表达式规则很简单，从左往右依次计算即可，而且小易所在的世界没有除法，
意味着表达式中没有/，只有(+, - 和 *)。现在给出一个表达式，
需要你帮忙计算出小易所在的世界这个表达式的值为多少

输入描述:
输入为一行字符串，即一个表达式。其中运算符只有-,+,*。参与计算的数字只有0~9.
保证表达式都是合法的，排列规则如样例所示。

输出描述:
输出一个数，即表达式的值

输入例子:
3+5*7

输出例子:
56


# 思路 把数字和运算符分开，存放在列表中

# python 3

s = input().strip().replace(' ', '')
contain = ['+', '-', '*']
op_lst = []

# 将运算字符的下标取出来放到列表
for i, v in enumerate(s):
    if v in contain:
        op_lst.append(i)

# 计算的过程
if op_lst:
    if len(op_lst) == 1:
        print(eval(s))
    else:
        tmp_result = 0
        for i, v in enumerate(op_lst):
            if i == len(op_lst) - 1: # 最后的下标
                print(eval(str(tmp_result) + s[v:]))
            elif i == 0: # 第一个下标
                tmp_result = eval(s[:op_lst[i+1]])
            else: # 中间的
                tmp_result = eval(str(tmp_result) + s[v:op_lst[i+1]])

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例

# 思路2
# 思路1的解法是通用的，但题目限定了条件，数字是0到9，就是说可以方便地获取成列表 list(input)
# 直接从左往右计算。。 如果没有这个限定，思路一是好解法。

s = input().strip()
lst = list(s)

# 计算结果初始化
tmp_result = eval(lst[0] + lst[1] + lst[2])
i = 3

# 从左到右计算
while i <= len(lst) - 1:
    tmp_result = eval(str(tmp_result) + lst[i] + lst[i+1])
    i += 2

print(tmp_result)

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例

其他人的实现：

expression = raw_input()

expression = list(expression)

res = int(expression[0])

for i in range(len(expression)- 2):

    if expression[i+1] == '+' :

        res = res + int(expression[i+2])

    if expression[i+1] == '-' :

        res = res - int(expression[i+2])

    if expression[i+1] == '*' :

        res = res * int(expression[i+2])

    i= i + 2

print res


9.

小易有一块n*n的棋盘，棋盘的每一个格子都为黑色或者白色，小易现在要用他喜欢的红色去涂画棋盘。
小易会找出棋盘中某一列中拥有相同颜色的最大的区域去涂画，帮助小易算算他会涂画多少个棋格。
输入描述:
输入数据包括n+1行：

第一行为一个整数n(1 ≤ n ≤ 50),即棋盘的大小

接下来的n行每行一个字符串表示第i行棋盘的颜色，'W'表示白色，'B'表示黑色

输出描述:
输出小易会涂画的区域大小

输入例子:
3
BWW
BBB
BWB

输出例子:
3


思路：遍历每列，找相邻最大相同数. 取最大值


# python3

n = int(input())
lst = []
for i in range(n):
    lst.append(list(input()))

# 转置
lst = list(list(i) for i in zip(*lst))

# 统计一列
def near_num(l):
    num = 0
    c = 1
    for i in range(1, len(l)):
        if l[i] == l[i-1]: # 相同累加
            c += 1
            if i == len(l) - 1: # 最后一个需判断赋值
                if c > num:
                    num = c
        else: # 不相同 比较c和num c 重新赋值
            if c > num:
                num = c
            c = 1
    return num

# 遍历每一列 求每一列相邻最大相同数量
results = [near_num(l) for l in lst]
print(max(results))

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例


10.

小易参与了一个记单词的小游戏。游戏开始系统提供了m个不同的单词，小易记忆一段时间之后需要在纸上
写出他记住的单词。小易一共写出了n个他能记住的单词，如果小易写出的单词是在系统提供的，
将获得这个单词长度的平方的分数。注意小易写出的单词可能重复，但是对于每个正确的单词只能计分一次。

输入描述:
输入数据包括三行：

第一行为两个整数n(1 ≤ n ≤ 50)和m(1 ≤ m ≤ 50)。以空格分隔

第二行为n个字符串，表示小易能记住的单词，以空格分隔，每个单词的长度小于等于50。

第三行为m个字符串，系统提供的单词，以空格分隔，每个单词的长度小于等于50。

输出描述:
输出一个整数表示小易能获得的分数

输入例子:
3 4
apple orange strawberry
strawberry orange grapefruit watermelon

输出例子:
136

# python 3

n, m = [int(i) for i in input().split()]
n_lst = [i for i in input().strip().split() if len(i) <= 50]
m_lst = [i for i in input().strip().split() if len(i) <= 50]

n_set = set(n_lst)
m_set = set(m_lst)

score = 0

for i in n_set:
    if i in m_set:
        score += len(i) ** 2

print(score)


# 您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为80.00%

11.

小易有n块砖块，每一块砖块有一个高度。小易希望利用这些砖块堆砌两座相同高度的塔。
为了让问题简单，砖块堆砌就是简单的高度相加，某一块砖只能使用在一座塔中一次。
小易现在让能够堆砌出来的两座塔的高度尽量高，小易能否完成呢。
输入描述:
输入包括两行：
第一行为整数n(1 ≤ n ≤ 50)，即一共有n块砖块
第二行为n个整数，表示每一块砖块的高度height[i] (1 ≤ height[i] ≤ 500000)


输出描述:
如果小易能堆砌出两座高度相同的塔，输出最高能拼凑的高度，如果不能则输出-1.
保证答案不大于500000。

输入例子:
3
2 3 5

输出例子:
5



12.

易老师购买了一盒饼干，盒子中一共有k块饼干，但是数字k有些数位变得模糊了，
看不清楚数字具体是多少了。易老师需要你帮忙把这k块饼干平分给n个小朋友，
易老师保证这盒饼干能平分给n个小朋友。现在你需要计算出k有多少种可能的数值
输入描述:
输入包括两行：

第一行为盒子上的数值k，模糊的数位用X表示，长度小于18(可能有多个模糊的数位)

第二行为小朋友的人数n


输出描述:
输出k可能的数值种数，保证至少为1

输入例子:
9999999999999X
3

输出例子:
4



# 解法1

# python 3

k = input()
n = int(input())

# 下标index为余数 mods[index] 表示余数为index的个数 mods[0] = 1 边界
mods = [1] + [0] * (n-1)

# 遍历数字k，处理每一位
for s in k:
    tmp = [0] * n
    if s != 'X':
        # 处理每一种余数
        for m in range(n):
            mod = int((int(s)+m*10)%n)
            tmp[mod] += mods[m]
    else:
        # 'X' 取值 0-9
        for i in range(10):
            for m in range(n):
                mod = int((i+m*10)%n)
                tmp[mod] += mods[m]
    mods = tmp

print(mods[0])

# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例


小易准备去魔法王国采购魔法神器,购买魔法神器需要使用魔法币,但是小易现在一枚魔法币都没有,
但是小易有两台魔法机器可以通过投入x(x可以为0)个魔法币产生更多的魔法币。
魔法机器1:如果投入x个魔法币,魔法机器会将其变为2x+1个魔法币
魔法机器2:如果投入x个魔法币,魔法机器会将其变为2x+2个魔法币
小易采购魔法神器总共需要n个魔法币,所以小易只能通过两台魔法机器产生恰好n个魔法币,
小易需要你帮他设计一个投入方案使他最后恰好拥有n个魔法币。
输入描述:
输入包括一行,包括一个正整数n(1 ≤ n ≤ 10^9),表示小易需要的魔法币数量。

输出描述:
输出一个字符串,每个字符表示该次小易选取投入的魔法机器。其中只包含字符'1'和'2'。

输入例子1:
10

输出例子1:
122



# 思路
# 1： x -> 2x + 1  最终是奇数
# 2: x -> 2x + 2  最终是偶数

# python 3

n = int(input())
s = ''
while n:
    if n % 2 == 0:
        s += '2'
        n = (n-2) / 2
    else:
        s += '1'
        n = (n-1) / 2
print(s[::-1])



为了得到一个数的"相反数",我们将这个数的数字顺序颠倒,然后再加上原先的数得到"相反数"。
例如,为了得到1325的"相反数",首先我们将该数的数字顺序颠倒,我们得到5231,
之后再加上原先的数,我们得到5231+1325=6556.如果颠倒之后的数字有前缀零,
前缀零将会被忽略。例如n = 100, 颠倒之后是1.
输入描述:
输入包括一个整数n,(1 ≤ n ≤ 10^5)

输出描述:
输出一个整数,表示n的相反数

输入例子1:
1325

输出例子1:
6556



s = input()
print(int(s) + int(s.rstrip('0')[::-1]))

一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定一个字符串,
请你帮助计算这个字符串的所有碎片的平均长度是多少。

输入描述:
输入包括一个字符串s,字符串s的长度length(1 ≤ length ≤ 50),s只含小写字母('a'-'z')


输出描述:
输出一个整数,表示所有碎片的平均长度,四舍五入保留两位小数。

如样例所示: s = "aaabbaaac"
所有碎片的平均长度 = (3 + 2 + 3 + 1) / 4 = 2.25

输入例子1:
aaabbaaac

输出例子1:
2.25


# 思路： 计算相同子序列个数，记得最后一位的判断，此处有坑！
# 另一个坑：结果要用round四舍五入 用round并不能通过 3.50 3.5的区别

# python 3
from decimal import Decimal

s = input()
res = []
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
        if i == len(s) - 1:
            res.append(count)
    else:
        res.append(count)
        count = 1
        if i == len(s) - 1:
            res.append(count)

# print(round(sum(res)/len(res), 2))
print(Decimal(sum(res)/len(res)).quantize(Decimal('0.00')))


魔法王国一共有n个城市,编号为0~n-1号,n个城市之间的道路连接起来恰好构成一棵树。
小易现在在0号城市,每次行动小易会从当前所在的城市走到与其相邻的一个城市,小易最多能行动L次。
如果小易到达过某个城市就视为小易游历过这个城市了,小易现在要制定好的旅游计划使他能游历最多的城市,
请你帮他计算一下他最多能游历过多少个城市(注意0号城市已经游历了,游历过的城市不重复计算)。
输入描述:
输入包括两行,第一行包括两个正整数n(2 ≤ n ≤ 50)和L(1 ≤ L ≤ 100),表示城市个数和小易能行动的次数。
第二行包括n-1个整数parent[i](0 ≤ parent[i] ≤ i), 对于每个合法的i(0 ≤ i ≤ n - 2),
在(i+1)号城市和parent[i]间有一条道路连接。

输出描述:
输出一个整数,表示小易最多能游历的城市数量。

输入例子1:
5 2
0 1 2 3

输出例子1:
3



## 解救小易

# python 3

n = int(input())

x_lst = [int(i) for i in input().split()]
y_lst = [int(i) for i in input().split()]

xy_lst = [[x, y] for x, y in zip(x_lst, y_lst)]

def dis(lst):
    x, y = lst
    return abs(x - 1) + abs(y - 1)

dis_lst = [dis(i) for i in xy_lst]
print(min(dis_lst))



## 统计回文

# python 3

a = input()
b = input()
c = 0
l = len(a)

def is_circle(s):
    return s == s[::-1]

for i in range(l):
    t = list(a)
    t.insert(i, b)
    s = ''.join(t)
    if is_circle(s):
        c += 1

if is_circle(a+b):
    c += 1

print(c)



## 两种排序方法

# python 3

n = int(input())

lst = [input() for i in range(n)]

dict_lst = sorted(lst)
len_lst = sorted(lst, key=len)

if (lst == dict_lst and lst == len_lst):
    print('both')
elif lst == dict_lst:
    print('lexicographically')
elif lst == len_lst:
    print('lengths')
else:
    print('none')


##  Fibonacci数列

# python 3

n = int(input())

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


# print(fib(31))

lst = [fib(i) for i in range(32)]
pivot = 0
for i in range(1, 32):
    if lst[i-1] < n < lst[i]:
        pivot = i
        break

print(min(n-lst[pivot-1], lst[pivot]-n))


# 以上解法超时


# 优化

n = int(input())
collect = [0, 1]
i = 2
s = 0
pivot = 0

while True:
    if s > 1000000:
        break
    else:
        s = collect[i-1] + collect[i-2]
        i += 1
        collect.append(s)

for j in range(1, i):
    if collect[j-1] <= n <= collect[j]:
        pivot = j
        break

print(min(n-collect[pivot-1], collect[pivot]-n))



# 再优化 注意下标

n = int(input())
collect = [0, 1]
i = 2
s = 0
while True:
    if s > n:
        break
    else:
        s = collect[i-1] + collect[i-2]
        i += 1
        collect.append(s)

print(min(n-collect[i-2], collect[i-1]-n))



[编程题] 数字游戏
时间限制：1秒
空间限制：32768K
小易邀请你玩一个数字游戏，小易给你一系列的整数。你们俩使用这些整数玩游戏。
每次小易会任意说一个数字出来，然后你需要从这一系列数字中选取一部分出来让它们
的和等于小易所说的数字。 例如： 如果{2,1,2,7}是你有的一系列数，小易说的数字是11.
你可以得到方案2+2+7 = 11.如果顽皮的小易想坑你，他说的数字是6，那么你没有办法拼凑出和为6
现在小易给你n个数，让你找出无法从n个数中选取部分求和的数字中的最小数。
输入描述:
输入第一行为数字个数n (n ≤ 20)
第二行为n个数xi (1 ≤ xi ≤ 100000)


输出描述:
输出最小不能由n个数选取求和组成的数

输入例子1:
3
5 1 2

输出例子1:
4


## [编程题]数字游戏

# python 3

# 思路：网上的  非常巧妙的解法！！
# 排序后 从0开始判断
# 找到比target大的元素则后面再也拼不出来了 否则累加进target

n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
target = 0
for i in lst:
    if i > target+1:
        break
    else:
        target += i
print(target+1)


"""



