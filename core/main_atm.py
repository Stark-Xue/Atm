# Author: Mr.Xue
# 2019.10.24

#!usr/bin/python3

import time

from core import auth
from core import accounts
from core import transaction
from core import account_shoplist
#from core import logger

#transaction logger
#trans_logger = logger.logger("transaction")
#access logger
#acc_logger = logger.logger('access')

#temp account data, only saves the data in memory
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

def account_info(acc_data):
    current_data = accounts.load_current_info(acc_data['account_id'])
    print(current_data)
    #print(acc_data)

def repay(acc_data): # 还款
    """print current balance and let user repay the bill
    :return:
    """

    account_data = accounts.load_current_info(acc_data['account_id'])
    # print(acc_data['account_data']['balance'])
    current_balance = '''-------- BALANCE INFO --------
        Credit: %s
        Balance: %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    if account_data['credit'] == account_data['balance']:
        back_flag = True
        print("用户[%s]不需要还款" % acc_data['account_id'])
    while not back_flag:
        repay_amount = input("\033[31;1m输入还款金额: \033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            #account_data['balance'] = account_data['balance'] + int(repay_amount)
            account_data = transaction.make_transaction(account_data, 'repay', repay_amount)
            need_repay = account_data['credit'] - account_data['balance']
            print("[%s] 您现在的额度是: %s, 还需要还款%s" % (acc_data['account_id'], account_data['balance'], need_repay))
            #print(account_data)
        elif repay_amount == 'b':
            back_flag = True
        else:
            print("\033[32;1m[%s] is not a valid ammout, only accept integer!\033[0m" % repay_amount)

def withdraw(acc_data): # 取款
    """print current balance and let user withdraw the bill
    :return:
    """

    account_data = accounts.load_current_info(acc_data['account_id'])
    # print(acc_data['account_data']['balance'])
    current_balance = '''-------- BALANCE INFO --------
        Credit: %s
        Balance: %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[31;1m输入取款金额\033[0m")
        if withdraw_amount.isdigit() and float(withdraw_amount) <= account_data['balance']:
            account_data = transaction.make_transaction(account_data, 'withdraw', withdraw_amount)
            print('\033[32;1m您现在的额度还剩[%s]' % account_data['balance'])
        elif withdraw_amount.isdigit() and float(withdraw_amount) > account_data['balance']:
            print("\033[32;1m提现余额不足，您的余额为[%s]\033[0m" % account_data['balance'])
        elif withdraw_amount == 'b':
            back_flag = True
        else:
            print("\033[32;1m[%s] is not a valid ammout, only accept integer!\033[0m" % withdraw_amount)     

def transfer(acc_data):
    id = input("输入转账人的id：")
    

def pay_check(acc_data):
    '''print what things user even bought
    :return:
    '''

    shoplist = account_shoplist.load_shoplist(acc_data['account_id'])
    #print(type(shoplist))
    print("客户[%s]购买记录：" % acc_data['account_id'])
    for k, v in shoplist.items():
        print(k ,v)

def logout(acc_data):
    exit(0)

def interactive(acc_data):
    """interact with user
    :return:
    """

    menu = '''
    -------bank-------
    \033[32;1m1. 账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 账单
    6. 退出
    \033[0m'''

    menu_dict = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }

    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        # print(user_option)
        if user_option in menu_dict:
            menu_dict[user_option](acc_data)
        else:
            print("\033[21;1mOption does not exist!\033[0m")

def sayhi():
    print("in the main")

def run():
    """the function will be called right way when the program started,
    here handles the user interaction stuff
    :return:
    """

    acc_data = auth.acc_login(user_data)#, access_logger
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        # 在这里将登录成功的用户信息记录到在线文件中
        interactive(user_data)