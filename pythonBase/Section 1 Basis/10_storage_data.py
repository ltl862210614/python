#! python3
#encoding:utf-8

import json
'''
序列化：enconding——把一个Python对象编码转换成json字符串
反序列化：decoding——把一个json字符串解码转换成Python对象
'''

numbers = [2,4,55,77,521,4854]

filepath = "testfile/"
filename = "numbers.json"

try:
	with open(filepath+filename,'a',encoding="utf-8") as file_obj:
		json.dump(numbers,file_obj)	#indent=4,设置缩进格式
		file_obj.write('\n')
except FileNotFoundError:
	print("the file '"+filename+"' doesn't exit.")

try:
	with open(filepath+filename,'r') as file_obj:
		for line in file_obj.readlines():
			line = line.strip()	#去掉空行
			if len(line) != 0:
				json_data = json.loads(line)
				print(json_data)
except FileNotFoundError:
	print("the file '"+filename+"' doesn't exit.")
