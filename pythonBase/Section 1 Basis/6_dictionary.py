#! python3
#encoding:utf-8

# 1)
def dic_create(dic,key,value):
	dic_new = {}
	dic_new['Hubei'] = 'Wuhan'
	dic_new['Hunan'] = 'Changsha'
	
	if dic_new:
		print("dic_new = " + str(dic_new))
	else:
		print("create an empty directory")
	return dic_new

def dic_add(dic,key,value):
	print("before add:"+str(dic))
	if key.title() not in dic:
		dic[key.title()] = value.title()
		print("after add:"+str(dic))
	else:
		print(key+" already in the dictionary")
	return dic
	
def dic_modify(dic,key,value):
	if dic:
		if key.title() in dic:
			print("before modify:"+str(dic))
			dic[key.title()] = value.title()
			print("after modify:"+str(dic))
		else:
			print(key+" not in the dictionary")
	else:
		print("this is an empty directory")
	return dic

def dic_delete(dic,key,value):
	if dic:
		if key.title() in dic:
			print("before delete:"+str(dic))
			del dic[key.title()]
			print("after delete:"+str(dic))
		else:
			print(key+" not in the dictionary")
	else:
		print("this is an empty directory")
	return dic

def dic_traversal(dic,key,value):
	if dic:
		for key,value in dic.items():
			print(key,value)
	else:
		print("this is an empty directory")
		
def dic_access(dic,key,value):
	province_capitals = {'Hubei':'Wuhan','Hunan':'Changsha','Yunnan':'Kunming','Guangdong':'Guangzhou'}

	if province_capitals:
		print(province_capitals)
	else:
		print("this is an empty directory")
	'''	
	print("input a province:")
	province = input()
	tem_province = province.title()
	'''
	province = input("input a province:")

	if province.title() in province_capitals:
		print(province + "'s capital is " + province_capitals[province.title()])
	else:
		print(province + " is not in the province_capitals")

def print_func(dic,key,value):
	print("direction test lists:")
	
	for cmd,func in func_lists.items():
		print(cmd,func)
	
def default():
	print("input a wrong command")
	
func_lists = {
	'01':dic_create,
	'02':dic_add,
	'03':dic_modify,
	'03':dic_delete,
	'04':dic_traversal,
	'05':dic_access,
	'help':print_func,
	}	

def dictionary_run():
	print_func(func_lists,None,None)
	
	dic_test = dic_create(None,None,None)
	'''
	try:
		key_val = input("input key value:")
		key_val = key_val.split()	#default seperator is a space
		dic_add(dic_test,key_val[0],key_val[1])
	except:
		print("input key value wrong")
	'''
	while True:
		key = input("please input cmd:")
		key = key.split()
		
		if key[0].lower() in func_lists:
			if len(key) == 1:
				key.append('0')
				key.append('0')
			elif len(key) == 2:
				key.append('0')
			print(key[0].lower(),key[1],key[2])
			func_lists.get(key[0].lower(),default)(dic_test,key[1],key[2])
		elif key[0].lower() == 'exit':	 
			break;
		else:
			print("input a wrong cmd.")

dictionary_run()	
	
