# -*- coding: utf-8 -*-
 
class jsonFormat(object):
	def __init__(self, input):
		self.returnJsonStr = ''
		self.json = input
		self.handleJson()
		self.makeJsonStr()
 
	def handleJson(self):
		"处理原始json"
		self.returnJsonStr = self.returnJsonStr + '{' + '\n'
		for key, value in self.json.items():
			self.judgeValueType(value, key)
		self.returnJsonStr = self.returnJsonStr + '}' + '\n'
 
	def judgeValueType(self, value, key=None):
		"判断value类型"
		if type(value) == list:  # 数组
			self.handleArray(value, key)
		elif type(value) == dict:  # 对象
			self.handleDict(value, key)
		elif type(value) == str:  # 字符串
			if key == None:
				self.returnJsonStr = self.returnJsonStr + '"' + value + '"' + '\n'
			else:
				self.returnJsonStr = self.returnJsonStr + '"' + key + '":' + '"' + value + '"' + '\n'
		elif value == None:  # 空值
			self.returnJsonStr = self.returnJsonStr + '"' + key + '":' + '""' + '\n'
		else:
			if key == None:
				self.returnJsonStr = self.returnJsonStr + str(value) + '\n'
			else:
				self.returnJsonStr = self.returnJsonStr + '"' + key + '":' + str(value) + '\n'
 
 
	def handleArray(self, array, key=None):
		"处理数组"
		self.returnJsonStr = self.returnJsonStr + '"' + key + '":' + '['
		for item in array:
			self.judgeValueType(item)
		self.returnJsonStr = self.returnJsonStr[0:-1] + ']' + '\n'
 
	def handleDict(self, dict, key=None):
		"处理对象"
		if key != None:
			self.returnJsonStr = self.returnJsonStr + '"' + key + '":' + '{' + '\n'
		else:
			self.returnJsonStr = self.returnJsonStr + '{' + '\n'
		for key, value in dict.items():
			self.judgeValueType(value, key)
		self.returnJsonStr = self.returnJsonStr + '}' + '\n'
 
	def makeJsonStr(self):
		"生成json字符串"
		jsonStr = self.returnJsonStr
		jsonArray = jsonStr.split('\n')
		jsonStr = ''
		for i in range((len(jsonArray)-1)):
			if '{' in jsonArray[i]:
				jsonStr = jsonStr + jsonArray[i] + '' + '\n'
			elif '}' in jsonArray[i+1]:
				jsonStr = jsonStr + jsonArray[i] + '' + '\n'
			else:
				jsonStr = jsonStr + jsonArray[i] + ',' + '\n'
		# print jsonStr
 
		jsonArray = jsonStr.split('\n')
		jsonStr = ''
		x = 0
		for arr in jsonArray:
			tabs = ''
			for j in range(x):
				tabs = tabs + '\t'
			if '{' in arr or '[' in arr:
				jsonStr = jsonStr + tabs + arr + '\n'
				x = x + 1
			elif '}' in arr or ']' in arr:
				jsonStr = jsonStr + tabs[0:-1] + arr + '\n'
				x = x - 1
			else:
				jsonStr = jsonStr + tabs + arr + '\n'
 
		self.returnJsonStr = jsonStr[0:-3]
 
input = {'a':'a', 'b':'b', 'c':{'d':'d', 'e':'e', 'f':{'g':'g', 'h':'h'}, 'y':'y', 'items':[{'11':'11', '12':{'111':'111','112':112}, '13':'13'},{'21':'21', '22':{'211':'211','212':'212'}, '23':'23'}]}, 'x':'x'}
a = jsonFormat(input)
print(a.returnJsonStr)