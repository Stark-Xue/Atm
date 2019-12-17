# Author: Mr.Xue
# 2019.10.24

#!usr/bin/python3

import time

from core import auth
from core import accounts
from core import shops
from core import account_shoplist

#temp account data, only saves the data in memory
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

def interactive(user_data, acc_data):
    """interact with user
    :return:
    """

    buy_list = [] # 已购买列表清单
    shop_data = shops.load_shop_info()
    while True:
        print('---- shop ----')
        for index, item in enumerate(shop_data):
            print(index+1, item[0], item[1])
        num = input("输入您想买的商品的编号: ")
        #print(shop_list[int(num)-1])
        if not num.isdigit():
            if num == 'q':
                print('您购买的商品列表如下：')
                for x in buy_list:
                    print(x)
                print('您的余额还剩下：', acc_data['balance'])
                accounts.dump_account(acc_data)
                account_shoplist.dump_shoplist(acc_data['id'], buy_list)
                break
            else:
                print('输入数字或者输入q结帐')
        else:
            if int(num) <=len(shop_data) and int(num) > 0:
                if acc_data['balance'] < float(shop_data[int(num)-1][1]):
                    print("您的余额不足")
                else:
                    buy_list.append(shop_data[int(num)-1])
                    acc_data['balance'] -= float(shop_data[int(num)-1][1])
                    print("您购买了%s, 您的余额还剩下\033[31;1m%s\033[0m" % (shop_data[int(num)-1][1], acc_data['balance']))
            else:
                print("该商品不存在")

def run():
    """the function will be called right way when the program started,
    here handles the user shopping
    :return:
    """

    acc_data = auth.acc_login(user_data)#, access_logger
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data, acc_data)