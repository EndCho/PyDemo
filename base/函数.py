#Author: lenovo
#Date: 2018/2/24
#_*_coding:utf-8_*_


def function1(log_text):
    f = open("log.txt", "a")
    f.write("exec function 1 %s" % log_text)
    f.close()
    print(log_text)


print("--------function 1 --------")
#function1()

#函数 != function()
#计算机函数 == subroutine 子程序,procedures 过程
#作用：
    # 1.减少重复代码
    # 2.方便修改,更易扩展
    # 3.保持代码一致性



def f():
    print("ok")

f() #调用一定记得加括号


import time
time_format = "%Y-%m-%d %X"
time_current = time.strftime(time_format)

print(time_current)