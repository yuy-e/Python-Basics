#chapter10

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#------------------------------------------------------------------------#
print("")
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.strip())
#------------------------------------------------------------------------#
print("")#with模块外仍可使用
filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.strip())
#------------------------------------------------------------------------#
print("")
filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))
#------------------------------------------------------------------------#
print("")
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))
#------------------------------------------------------------------------#

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")

#------------------------------------------------------------------------#
#10-1
filename = 'learning_python.txt'
with open(filename) as file_object:
	contents = file_object.read()
	print(contents.strip())

print("")
filename = 'learning_python.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.strip())

print("")
filename = 'learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())

#10-2
print("")
filename = 'learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.replace('Python', 'C++').strip())
#------------------------------------------------------------------------#

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
#------------------------------------------------------------------------#

#10-3
filename = 'guests.txt'
with open(filename,'w') as file_object:
	name = input("Enter your name.")
	file_object.write(name)

#10-4
filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
	while True:
		print("\nEnter 'q' to exit at any time.")
		name = input("Enter your name.")
		if name == 'q':
			break
		else:
			print("Welcome, " + name + '!')
			file_object.write(name + "\n")

#10-5
#Method1
filename = 'love_programming_reason.txt'

with open(filename, 'w') as file_object:
	while True:
		print("\nEnter 'q' to exit at any time.")
		reason = input("\nWhy you love programming?")
		if reason == 'q':
			break
		else:
			file_object.write(reason+"\n")

#Method2
filename = 'love_programming_reason.txt'
reasons = []
while True:
	reason = input("\nWhy you love programming?")
	reasons.append(reason)
	continue_poll = input("Would you like to let someone else respond? (y/n)")
	if continue_poll == 'n':
		break

with open(filename, 'w') as file_object:
	for reason in reasons:
		file_object.write(reason + "\n")
#------------------------------------------------------------------------#
try:
	print(5/2)
except ZeroDivisionError:
	print("You can't divide by zero!")

#------------------------------------------------------------------------#
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while  True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break

	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You cannot divide by 0!")
	else:
		print(answer)
#------------------------------------------------------------------------#

filename = 'alice.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exit."
	print(msg)
else:
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")
#------------------------------------------------------------------------#
def count_words(filename):
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exit."
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)
#------------------------------------------------------------------------#
#10-6 + 10-7
while True:
	print("Enter 'q' to quit.")
	number_1 = input("\nEnter first number.")
	if number_1 != 'q':
		try:
			a = int(number_1)
		except ValueError:
			print("You should enter a number.")
		else:
			number_2 = input("\nEnter second number.")
			if number_2 != 'q':
				try:
					b = int(number_2)
				except ValueError:
					print("You should enter a number.")
				else:
					c = a + b
					print("The sum of the two number is: " + str(c))
			else:
				break
	else:
		break

#10-8
filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'

with open(filename_1, 'w') as fl_object_1:
	fl_object_1.write('henry\n') #一次只能写入一个数据
	fl_object_1.write('coco\n')
	fl_object_1.write('mildred\n')
with open(filename_2, 'w') as fl_object_2:
	fl_object_2.write('willie\n') 
	fl_object_2.write('annahootz\n') 
	fl_object_2.write('summit\n') 

try:
	with open(filename_1) as fl_object_1:
		contents = fl_object_1.read()
except FileNotFoundError:
	print("Sorry, I can't find the file.")
else:
	print(contents)
	try:
		with open(filename_2) as fl_object_2:
			contents = fl_object_2.read()
	except FileNotFoundError:
		print("Sorry, I can't find the file.")
	else:
		print(contents)

#10-9
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
    	print(contents)

#10-10
filename = 'alice.txt'
with open(filename) as file_object:
	contents = file_object.read()
	num_the = contents.lower().count('the')
	print(num_the)
#------------------------------------------------------------------------#

import json

filename = 'username.json'

try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")
#------------------------------------------------------------------------#
import json

def greet_user():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

greet_user()

#------------------------------------------------------------------------#
#重构

import json

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	username = get_stored_username()
	if username:
		print("Welcome back, "+username+"!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, "+username+"!")

greet_user()

#------------------------------------------------------------------------#
#10-11
import json
favourite_number = input("What is your favourite number?")

filename = 'favourite_number.json'
with open(filename, 'w') as f_obj:
	json.dump(favourite_number, f_obj)


with open(filename) as f_obj:
	number = json.load(f_obj)
	print("\nI know your favourite number! It's "+number+" .")

#10-12
import json

filename = 'favourite_number.json'
try: 
	with open(filename) as f_obj:
		number = json.load(f_obj)

except FileNotFoundError:
	favourite_number = input("What is your favourite number?")
	with open(filename, 'w') as f_obj:
		json.dump(favourite_number, f_obj)
else:
	print("\nI know your favourite number! It's "+number+" .")

#------------------------------------------------------------------------#

#10-13
import json

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input("What is your name?")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj) 
	return username

def greet_user():
	username = get_stored_username()
	
	if username:
		msg = input("\nIs your username: "+username+"? (y/n)")
		if msg == 'y':
			print("Welcome back, " + username + " !")
		else:
			username = get_new_username()
			print("We will remember you when you come back, " + username + " !")
	else:
		username = get_new_username()
		print("We will remember you when you come back, " + username + " !")

greet_user()
#------------------------------------------------------------------------#
# 简化greet_user内部重复代码 return
def greet_user():
	username = get_stored_username()
	
	if username:
		msg = input("\nIs your username: "+username+"? (y/n)")
		if msg == 'y':
			print("Welcome back, " + username + " !")
			return #仅当if语句成功时返回 welcome back语句

		username = get_new_username() #if语句fail, 运行get_new_username
		print("We will remember you when you come back, " + username + " !")

greet_user()

#------------------------------------------------------------------------#

