#! python3
#import sys

'''
编写函数时，可给每个形参指定默认值 。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。
使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。
'''
def describe_pet(pet_name,pet_type="cat"):
#def describe_pet(pet_type,pet_name):
	print("\nI have a %s."%pet_type)
	print("my %s's name is %s"%(pet_type,pet_name))

'''
位置实参: 调用函数时，基于实参的顺序,将函数调用中的每个实参都关联到函数定义中的一个形参。
'''	
describe_pet("cat","Tom")
'''
关键字实参: 是传递给函数的名称—值对。在实参中将名称和值关联起来，向函数传递实参时不会混淆。
关键字实参无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
'''
describe_pet(pet_type="cat",pet_name="Tom")
describe_pet(pet_name="Tom",pet_type="cat")

describe_pet(pet_name="Tom")
describe_pet("Tom")

lst=[1,2,3,4]
print(lst)	#[1, 2, 3, 4]
lst1=lst
lst1.pop()
print(lst)	#[1, 2, 3]

#切片表示法[:] 创建列表的副本
lst[:].pop()
print(lst)	#[1, 2, 3]
'''
虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创
建副本，从而提高效率，在处理大型列表时尤其如此。
'''
print("\n###################################################################")
magicians_list = ['Wind','Rain','Thunder','Lightnig']
greatMagicians_list = []

def show_list(magiciansList):
	print(magiciansList)
	
def show_magicians(magiciansList):
	for magician in magiciansList:
		print(magician)
		
def make_great(magiciansList,greatMagiciansList):
	while magiciansList:
		magician = "the Great " + magiciansList.pop(0)
		greatMagiciansList.append(magician)

show_list(magicians_list)		
make_great(magicians_list[:],greatMagicians_list)	#传递列表副本不修改列表原件
show_magicians(greatMagicians_list)
show_list(magicians_list)

print("\n###################################################################")
print("传递任意数量实参:\n")
#形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收到的所有值都封装到这个元组中。
def show_courses(*courses):
	print(courses)
	print("len=%d"%len(courses))
	for course in courses:
		print(course)
	print("\n")
		
show_courses("Chinese","Mathematics","Physical","Chemistry","Biology")
show_courses("English")

print("\n###################################################################")
print("使用任意数量的关键字实参:\n")
#将函数编写成能够接受任意数量的键—值对
def build_profile(firstName,lastName,**userInfo):
	profile = {}
	
	profile['firstName'] = firstName.title()
	profile['lastName'] = lastName.title()
	for key,value in userInfo.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)



