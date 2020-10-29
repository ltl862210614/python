#! python3
#encoding:utf-8

coders = ['sbA','sbB','sbC','sbD','sbE']

for coder in coders:
	print(coder)
print("\n")
	
#1) 数值列表
for value in range(1,5):	#不包括5
	print(value)
print("\n")
	
numbers = list(range(1,6))
print(numbers)
print("\n")

even_nums = list(range(1,15,2))
print(even_nums)
print("\n")

squares = []

for value in range(1,6):
	square = value**2
	squares.append(square)
	print(squares)
print("\n")

#2) 数值列表计算
print("min:%d"%(min(squares)))	
print("max:%d"%(max(squares)))	
print("sum:%d"%(sum(squares)))	

# 3)列表解析
numbers = [value**3 for value in range(1,6)]
print(numbers)

# 4)切片
print(numbers[0:3])
print(numbers[:3])
print(numbers[3:])
print(numbers[-2:])

for num in numbers[:-2]:
	print(num)

# 5) 列表复制	
numbers2 = numbers[:]	#numbers2 = numbers, 则numbers,numbers2未同一个列表
numbers2.append(66)
print(numbers)
print(numbers2)

# 6) 元组 
demo_tuple = (1,2,5,4,8,11,7,6)
print(demo_tuple)

for member_tuple in demo_tuple:
	print(member_tuple)

#不可单独修改元素值
#demo_tuple[0] = 2	#报错	

#修改元组变量
demo_tuple = (2,4,6,8,10,12)
print(demo_tuple)
	
	