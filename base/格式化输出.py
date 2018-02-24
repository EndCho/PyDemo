#Author: lenovo
#Date: 2017/10/31

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")
if salary.isdigit():
    salary=int(salary)
else:
    print("must input digit")
    #exit()
msg='''
--------info of %s------------
Name:%s
Age:%d
Job:%s
Salary:%d
You will retired in %s years
----------end-------------
''' % (name,name,age,job,salary,65-age)

print(msg)