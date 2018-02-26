#Author: lenovo
#Date: 2018/2/26
#_*_coding:utf-8_*_


try :
    import  cPickle as pickle
except ImportError:
    import pickle

#pickle实现序列化主要使用的是dumps方法或dump方法。
#dumps方法可以将任意对象序列化为一个str，然后可以将这个str写入文件进行保存.
d = dict(url='index.html',title='首页',content='首页')
pickle.dumps(d)

#使用dump方法，可以将序列化后的对象直接写入文件中

f=open(r'D:\dump.txt','wb')#r使用后目录不有转义了。
pickle.dump(d,f)
f.close()


#pickle实现反序列化使用的是loads方法或load方法。把序列化后的文件从磁盘上读取为一个str，
# 然后直接使用loads方法将这个str反序列化为对象，或者直接使用load方法将文件反序列化为对象
