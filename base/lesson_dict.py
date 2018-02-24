#Author: lenovo
#Date: 2017/12/2
#_*_coding:utf-8_*_

dic={'name':'alex','age':35,'hobby':'girl','is_handsome':True}
print(dic['name'])

#键存在就不改动，返回字典中相应的键对应的值
ret = dic.setdefault('age', 18)
print(ret)


#键不存在，在字典中增加新的键值对，并返回
dic.setdefault('no',1)
print(dic)

print(dic.keys())
del dic['name']#删除字典中指定键值对
print(dic)
dic.pop('age')#删除字典中指定键值对并返回该键的值
print(dic)
dic.popitem()#随机删除某组键值对，并以元组方式返回值
print(dic)
dic.clear()#清空字典的键值对
print(dic)


catelog={'mooc':{'教程':['website','www.imooc.com']},
         'neteasy':{'视频':['wangzhan','edu.163.com']},
         'bilibili':{'娱乐':['网站','www.bilibili.com']}}

catelog['neteasy']['视频'][0]='link'
print(catelog)


dic5={'name':'alax','age':18}
for i  in dic5.items():
    print(i)

dic5={'name':'alax','age':18}#items底层有转化，改成不是元组的形式，数据量大时会耗性能，建议用上面的形式
for i,v  in dic5.items():
    print(i)


#字符串
a="Let's go "
print(a)
print('hello'*2)#重复输出字符串

#查找
print('helloword'[2:])#通过索引获取字符串中的字符，这里和列表中的切片操作是相同的，具体内容见列表
#关键字 in

#格式字符串
print('alax is a good teacher')
print('%s is a good teacher '% 'alax')

a='123'
b='abc'
c='***********'.join([a,b])#用’************‘拼接a,b

print(c)


#String 的内置方法
st='hello kitty {name} is {age}'
print(st.count('l'))#统计元素个数
print(st.capitalize())#首字母大写
print(st.center(50,'#'))#居中，在50个#之间
print(st.startswith('h'))#以某个内容开头
print(st.endswith('tty'))#以某个内容结尾
print(st.expandtabs(10))#设置tab按键的空格数
print(st.find('t'))#查找到第一个元素，并将索引值返回，如果不存在就返回-1

print(st.format(name='alax',age=22))#格式化输出的另一种方式
print(st.format_map({'name':'alax','age':37}))

print(st.index('t'))#查找到第一个元素，并将索引值返回,如果不存在就报错

