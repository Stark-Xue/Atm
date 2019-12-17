# Author: Mr.Xue
# 2019.10.27

#!usr/bin/python3

import json
import datetime


from core import db_handler
from conf import settings

def load_shoplist(account_id):
    """return account shop list info
    param account_id: user name
    :return:
    """

    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s_shoplist.json' % (db_path, account_id)
    with open(account_file) as f:
        acc_data = json.load(f)
        return acc_data

def dump_shoplist(id, buy_list):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s_shoplist.json' % (db_path, id)
    nowtime = datetime.datetime.now()
    dic1 = load_shoplist(id)
    dic2 = {str(nowtime): buy_list}
    dic1.update(dic2)
    with open(account_file, 'w') as f:
        f.write(json.dumps(dic1))