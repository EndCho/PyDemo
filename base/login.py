#Author: lenovo
#Date: 2017/11/10
#_*_coding:utf-8_*_

for i in range(3):
    _user = "Chou"
    _passwd = "abc123"

    username = input("usernume:")
    passwd = input("password:")

    if username==_user and passwd == _passwd:
        print("Welcome %s login..."% _user)
        break
    else:
        print("Invalid username or password")
