#Author: lenovo
#Date: 2018/2/4
#_*_coding:utf-8_*_

#能调用方法的一定是对象

import sys

#data = open('你好', 'r',encoding='utf8').read()

#f = open('你好','a',encoding='utf-8')
#print(f.readline()) #后面换行符也打印出来
#print(f.readline())

#data=f.read()
#print(data)

# print(f.read(2))
# print(f.read(2))

# print(f.readlines())


#--------------
# data = f.readlines()#只需要读数据出来，不需要操作就可以关闭文件了
# f.close()
# number=0
# for i in data:
#     number+=1
#     if number==2:
#         i=''.join([i.strip(),'mmmmmmm'])#取代万恶的+
#     print(i.strip())




# for i in f:#这是for内部将对象作为一个迭代器，用一行取一行
#     print(i.strip())

#---------------调整光标
# print(f.tell())
# print(f.read(1))
# print(f.tell())
#
# f.seek(0)
# print(f.tell())


#---------------进度条
# import sys,time
#
# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush()
#     time.sleep(0.2)

# import time
# for i in range(30):
#     print('*',end='',flush=True)
#     time.sleep(0.2)

# 截断
# f.truncate(5)
# print(f.seekable())
# print(f.readable())
# f.close()


# f = open('你好','r+') #以读写模式打开文件
# print(f.read(5))#可读
# f.write('hello')
# print('------')
# print(f.read())

# f_read=open('你好','r',encoding='utf-8')
# f_write = open('你好1', 'w', encoding='utf-8')
#
# number=0
# for line in f_read.readlines():
#     number+=1
#     if number==2:
#         line=''.join([line.strip(),'GG'])
#     f_write.write(line)


#with 语句执行完成就自动关闭文件
with open('你好','r') as f:
    f.readlines()
    f.read()
