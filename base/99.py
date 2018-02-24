#Author: lenovo
#Date: 2017/11/10
#coding=utf-8

i=1
while i<=9:
    j=1
    while j<=i:
        print(i,"*",j,"=",i*j,end=" ")
        j+=1
    i+=1
    print()


line=5
while line>0:
    temp=line
    while temp>0:
        print("*",end="")
        temp-=1
    print()
    line-=1

import sys
print(sys.argv)