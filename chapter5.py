#chapter5
#5-1
car ='subaru'
print("Is car = 'subaru'? I predict True.")
print(car=='subaru')

print("\nIs car = 'audi'? I predict False.")
print(car=='audi')
#------------------------------------------------------------------------#
animal = 'giraffe'
print(animal == 'giraffe')
animal='elephant'
print(animal == 'elephant')
animal='fox'
print(animal == 'fox')
animal='cat'
print(animal == 'cat')
animal='dog'
print(animal == 'dog')
animal='rabbit'
print(animal != 'rabbit')
animal='polar bear'
print(animal != 'polar bear')
animal='lion'
print(animal != 'lion')
animal='puma'
print(animal != 'puma')
animal='crocodile'
print(animal != 'crocodile')
#------------------------------------------------------------------------#
#5-2
print('\n')
words_1= 'reminiscence'
words_2= 'quarantine'
print(words_1==words_2)
words_2 = 'REMINISCENCE'
print(words_1==words_2.lower())

number_1=88
number_2=88
if number_1 != number_2:
	if number_1 > number_2:
		print("first number is bigger than the second one.")
	elif number_1 < number_2:
		print("second number is bigger than the first one.")
elif number_1 == number_2:
	print('equal')

number_3=44
number_4=22
if number_3 >= number_4:
	print("number_3>=number_4")
elif number_3 <= number_4:
	print("number_3<=number_4")

numbers = list(range(3,20))
print(numbers)
value = 1188
if value>=3 and value<20:
	for number in numbers:
		if value == number:
			print('the value is in the list.')
elif value<-1 or value>= 100:
	print('the value is out of range.')
else:
	print('the value is not in the lists.')
#------------------------------------------------------------------------#
#5-3
alien_color = ['green','yellow','red']
color = 'green'
if color=='green':
	print('Congratuation! You got 5 points!')

color = 'green'
if color =='green':
	print('Congratuation! You got 5 points!')
#5-4
print('\n')
color = 'red'
if color=='green':
	print('Congratuation! You got 5 points for shoting the green alien!')
if color!='green':
	print('Congratuation! You got 10 point!')

color = 'red'
if color=='green':
	print('Congratuation! You got 5 points for shoting the green alien!')
else:
	print('Congratuation! You got 10 point!')
#5-5
print('\n')
color = 'red'
if color == 'green':
	print('Congratuation! You got 5 points!')
elif color == 'yellow':
	print('Congratuation! You got 10 points!')
else:
	print('Congratuation! You got 15 points!')
#5-6
age = 67
if age>=0 and age<2:
	print('infant')
elif age>=2 and age<4:
	print('toddler')
elif age>=4 and age<13:
	print('child')
elif age>=13 and age<20:
	print('teenager')
elif age>=20 and age<65:
	print('adult')
else:
	print('the aged')
#5-7
favourite_fruits = ['peach','pineapple','strawberry']
if 'peach' in favourite_fruits:
	print("You really like peach!")
if 'banana' in favourite_fruits:
	print("You really like banana!")
if 'pineapple' in favourite_fruits:
	print("You really like pineapple!")
if 'apple' in favourite_fruits:
	print("You really like apple!")
if 'strawberry' in favourite_fruits:
	print("You really like strawberry!")
#------------------------------------------------------------------------#
#  if xxx: 查询列表是否为空
requested_toppings =[]
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding "+requested_topping +".")
	print("\nFinished making your pizza.")
else:
	print("\nAre you sure you want a plain pizza?")
#------------------------------------------------------------------------#
# 使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("\nAdding "+requested_topping+" .")
	else:
		print("\nSorry, we do not have "+requested_topping+" .")
print("\nFinished making your pizza!")
#------------------------------------------------------------------------#
#5-8
users = ['admin','hua tian','luge wang','yue yu','wenxuan wang']
for user in users:
	if user == 'admin':
		print("Hello "+user+", would you like to see a status report?")
	else:
		print("Hello "+user.title()+", thank you for logging in again.")
#5-9
users = []
if users:
	for user in users:
		if user == 'admin':
			print("Hello "+user+", would you like to see a status report?")
		else:
			print("Hello "+user.title()+", thank you for logging in again.")
else:	
	print("\nWe need to find some users!")
#5-10
current_users=['admin','hua tian','luge wang','yue yu','wenxuan wang']
new_users=['aDmin','wenxuan xie','yuyin an','Liping Guo','yuE yu']
for new_user in new_users:
	if new_user.lower() in current_users:
		print("Sorry, the username:"+new_user+" has been used. Please use another username.")
	else:
		print("The username:"+new_user+" has not been used.")
#5-11
numbers =list(range(1,10))
for number in numbers:
	if number==1:
		print("1st")
	elif number==2:
		print("2nd")
	elif number==3:
		print("3rd")
	else:
		print(str(number)+"th")
#------------------------------------------------------------------------#
