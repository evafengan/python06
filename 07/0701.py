# -*- coding:utf-8 -*-

"""os文件库"""
import os

#新建文件夹
# os.mkdir("testdir")

# #移除文件
# os.remove("test/my.txt")
# #删除文件夹
# os.removedirs("test")

# #打印路径下有什么文件
# print(os.listdir("./"))
#
# #打印文件路径
# print(os.getcwd())
#
# #查询是否存在test文件夹
# print(os.path.exists("test"))
#
# #不存在test文件夹，就新建test文件夹
# if not os.path.exists("test"):
#     os.mkdir("test")
#
# #如果不存在my.txt文件，就新建文件且向文件写入
# if not os.path.exists("test/my.txt"):
#     #打开my.txt文件，以w写的权限
#     f = open("test/my.txt","w")
#     #向文件内写入
#     f.write("hello,world")
#     f.close()

# import shutil
# #删除带文件的文件夹
# rootdir = r"/Users/eva/Documents/hogwards202009/code/python06/07/test"
# shutil.rmtree(rootdir, True)

"""time时间库"""
import time

#打印现在时间
print(time.asctime())
#打印时间戳
print(time.time())
#打印本地时间,元组形式显示
print(time.localtime())
#打印本地时间，按格式显示
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#显示两天前的时间
now_timestamp = time.time()
two_day_timestamp = now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))

"""urllib.request库"""
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
#打印响应状态
print(response.status)
#打印响应内容
print(response.read())
#打印响应的头文件
print(response.headers)

"""math计算库"""
import math
#向上取整
print(math.ceil(5.3))
#向下取整
print(math.floor(5.6))
#开平方
print(math.sqrt(36))

