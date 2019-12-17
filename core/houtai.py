# Author: Mr.Xue
# 2019.10.31

#!usr/bin/python3

import ast

from core import shops
from core import accounts

def run():
	caozuo = ['modify', 'delete', 'insert', 'add_acc', 'del_acc']
	file_name = 'thing.txt'

	#f = open(file_name, 'r+')
	#info = f.read()
	#info_list = ast.literal_eval(info)
	#f.close()
	info_list = shops.load_shop_info()

	while True:
		i = 1
		for x in caozuo:
			print(i, x)
			i += 1
		choice = input('input your choice(1-3): ')
		while True:
			if choice.isdigit():
				if int(choice) == 1: # modify
					for j, x in enumerate(info_list):
						print('\t', j+1, x)
					choice2 = input('\tinput which one you want modify: ')
					if choice2.isdigit():
						modify_price = int(input('\tinput the modify price: '))
						info_list[int(choice2)-1][1] = modify_price
					elif choice2 == 'q':
						break
					else:
						print('\tInvalid input...')
				elif int(choice) == 2: # delete
					for j, x in enumerate(info_list):
						print('\t', j+1, x)
					choice3 = input('\tinput which one you want delete: ')
					if choice3.isdigit():
						del info_list[int(choice3)-1]
					elif choice3 == 'q':
						break
					else:
						print('\tInvalid input...')
				elif int(choice) == 3: # insert
					thing_name = input("\tinput the thing's name you want insert: ")
					if thing_name == 'q':
						break
					thing_price = int(input("\tinput the thing's price: "))
					list1 = []
					list1.append(thing_name)
					list1.append(thing_price)
					info_list.append(list1)
				else:
					print('Invalid value...')
			elif choice == 'q':
				#f = open(file_name, 'r+')
				#f.write(str(info_list))
				#f.close()
				shops.dump_shop_info(info_list)
				print('you choice exit...')
				exit()
			else:
				print('please input digit...')