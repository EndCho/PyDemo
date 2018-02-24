#Author: lenovo
#Date: 2017/12/8
#_*_coding:utf-8_*_

menu = {
    '北京':{
            '朝阳':{
                'CICC':{},
                'HP':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                'apple':{},
            },

            '昌平':{
                '沙河':{
                    '老男孩':{},
                    '阿泰包子':{},
            },
            '天通苑':{
                "链家":{},
                '我爱我家':{},
            },
            '回龙观':{},
            },
            '海淀':{
                '五道口':{
                    '谷歌':{},
                    '网易':{},
                    'sohu':{},
                    'sougou':{},
                    '快手':{}
            },
            '中关村':{
                "youku":{},
                'iqiyi':{},
                '汽车之家':{},
                '新东方':{},
                "QQ":{},
            }

        },
    },
    '上海':{
        '浦东':{
            "陆家嘴":{
                "CICC":{},
                "高盛":{},
                "摩根":{},

            },
            "外滩":{},
        },
        '闵行':{},
        '静安':{},
    },
    '山东':{
        "济南":{

        },
        "德州":{
            "乐陵":{
                "丁坞镇":{},
                "城区":{},
            },

        }
    }

}
back_flag=False
while not back_flag:
    for key in menu:
        print(key)
    choice = input("1>>>>>>>").strip()
    if choice in menu:
        while not back_flag:
            for key2 in menu[choice]:
                print(key2)
            choice2 =input("2>>>>>>>").strip()
            if choice2 in menu[choice]:
                while not back_flag:
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    choice3 = input("3>>>>>")
                    if choice3 in menu[choice][choice2]:
                        while not back_flag:
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            choice4 = input("4>>>>>")
                            if choice4 in menu[choice][choice2][choice3]:
                                print("last lever")
                                if choice4=='b':
                                    back_flag = True