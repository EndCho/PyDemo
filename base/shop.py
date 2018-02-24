#Author: lenovo
#Date: 2017/11/10
#_*_coding:utf-8_*_

salary = 5000
product_list=[
    ("Mac",9000),
    ("kindle",8000),
    ("tesla",30000),
    ("python book",105),
    ("bike",2000),
]

saving = input('please input your money:')
shopping_car=[]
if saving.isdigit():#判断输入的是不是一个数字
    saving = int(saving)
    while True:
        #打印商品内容
        for i,v in enumerate(product_list,1):
            print(i,v)
        #引导用户选择商品
        choice=input('选择购买商品的编号[退出：q]：')

        #验证输入是否合法
        if choice.isdigit():
            choice=int(choice)
            #将用户选择商品通过choic选出来
            if choice>0 and choice<=len(product_list):
                p_item=product_list[choice-1]

                #
                if p_item[1]<saving:
                    saving-=p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，还剩%s'%saving)
            else:
                print('编码不存在')
        elif choice=='q':
            print('-------------你已购买以下商品---------')
            #循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print('你还剩%s元钱'%saving)
            print('退出')
            break
        else:
            print('invalid input')

