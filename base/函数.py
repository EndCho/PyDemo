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
