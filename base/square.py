#Author: lenovo
#Date: 2017/11/10
#coding=utf-8

height=int(input("please input height:"))
width = int(input("please input width:"))
num_height=1
while num_height<=height:
    num_width=1
    while num_width<=width:
        print("#",end="")
        num_width+=1
    print()
    num_height+=1