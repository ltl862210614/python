'''
通过字符串调用函数或方法
'''
#! python3
#import sys

def test1():
	print("test1")
	
def test2():
	print("test2")

def test3():
	print("test3")

class func_class(object):
	'''
	class Struct(object):
		def __init__(self,cmd,func):
			self.cmd = cmd
			self.func = func
			
	def make_struct(self,cmd,func):
		return self.Struct(cmd,func)
	'''	
	def test4(self):
		print("test4")
	
	def test5(self):
		print("test5")

		
func_lists = {
	'01':'test1',
	'02':'test2',
	'03':'test3',
	'04':'test4',
	'05':'test5',
	}

def print_func():
	print("dictionary test lists:")
	
	for cmd,func in func_lists.items():
		print(cmd,func)

def dictionary_run():
	exec('print("Hello Python")')
	print_func()
	
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
		key = key.split(' ',-1)
		if len(key) > 1:
			print(key[0],key[1])
		
		if key[0].lower() in func_lists:
			print(key[0].lower(),func_lists[key[0].lower()])
			
			if int(key[0]) < 4:
				'''
				eval() 通常用来执行一个字符串表达式，并返回表达式的值。在这里它将字符串转换成对应的函数。
				eval() 功能强大但是比较危险（eval is evil），不建议使用。
				locals() 和 globals() 是python的两个内置函数，通过它们可以一字典的方式访问局部和全局变量。
				'''
				if len(key) > 1:
					if int(key[1]) == 1:
						eval(func_lists[key[0].lower()])()
					elif int(key[1]) == 2:
						globals()[func_lists[key[0].lower()]]()
				else:
					locals()[func_lists[key[0].lower()]]()
			elif int(key[0]) < 6:
				#getattr() 是 python 的内建函数，getattr(object,name) 就相当于 object.name，但是这里 name 可以为变量。
				getattr(func_class(),func_lists[key[0].lower()])()
				
				exec("func_class().%s()"%func_lists[key[0].lower()])
				
		elif key[0].lower() == 'exit':	 
			break;
		else:
			print("input a wrong cmd.")
			
dictionary_run()
