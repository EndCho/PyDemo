#Author: lenovo
#Date: 2017/12/11
#_*_coding:utf-8_*

def sayhello():
    print('hello, jack!')


def printMax(a,b):
    if a>b:
        print(a,">",b)
    else:
        print(b,">",a)

printMax(3,4)


sayhello()


def func(x):
    print('x is',x)
    x=2
    print('changed local x to ',x)
x=50
func(x)


#得到python3默认编码为utf-8
import sys
print(sys.getdefaultencoding())


