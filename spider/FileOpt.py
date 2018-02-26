#Author: lenovo
#Date: 2018/2/26
#_*_coding:utf-8_*_


import os
print(os.getcwd())#D:\Demo\PyDemo\spider

#删除一个文件
os.remove('path')

#删除多个空目录
os.removedirs(r'd:\python')

#检验给出的路径是否是一个文件
os.path.isfile('filepath')

#检验给出的路径是否是一个目录
os.path.isdir('filename')

#判断是否是绝对路径
os.path.isabs('filepath')
