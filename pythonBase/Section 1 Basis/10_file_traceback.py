#! python3
#encoding:utf-8

'''
关键字with 在不再需要访问文件后会在合适的时候自动将其关闭。在下面程序中，调用了open() ，但没有调用close()，路径用'/' 
相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。因为read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。
要删除多出来的空行，可在print 语句中使用rstrip()删除（剥除）字符串末尾的空白：
'''
#with open('testfile/test.txt') as file_object:
#with open('E:/WorkSpace/python/tease.py','rb') as file_object:	#绝对路径
#with open('../tianqi.py','r',encoding='utf-8') as file_object:	#相对路径
#with open('testfile/pi_digits.txt') as file_object:

'''
with open('10 file_traceback.py',encoding='utf-8') as file_object:
	#读取整个文件
	contents = file_object.read()
	print(contents.rstrip())
'''
'''
with open('10 file_traceback.py',encoding='utf-8') as file_object:	
	#逐行读取
	for line in file_object:
		print(line.rstrip())
'''	
'''使用文件内容'''	
with open('testfile/pi_million_digits.txt',encoding='utf-8') as file_object:
	'''创建一个包含文件各行内容的列表'''
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()	#去掉前后空格
print(pi_string[:50]+"...")
print("pi length:"+str(len(pi_string)))

birthday = ''#input("Input your birthday:")
ret = pi_string.find(birthday)
if ret:
#if birthday in pi_string:
	print("your birthday is in the first million digists of pi[%d]."%ret)
else: 
	print("your birthday isn't in the first million digists of pi.")
	
'''写入文件'''
'''
读取取模模式式 （'r' ）、写写入入模模式式 （'w' ）、附附加加模模式式 （'a' ）或让你能够读取和写入文件的模式('r+' )
以写入（'w' ）模式打开文件时，如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
'''
filename = "testfile/writetest.txt"
with open(filename,'w') as file_object:
	file_object.write("hello world.\n")
	
	
	
print("\n###################################################################\n")
'''异常'''
print("input two numbers and divide them.")
print("input 'q' to quit.\n")

while True:
	first_num = input("Enter first num:")
	if first_num == 'q':
		break
	second_num = input("Enter second num:")
	if second_num == 'q':
		break
	try:
		#可能引发异常的代码
		answer = int(first_num) / int(second_num)
	except ZeroDivisionError:
		#引发异常处理
		print("You cann't divide by zero.")
	except ValueError:
		print("please input a number.")
	else:
		#try成功执行的处理
		print(answer)
		
'''处理FileNotFoundError 异常'''
filepath = "testfile/"
filename = "Alice's Adventures in Wonderland.txt"

def count_words(filename):
	words_sum = 0
	try:
		with open(filename) as file_obj:
			content = file_obj.read()
	except FileNotFoundError:
		print("the file '"+filename+"' doesn't exit.")
		pass	#充当占位符，不做任何操作
	else:
		#print(content)
		print("the 'hello' appears "+str(content.lower().count('hello'))+" times.")
		words = content.split()
		words_sum = len(words)
		print("The file '"+filename+"' has about "+str(words_sum)+" words.")
	return words_sum
		
count_words(filepath+filename)

file_names = ['test.txt','writetest.txt','haha.txt']
for filename in file_names:
	count_words(filepath+filename)
	

	
	


