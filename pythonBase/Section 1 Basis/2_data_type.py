#! python3
#encoding:utf-8

'''
#1)修改字符串
first_name = 'hello'
last_name = "python"
full_name = first_name + ' ' + last_name

print(full_name)
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(full_name)	#不会改变原变量
'''

'''
#2)删除空白
del_blank = ' hello python '
print(del_blank.rstrip())	#删除字符串末尾空白
print(del_blank.lstrip())	#删除字符串开头空白
print(del_blank.strip())	#删除字符串两端空白
'''

#3)类型转换str
money = 2.2
deposit = "I have " + str(money) + " dollars"
print(deposit)
