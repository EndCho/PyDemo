#Author: lenovo
#Date: 2018/2/24
#_*_coding:utf-8_*_


def function1(log_text):
    f = open("log.txt", "a")
    f.write("exec function 1 %s" % log_text)
    f.close()
    print(log_text)


print("--------function 1 --------")
function1()

#函数 != function()
#计算机函数 == subroutine 子程序,procedures 过程
#作用：
    # 1.减少重复代码
    # 2.方便修改,更易扩展
    # 3.保持代码一致性
