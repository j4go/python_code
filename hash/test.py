# coding: utf-8

args_dict = {
	"a": "arg_a",
	"b": "arg_b"
}
# for k,v in args_dict.items():
# 	print k,v

# print(args_dict.items())
# print(args_dict.values())

def test_func(**arg):
	print arg

# test_func(**args_dict)

vec = [-2, 3, 0, 8, -9, 1]
vec1 = [x * 2 for x in vec if x > 0]
# print(vec1)

from sys import argv
print argv

