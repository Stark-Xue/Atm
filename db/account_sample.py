# Author: Mr.Xue
# 2019.10.24

#!usr/bin/python3

import json

acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0=normal, 1=locked, 2=disabled
}

#print(json.dumps(acc_dic))
with open("1234.json", 'w') as f:
	#f.write(str(info))
	#print(json.dumps(info))
	#f.write(json.dumps(info))
	f.write(json.dumps(acc_dic)) # pickle.dump(info, f)