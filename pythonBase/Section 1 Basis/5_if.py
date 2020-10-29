#! python3
#encoding:utf-8

# 1)检查单个条件
cities = ['Beijing','Shenzhen','Guangzhou','Shanghai','Wuhan']

if cities:
	print(cities)
else:
	print("this is an empty list")
	
if 'HongKong' in cities:	#判断变量是否在列表中
	print("")
else:
	print("HongKong is not in the list")
	
for city in cities:
	if city == 'Shenzhen':	
		print(city.upper())
	else:
		print(city.title())
#字符串比较区分大小写，若不用区分大小写，可都转成大写或小写再比较
#if city.lower == shenzhen:

#检查特定值是否包含在列表中
mem = 'Xian'
if mem not in cities:
	print("Xian is not in the list")


# 2) 检查多个条件
num_1 = 1
num_2 = 20

num = int(input("input a number:"))
if num_1 <= num and num_2 >= num:	#与条件判断
	print("input number is proper")
elif num_1 > num:
	print("number is smaller")
else:
	print("number is bigger")
#if num_1 <= num or num_2 >= num:  #或条件判断



