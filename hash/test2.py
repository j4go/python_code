# coding:utf-8


'''
my own deepcopy function

'''
# def my_own_deepcopy(obj):
# 	ret = {}

# 	# obj could be array or others
# 	if (not isinstance(obj, (dict, list, tuple))):
# 		print('####')
# 		return obj

# 	# only for dict
# 	for k in obj:
# 		if (isinstance(obj[k], list)):
# 			print("###list")
# 			ret[k] = obj[k][:]
# 		elif (isinstance(obj[k], dict)):
# 			print("###dict")
# 			ret[k] = my_own_deepcopy(obj[k])
# 		else:
# 			print "33333"
# 			ret[k] = obj[k]

# 	return ret



# t1 = {'a':1,2:'b',3:{4:[1,2,{12:[1,2]}]}}
# t2 = [1,2,3]

# print my_own_deepcopy(t1)

#print type(t1) == dict





'''
quick sort

'''

# def quick_sort(a):
# 	if (len(a) < 2):
# 		return a
# 	pivot_index = len(a) // 2 # pick middle index as pivot index
# 	pivot = a[pivot_index:pivot_index+1][0]
# 	del a[pivot_index]
# 	left_a = []
# 	right_a = []
# 	for i in xrange(len(a)):
# 		if(a[i] <= pivot):
# 			left_a.append(a[i])
# 		else:
# 			right_a.append(a[i])
# 	return quick_sort(left_a) + [pivot] + quick_sort(right_a)


# a = [3,4,8,2,9,1]
# print(quick_sort(a))




# def conflict(t, next_x):
# 	next_y = len(t) # 下一列
# 	for i in xrange(next_y):
# 		if(abs(t[i] - next_x) in (0, next_y - i)):
# 			return True 
# 	return False

# def queens(num=8, t=()):
# 	if len(t) == num-1:
# 		for i in xrange(num):
# 			if(not conflict(t, i)):
# 				yield (i,)
# 	else:
# 		for i in xrange(num):
# 			if(not conflict(t, i)):
# 				for ret in queens(num, t + (i,)):
# 					yield (i,) + ret

# for i in queens():
# 	print i

# print(len(list(queens())))


# def conflict(a, next_x):
# 	next_y = len(a) # 下一列
# 	for i in xrange(next_y):
# 		if(abs(a[i] - next_x) in (0, next_y - i)):
# 			return True 
# 	return False

# def queens(num=8, a=[]):
# 	if len(a) == num-1:
# 		for i in xrange(num):
# 			if not conflict(a, i):
# 				yield [i]
# 	else:
# 		for i in xrange(num):
# 			if not conflict(a, i) :
# 				for ret in queens(num, a + [i]):
# 					yield [i] + ret


# print(len(list(queens(8))))



# import re
# p = re.compile('[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+')
# m = p.match('yianny@163.com')
# if m is not None:
# 	print m.group()

# print ord('a')
# print chr(65)

s = set('abc')
print list(s)