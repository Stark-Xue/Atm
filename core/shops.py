# Author: Mr.Xue
# 2019.10.27

#!usr/bin/python3

import json
import time


from core import db_handler
from conf import settings

def load_shop_info():
    """return shop list
    :return:
    """

    db_path = db_handler.db_handler(settings.DATABASE)
    shop_file = '%s/thing.json' % (db_path)
    with open(shop_file) as f:
        shop_data = json.load(f)
        return shop_data

def dump_shop_info(shop_data):
    db_path = db_handler.db_handler(settings.DATABASE)
    shop_file = '%s/thing.json' % (db_path)
    with open(shop_file, 'w') as f:
        f.write(json.dumps(shop_data))