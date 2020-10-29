#! python3
#encoding:utf-8

def myInput():
	age = input("enter your age:")	#Python将输入解读成了字符串  
	if int(age) < 18:	#函数int()将数字的字符串表示转换为数值
		print("you are still a kid")
	else:
		print("you have been an adult")

def myWhile():
	prompt = "\nPlease enter the city you have visited:"
	prompt += "\n(Enter 'quit' when you are finished.)"
	
	flag = True
	while flag:
		city = input(prompt)
		
		if city.lower() == 'quit':
			break
		elif city.title() == 'Wuhan':
			print("you don't want to %s"%city.title())
			continue
		print("I have gone to %s!"%city.title())

def myList():
	unconfirmed_users = ['tom','mary','jacky','jerry']
	confirmed_users = []
	
	while unconfirmed_users:
		current_user = unconfirmed_users.pop()
		print("verifying user:"+current_user.title())
		confirmed_users.append(current_user)
		
	print("\nThe following users have been confirmed:")
	for confirmed_user in confirmed_users:
		print(confirmed_user.title())
		
	print(confirmed_users)
	confirmed_users.remove(confirmed_users[0])	#删除列表中的特定值
	print(confirmed_users)

	del confirmed_users[-1]		#删除列表中的特定值
	print(confirmed_users)
	
	confirmed_users.pop(-1)		
	print(confirmed_users)
		
myInput()
#myWhile()
myList()