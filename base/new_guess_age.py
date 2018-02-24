#Author: lenovo
#Date: 2017/11/7
#coding=utf-8

age = 50
flag = True

while flag:
    user_input_age = int(input("Age is :"))
    if(user_input_age==age):
        print("yes")
        print("end")
        flag=False
    elif(user_input_age>age):
        print("bigger")
    else:
        print("smaller")
