# -*- coding: utf-8 -*-

# url = "https://source.unsplash.com/random/800x450?technology,computer,phone,mac,digital"
# import sys
# pic_url = None # 要保存的图片的目录
# # 要保存的图片的目录
# if sys.platform == "darwin":
#     pic_url = "/Users/molock/py3env/"
# else:
#     pic_url = "/usr/share/nginx/py_get_pics_dir/" 



# import requests
 
# r = requests.get(url=url)   
# # print(r.status_code)    # 获取返回状态

# url = r.url # 获得真实的图片url
# status_code = r.status_code

# from urllib.parse import urlparse, parse_qs
# parseResult = urlparse(url)
# param_dict = parse_qs(parseResult.query) # 解析url中的参数和值

# fm = param_dict.get('fm')
# pic_extname = None # 图片后缀名
# if fm:
#     pic_extname = fm[0]

# import uuid, hashlib
# import redis
# # 连接redis
# # pr = redis.Redis(host='127.0.0.1', port=6379,db=0)

# if status_code == 200 and pic_extname:
#     # 拼成将要保存的文件名
#     filename = str(uuid.uuid1()).replace('-', '') + '.' + pic_extname
#     full_filename = pic_url + filename
#     file_md5 = None # 文件的md5
#     with open(full_filename, 'wb') as file:
#         file.write(r.content)
#     # with open(full_filename, 'rb') as file:
#     #     file_md5=hashlib.md5(file.read()).hexdigest()
#     #     pr.hset("pic_md5_uuid", file_md5, filename)
#     #     print(pr.hgetall("pic_md5_uuid"))

# -*- coding: utf-8 -*-
import sys, requests, uuid, hashlib
url = "https://source.unsplash.com/random/800x450"
pic_url = "/Users/molock/py3env/" # 要保存的图片的目录
r = requests.get(url=url)   
url = r.url # 获得真实的图片url
status_code = r.status_code

from urllib.parse import urlparse, parse_qs
parseResult = urlparse(url)
param_dict = parse_qs(parseResult.query) # 解析url中的参数和值

fm = param_dict.get('fm')
pic_extname = None # 图片后缀名
if fm:
    pic_extname = fm[0]

if status_code == 200 and pic_extname:
    # 拼成将要保存的文件名
    filename = str(uuid.uuid1()).replace('-', '') + '.' + pic_extname
    full_filename = pic_url + filename
    file_md5 = None # 文件的md5
    with open(full_filename, 'wb') as file:
        file.write(r.content)