#! python3
#encoding:utf-8

'''Python 2.7中创建类时，需要在括号内包含单词object ：class ClassName(object):'''
class Dog():	
	'''模拟小狗'''
	def __init__(self,name,age):
		'''初始化属性name和age'''
		self.name = name
		self.age = age
		print(name + " is a dog,it is " + str(age) + " years old")
		
	def sit(self):
		'''模拟小狗被命令坐下'''
		print(self.name.title() + " is now sitting")
		
	def roll_over(self):
		'''模拟小狗被命令打滚'''
		print(self.name.title() + " rolled over")

print("\n1、创建和使用类：\n")		
my_dog = Dog('mantou',2)	
print("\n###################################################################\n")


class Car():
	def __init__(self,make,modle,year):
		self.make = make
		self.modle = modle
		self.year = year
		'''给属性指定默认值'''
		self.odometer = 0;
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.modle
		return long_name.title()
		
	def read_odometer(self):
		print("This car has " + str(self.odometer) + " miles on it.")
		return self.odometer
	
	'''通过方法修改属性值'''
	def update_odometer(self,mileage):
		self.odometer = mileage
	
	'''通过方法对属性值进行递增'''
	def increment_odometer(self,miles):
		self.odometer += miles
		
	def gas_tank(self):
		print("This car has a gas tank.")
		
print("\n2、使用类和实例：\n")	
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

'''直接修改属性值'''
my_new_car.odometer = 100
my_new_car.read_odometer()

'''通过方法修改属性值'''
my_new_car.update_odometer(200)
my_new_car.read_odometer()

'''通过方法对属性值进行递增'''
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
print("\n###################################################################\n")


print("\n3、继承：\n")
'''将实例用作属性'''
class Battery():
	def __init__(self,battery_size=70):
		self.battery_size = battery_size
	
	def describle_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		print("This car can go approximately "+str(range)+" miles on a full charge.")
		return range
		
class ElectricCar(Car):
	'''初始化父类属性'''
	def __init__(self,make,modle,year,battery=85):
		'''super()调用父类__init__，将父类与子类关联起来'''
		'''Python 2.7,super(ElectricCar,self),定义父类时在括号内指定object '''
		super().__init__(make,modle,year)
		'''给子类定义属性'''
		self.battery_size = 70
		self.battery = Battery(battery)
	
	'''给子类定义方法'''
	def describle_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	'''重写父类的方法'''
	def gas_tank(self):
		print("The electric car needn't a gas tank.")

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describle_battery()
my_tesla.gas_tank()
my_tesla.battery.describle_battery()
my_tesla.battery.get_range()




		