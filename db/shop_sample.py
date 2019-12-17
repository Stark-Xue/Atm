# Author: Mr.Xue
# 2019.10.27

#!usr/bin/python3

import json

acc_dic = [['apple', 200], ['banana', 100], ['milk', 200], ['water', 100], ['iphone', 4000]]

#print(json.dumps(acc_dic))
with open("thing.json", 'w') as f:
	#f.write(str(info))
	#print(json.dumps(info))
	#f.write(json.dumps(info))
	f.write(json.dumps(acc_dic)) # pickle.dump(info, f)