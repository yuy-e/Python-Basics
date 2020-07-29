#chapter7
#------------------------------------------------------------------------#
height = input("How tall are you, in inches?")
height = int(height)

if height >= 36:
	print("\nYou are tall enough to ride!")
else:
	print("\nYou will be able to ride when you are a litter older.")
#------------------------------------------------------------------------#
#7-1
car = input("What kind of car would you like to rent?")
print("Let me see if I can find you a "+ car.title() +".")
#7-2
number = input("How many guests will coming?")
number = int(number)
if number > 8:
	print("Sorry, we don't have available table.")
else:
	print("Welcome, we still have available tables.")
#7-3
value = input("Please enter a number.")
value = int(value)
if value % 10 == 0:
	print("The number is a multiple of 10.")
else:
	print("The number is not a multiple of 10.")
#------------------------------------------------------------------------#
#让用户选择何时退出
prompt = "\nTell me something, I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)
#------------------------------------------------------------------------#
#使用标志active
prompt = "\nTell me something, I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
active = True
while active == True:
	message = input(prompt)
#	print(message) 此时print(message)，quit仍然输出一次后退出程序。
	if message == 'quit':
		active = False
	else:
		print(message)
#------------------------------------------------------------------------#
#break
prompt = '\nPlease enter the name of a city you have visited.'
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to "+city.title()+"!")
#------------------------------------------------------------------------#	
#continue
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)
#------------------------------------------------------------------------#
#7-4
#Method1
prompt = "\nPlease enter the toppings you need."
prompt += "\n(Enter 'quit' when you are finished.)"
active = True
while active == True:
	toppings = input(prompt)
	if toppings == 'quit':
		active = False
	else:
		print("We will add "+toppings+" in your pizza.")
#Method2
prompt = "\nPlease enter the toppings you need."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	toppings = input(prompt)
	if toppings == 'quit':
		break
	else:
		print("We will add "+toppings+" in your pizza.")

#7-5
#Method1
prompt = "\nPlease enter your age: "
prompt += "\n(Enter 'quit' when you are finished.)"
active = True
while active == True:
	age = input(prompt)
	if age == 'quit':
		active = False
	elif int(age) <= 3:
		price = 0
		print("Free.")
	elif int(age)>3 and int(age)<=12:
		price = 10
		print("You need to pay 10 dollars for a ticket.")
	else:
		price = 15
		print("You need to pay 15 dollars for a ticket.")	
#Method2
prompt = "\nPlease enter your age: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)
	if age < 3:
		print("You get in free!")
	elif age < 13:
		print("Your ticket is $10.")
	else:
		print("Your ticket is $15.")

#7-6见7-4/7-5Method
#7-7
prompt = "\nThis is an circle without ending."
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
	circle = input(prompt)
	print(circle)

#------------------------------------------------------------------------#
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


pets = ['dog','cat','dog','giraffe','cat','elephant','rabbit']
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#------------------------------------------------------------------------#
responses = {}

polling_active = True
while polling_active == True:
	name = input("\nWhat is your name?")
	response = input("\nWhich mountain would you like to climb someday?")

	responses[name] = response #将问卷存储在字典中

	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

print("\n----Poll Results ----")
for name, response in responses.items():
	print(name + "would like to climb " + response + ".")
#------------------------------------------------------------------------#
#7-8
sandwich_orders = ['tuna','veggie','grilled cheese','turkey','roast beef']
finished_sandwiches = []
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I made your " + current_sandwich + " sandwich.")
	finished_sandwiches.append(current_sandwich)
print("\nI have made all the sandwiches: ")
for sandwich in finished_sandwiches:
	print("\t" + sandwich.title())
#7-9
sandwich_orders = ['tuna','veggie','pastrami','grilled cheese','pastrami','turkey','roast beef','pastrami']
print("I'm sorry, we are all out of pastrami today.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)
#7-10
places = {}

while True:
	name = input("\nWhat is your name?")
	place = input("\nIf you could visit one place in the world, where would you go?")
	response = input("\nWould you like to to let another person respond? (yes/no) ")
	places[name] = place #将问卷存储在字典中
	if response == 'no':
		break
print("\n----Poll Results ----")
for name, place in places.items():
	print(name.title() + ":" + place.title())
#------------------------------------------------------------------------#





