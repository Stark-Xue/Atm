# Author: Mr.Xue
# 2019.10.24

#!usr/bin/python3

from conf import settings
from core import accounts

def make_transaction(account_data, tran_type, amount, **others):
    """deal all the user transactions
    :param account_data: user account data
    :param tran_type: transaction type
    :param amount: transaction amount
    :param others: mainly for logging usage
    :return:
    """

    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data["balance"]
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
            account_data['balance'] = new_balance
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s],
                    your current balance is [%s]\033[0m''' % (account_data['credit'], (amount + interest), account_data['balance']))
                return
            account_data['balance'] = new_balance
        accounts.dump_account(account_data)
        return account_data
    else:
        print("\033[31;1mTansaction type [%s] is not exits!\033[0m" % tran_type)            