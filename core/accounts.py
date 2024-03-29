# Author: Mr.Xue
# 2019.10.24

#!usr/bin/python3

import json
import time


from core import db_handler
from conf import settings

def load_current_info(account_id):
    """return account basic info
    param account_id: user name
    :return:
    """

    db_path = db_handler.db_handler(settings.DATABASE)
    #print(type(account_id))
    account_file = '%s/%s.json' % (db_path, account_id)
    with open(account_file) as f:
        acc_data = json.load(f)
        return acc_data

def dump_account(account_data):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' % (db_path, account_data['id'])
    with open(account_file, 'w') as f:
        f.write(json.dumps(account_data))