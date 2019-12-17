# Author: Mr.Xue
# 2019.10.31

#!usr/bin/python3

import os,sys

#print(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from core import main_shop
from core import houtai
from core import main_atm

menu = """
---------all---------
1、ATM机入口
2、商城入口
3、商城后台入口
"""

list_info = {'1': main_atm, '2': main_shop, '3': houtai}

exit_flag = False
while not exit_flag:
    print(menu)
    choice = input("enter your choice>>:")
    if choice in list_info:
        list_info[choice].run()
    else:
        print("\033[21;1mOption does not exist!\033[0m")
#main.sayhi()
#main_atm.run()
#main_shop.run()
#houtai.run()