#Author: lenovo
#Date: 2018/2/24
#_*_coding:utf-8_*_

a=set([1,2,3,4,5])
b=set([4,5,6,7,8])

#intersection 交集 # a & b
print(a.intersection(b)) #{4, 5}
print(a & b)

#union 并集 a= t | s #t和s 的并集
print(a.union(b))   #{1, 2, 3, 4, 5, 6, 7, 8}
print(a | b)


print(a.difference(b)) #{1, 2, 3} in a but not in b     #a-b
print(a - b)
print(b.difference(a)) #{8, 6, 7} in b but not in a     #b-a
print(b - a)


print(a.symmetric_difference(b)) #symmetric=对称 差集，反向交集 #a ^b
print(a ^ b)

#父集 超集
print(a.issubset(b)) #a>b
print(a.issubset(b)) #子集 a<b