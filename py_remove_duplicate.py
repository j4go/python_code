# -*- coding: utf-8 -*-
# import os, sys

# 列出当前目录所有文件夹
# l = [i for i in os.listdir('.') if os.path.isdir(i)]

# # 列出当前目录所有文件
# all_filename_list = [i for i in os.listdir('.') if os.path.isfile(i)]

# 列出当前目录所有后缀jpg的文件
# l = [i for i in os.listdir('.') if os.path.isfile(i) and os.path.splitext(i)[1]=='.jpg']

# 获取当前文件夹名
# l = os.path.dirname(__file__)
# l = os.path.abspath(__file__)
# l = os.path.basename(__file__)

# print(os.path.abspath(__file__))
# print(os.path.basename(__file__))




# d = None 
# if sys.platform == "darwin":
#     d = '/Users/molock/py3env/'
# else:
#     d = '/usr/share/nginx/py_get_pics_dir/'

import os, hashlib
d = os.getcwd()
all_filename_list = [i for i in os.listdir('.') if os.path.isfile(i)]
not_duplicate_arr = []
for filename in all_filename_list:
    full_filename = d + '/' + filename
    with open(full_filename, 'rb') as file:
        file_md5=hashlib.md5(file.read()).hexdigest()
        if file_md5 not in not_duplicate_arr:
            not_duplicate_arr.append(file_md5)
        else:
            os.remove(full_filename)


