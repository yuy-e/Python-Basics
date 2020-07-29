#chapter9
'''
现在网络上有很多关于面向过程和面向对象区别的文档，都总结的很好，总结如下
1面向过程在解决问题的时候，会分析出解决问题的步骤，然后用函数一步步的将这些步骤实现，依次调用函数。而面向对象在解决问题的时候，会将问题拆散成一个个对象，建立对象的目的不是为了完成某个步骤，而是为了描述某个事物在整个解决问题的步骤中的行为。这来自于思考问题方式的不同。
2从结构上说，面向过程的特点是过程化和模块化，而面向对象的特点则是类封装、继承和多态（多态：同一操作作用于不同的对象，可以有不同的解释，产生不同的执行结果。在运行时，可以通过指向基类的指针，来调用实现派生类中的方法）。
3执行效率不同，面向过程不需要封装类再实例化对象调用，只定义了函数和调用，所以执行效率会更高一些。
总的来说，面向过程执行效率更高也更直接，面向过程更灵活也更丰满。
'''
#9-1
class Restaurant():
	def __init__(self, restaurant_name, restaurant_type):
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type

	def describe_restaurant(self):
		print("\nThe restaurant name is " + self.restaurant_name + ".")
		print("The type of the restaurant is " + self.restaurant_type + ".")

	def open_restaurant(self):
		print("The restaurant is opening.")

restaurant = Restaurant('the mean queen', 'pizza')
print("restaurant's name is " + restaurant.restaurant_name.title() + ".")
print("restaurant's type is " + restaurant.restaurant_type.title() + ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()
#9-2
mean_queen = Restaurant('the mean queen','pizza')
mean_queen.describe_restaurant()
ludvigs = Restaurant("ludvig's bostro",'seafood')
ludvigs.describe_restaurant()
mango_thai = Restaurant('mango thai','thai food')
mango_thai.describe_restaurant()
#9-3
class User():
	def __init__(self, first_name, last_name, gender, username, email):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.username = username
		self.email = email
		self.full_name = self.first_name+" "+self.last_name
	def describe_user(self):
		print("\nThe user's name is "+self.full_name.title()+".")
		print("\tUser's gender: "+self.gender)
		print("\tUser's username: "+self.username)
		print("\tUser's email: "+self.email)
	def greet_user(self):
		print("\nHello, " + self.full_name.title() + "!")

user_1 = User('yue','yu','female','yueyue','111222333@qq.email')
user_1.describe_user()
user_1.greet_user()
#------------------------------------------------------------------------#
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	#通过update_odometer方法更新属性
	def update_odometer(self, mileage):
		self.odometer_reading = mileage

	#通过increment_odometer方法递增属性
	def increment_odometer(self, miles):
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You cannot roll back on odometer!")

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#直接更新属性值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#通过update_odometer方法更新属性
my_new_car.update_odometer(18)
my_new_car.read_odometer()

#通过increment_odometer方法递增属性
my_new_car.increment_odometer(66)
my_new_car.read_odometer()
#------------------------------------------------------------------------#
#9-4
class Restaurant():
	def __init__(self, restaurant_name, restaurant_type):
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		self.number_served = 0

	def describe_restaurant(self):
		print("\nThe restaurant name is " + self.restaurant_name.title() + ".")
		print("The type of the restaurant is " + self.restaurant_type.title() + ".")
		print("The restaurant has served " + str(self.number_served) + " customers.")

	def open_restaurant(self):
		print("The restaurant is opening.")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.open_restaurant()
restaurant.set_number_served(23)
restaurant.increment_number_served(55)
restaurant.describe_restaurant()
#9-5
class User():
	def __init__(self, first_name, last_name, gender, username, email):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.username = username
		self.email = email
		self.full_name = self.first_name+" "+self.last_name

		self.login_attempts = 0
	def describe_user(self):
		print("\nThe user's name is "+self.full_name.title()+".")
		print("\tUser's gender: "+self.gender)
		print("\tUser's username: "+self.username)
		print("\tUser's email: "+self.email)
	def greet_user(self):
		print("\nHello, " + self.full_name.title() + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print("User's attempts to log in: " + str(self.login_attempts))

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("User's attempts to log in have been reset: 0 .")

user_1 = User('yue','yu','female','yueyue','111222333@qq.email')
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
#------------------------------------------------------------------------#
'''父类Car'''
#------------------------------------------------------------------------#
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	#通过update_odometer方法更新属性
	def update_odometer(self, mileage):
		self.odometer_reading = mileage

	#通过increment_odometer方法递增属性
	def increment_odometer(self, miles):
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You cannot roll back on odometer!")
#------------------------------------------------------------------------#
'''Battery类 + 子类Electriccar'''
#------------------------------------------------------------------------#
	
class Battery:
	def __init__(self, battery_size = 70): #初始化，设置默认值
		self.battery_size = battery_size
	def describe_battery(self):
		print("\nThis car has a "+str(self.battery_size)+" -kWh battery.")
	def get_range(self): #扩展方法
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		print("\nThis car can go approximately " + str(range) + " miles on a full charge.")

class ElectricCar(Car): #继承父类属性+方法
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery() #子类特殊属性

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
#------------------------------------------------------------------------#
#9-6
class Restaurant():
	def __init__(self, restaurant_name, restaurant_type):
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type

	def describe_restaurant(self):
		print("\nThe restaurant name is " + self.restaurant_name + ".")
		print("The type of the restaurant is " + self.restaurant_type + ".")

	def open_restaurant(self):
		print("The restaurant is opening.")

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, restaurant_type):
		super().__init__(restaurant_name, restaurant_type)
		self.flavors = []
	def show_icecream(self):
		print("\nWe have different flavors of icecream: ")
		for flavor in self.flavors:
			print("\t" + flavor)

my_icecreamstand = IceCreamStand('dairy queen','icecream')
my_icecreamstand.flavors = ['vanilla','matcha','strawberry']
my_icecreamstand.describe_restaurant()
my_icecreamstand.open_restaurant()
my_icecreamstand.show_icecream()
#9-7
class User():
	def __init__(self, first_name, last_name, gender, username, email):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.username = username
		self.email = email
		self.full_name = self.first_name+" "+self.last_name

		self.login_attempts = 0
	def describe_user(self):
		print("\nThe user's name is "+self.full_name.title()+".")
		print("\tUser's gender: "+self.gender)
		print("\tUser's username: "+self.username)
		print("\tUser's email: "+self.email)
	def greet_user(self):
		print("\nHello, " + self.full_name.title() + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print("User's attempts to log in: " + str(self.login_attempts))

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("User's attempts to log in have been reset: 0 .")

class Admin(User):
	def __init__(self, first_name, last_name, gender, username, email):
		super().__init__(first_name, last_name, gender, username, email)
		self.privileges = []
	def show_privileges(self):
		print("\nThe user's privileges include: ")
		for privilege in self.privileges:
			print("\t"+privilege)
myself = Admin('yue','yu','female','yueyue','111222333@qq.com')
myself.privileges = ['can add post','can delete post','can ban post']
myself.describe_user()
myself.show_privileges()

#9-8
class User():
	def __init__(self, first_name, last_name, gender, username, email):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.username = username
		self.email = email
		self.full_name = self.first_name+" "+self.last_name

		self.login_attempts = 0
	def describe_user(self):
		print("\nThe user's name is "+self.full_name.title()+".")
		print("\tUser's gender: "+self.gender)
		print("\tUser's username: "+self.username)
		print("\tUser's email: "+self.email)
	def greet_user(self):
		print("\nHello, " + self.full_name.title() + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print("User's attempts to log in: " + str(self.login_attempts))

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("User's attempts to log in have been reset: 0 .")

class Privileges():
	def __init__(self, privileges = []):
		self.privileges = privileges

	def show_privileges(self):
		print("\nThe user's privileges include: ")
		for privilege in self.privileges:
			print("\t"+privilege)

class Admin(User):
	def __init__(self, first_name, last_name, gender, username, email):
		super().__init__(first_name, last_name, gender, username, email)
		self.privileges = Privileges()

myself = Admin('yue','yu','female','yueyue','111222333@qq.com')
privileges = ['can add post','can delete post','can ban post']
myself.describe_user()
myself.privileges.privileges = privileges #实例的privileges属性 = Privileges类的previliges属性
myself.privileges.show_privileges()
#9-9
class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	#通过update_odometer方法更新属性
	def update_odometer(self, mileage):
		self.odometer_reading = mileage

	#通过increment_odometer方法递增属性
	def increment_odometer(self, miles):
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You cannot roll back on odometer!")
	
class Battery:
	def __init__(self, battery_size = 70): #初始化，设置默认值
		self.battery_size = battery_size
	def describe_battery(self):
		print("\nThis car has a "+str(self.battery_size)+" -kWh battery.")
	def get_range(self): #扩展方法
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		print("\nThis car can go approximately " + str(range) + " miles on a full charge.")

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85

class ElectricCar(Car): #继承父类属性+方法
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery() #子类特殊属性

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
#------------------------------------------------------------------------#
#9-13 使用OderedDict
#-------------------------------- 6-4 -----------------------------------#
'''
vocabularies = {
	'string': 'a series of characters.',
	'comment': 'a note in a program that the Python interpreter ignores.',
	'list': 'a collection of iems in a particular order.',
	'dictionary': 'a collection of key-value pairs.',
	'loop': 'work through a collection of items, one at a time.',
}
for key, value in vocabularies.items():
	print(key+':'+value)
print("\n")
vocabularies['del'] = 'delete'
vocabularies['key'] = 'the first item in a key-value pair in a dictionary.'
vocabularies['value'] = 'an item associated with a key in a dictionary.'
vocabularies['conditionary test'] = 'a conparison between two values.'
vocabularies['float'] = 'a numerical value with a decimal compoent.'
vocabularies['boolean expression'] = 'an expression that evaluate to True or False.'
for word, definition in vocabularies.items():
	print(word.title() + ':' + definition)
'''
#-------------------------------- 9-13 -----------------------------------#
from collections import OrderedDict
vocabularies = OrderedDict()

vocabularies['del'] = 'delete'
vocabularies['key'] = 'the first item in a key-value pair in a dictionary.'
vocabularies['value'] = 'an item associated with a key in a dictionary.'
vocabularies['conditionary test'] = 'a conparison between two values.'
vocabularies['float'] = 'a numerical value with a decimal compoent.'
vocabularies['boolean expression'] = 'an expression that evaluate to True or False.'

for word, definition in vocabularies.items():
	print("\t" + word.title() + ':' + definition)
#9-14
from random import randint

class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		self.x = randint(1, self.sides)
		return self.x      #必须return才能将值保存在result中

#6面骰子掷10次
test = Die()
results = []

for i in range(10):       #range(1,10):1-9 but range(10):0-9
	result = test.roll_die()
	results.append(result)
print(results)

#10面骰子掷10次
test = Die(10)
results = []
for i in range(10):
	result = test.roll_die()
	results.append(result)
print(results)

#20面骰子掷10次
test = Die(20)
results = []
for i in range(10):
	result = test.roll_die()
	results.append(result)
print(results)




