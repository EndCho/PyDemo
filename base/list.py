#Author: lenovo
#Date: 2017/11/5
#coding=utf-8
aList=[123,'xyz','zxcz','abc']
aList.append("hello")
print(aList)
print(aList.count("hello"))
print(aList.extend(["python",456]))
print(aList)
print(aList.index(123))
var1="hive"
if(var1 in aList):
    print(aList.index(var1))
else:
    print("%s not in aList"%(var1))

aList.insert(3,"three")
print("插入后",aList)
print("移除的元素是",aList.pop(1))
print("移除后的aList",aList)

#print(aList.sort(lambda x,y:cmp(len(str(x)),len(str(y)))))