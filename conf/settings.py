# Author: Mr.Xue
# 2019.10.24

#!usr/bin/python3

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage', # support mysql, postgresql in the future
    'name': 'data',
    'path': "%s/db" % BASE_DIR
}

TRANSACTION_TYPE = {
    'repay': {"action": 'plus', "interest": 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0}
}