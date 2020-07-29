#chapter 8
#------------------------------------------------------------------------#
#8-1
def display_message():
	print("We will learn how to write functions.")
display_message()
#8-2
def favourite_book(title):
	print("\nOne of my favourite_books is "+title+".")
favourite_book('Alice in Wonderland')
#8-3
def make_shirt(size, pattern):
	print("\nThe size of T-shirt is " + size.title() + ".")
	print("\nThe pattern of T-shirt is: '" + pattern + "' .")
make_shirt('m', 'Hi!')
#8-4
def make_shirt(size, pattern = 'I love Python'):
	print("\nThe size of T-shirt is " + size.title() + ".")
	print("The pattern of T-shirt is: '" + pattern + "' .")
make_shirt('l')
make_shirt('m')
make_shirt('s','I love China!')
#8-5
def describe_city(name, country = 'china'):
	print("\n" + name.title() + " is in " + country.title() + ".")
describe_city('hefei')
describe_city('tokyo', 'japan')
describe_city('beijing')
#------------------------------------------------------------------------#
def get_formatted_name(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()
fairy = get_formatted_name('yue', 'yu')
print(fairy)
student = get_formatted_name('lu', 'wang', 'ge')
print(student)
#------------------------------------------------------------------------#
#返回字典
def build_person(first_name, last_name, age = ''): #默认age为空字符串
	person ={
	'first':first_name,
	'last':last_name,
	}
	if age:
		person['age'] = age
	return person
fairy = build_person('yue','yu',age = 21)
print(fairy)
#------------------------------------------------------------------------#
#交互：用户输入，返回姓名

def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
print("\nPlease tell me your name.")
print("\nEnter 'q' at any time to quit.")
while True:
	f_name = input("\nFirst name: ")
	if f_name == 'q':
		break
	l_name = input("\nLast name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")

#------------------------------------------------------------------------#
#8-6
def city_country(city, country):
	print("\n" + city.title() + ", " + country.title())
city_country('santiago', 'chile')
city_country('tokyo', 'japan')
city_country('hefei', 'china')
#8-7
def make_album(singer, album_name, song_number = ''):
	album_info = { 
		'singer': singer,
		'album_name': album_name,
	}
	if song_number:
		album_info['song_number'] = song_number
	return album_info
album = make_album('kevin penkin', 'florence')
print(album)
album = make_album('damien rice', 'o')
print(album)
album = make_album('lover boy 88', 'head in the clouds', 13)
print(album)
#8-8
def make_album(singer, album_name, song_number = ''):
	album_info = {'singer':singer, 'album_name':album_name}
	if song_number:
		album_info['song_number'] = song_number
	return album_info
print("\nEnter 'q' at any time to quit.")
while True:
	singer = input("\nPlease enter a singer name.")
	if singer == 'q':
		break
	album_name = input("\nPlease enter one of he/she 's albums's name.")
	if album_name =='q':
		break
	prompt = "\nPlease enter the number of songs in the album."
	prompt += "\nEnter 0 if you don't know the songs' numbers."
	song_number = input(prompt)
	if song_number == 'q':
		break
	album_info = make_album(singer.title(), album_name.title(), song_number)
	print(album_info)
#------------------------------------------------------------------------#
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#切片表示法[:]创建列表的副本，不改变unprinted_designs原列表
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
#------------------------------------------------------------------------#
#8-9
def show_magicians(magicians):
	for magician in magicians:
		print(magician)

magicians = ['david copperfield', 'harry houdni', 'criss angel', 'david blaine']
show_magicians(magicians)
#8-10
def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(unrevised_magicians, completed_magicians):
	while unrevised_magicians:
		current_magician = unrevised_magicians.pop()
		current_magician = 'the Great ' + current_magician.title()
		completed_magicians.append(current_magician)

unrevised_magicians = ['david copperfield', 'harry houdni', 'criss angel', 'david blaine']
completed_magicians = []
make_great(unrevised_magicians, completed_magicians)
show_magicians(completed_magicians)
print(unrevised_magicians)
#8-11
def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(unrevised_magicians, completed_magicians):
	while unrevised_magicians:
		current_magician = unrevised_magicians.pop()
		current_magician = 'the Great ' + current_magician.title()
		completed_magicians.append(current_magician)

unrevised_magicians = ['david copperfield', 'harry houdni', 'criss angel', 'david blaine']
completed_magicians = []
make_great(unrevised_magicians[:], completed_magicians)
show_magicians(completed_magicians)
show_magicians(unrevised_magicians)
#------------------------------------------------------------------------#
#位置实参 + 任意数目实参
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#------------------------------------------------------------------------#
#任意数目的关键字实参
def build_profile(first, last, **user_info):
	profile = {} #创建空字典
	profile['first name'] = first
	profile['last name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert','einstein', location = 'princeton', field = 'physics')
print(user_profile)
#------------------------------------------------------------------------#
#8-12
def make_sandwiches(*ingredients):
	print("\nThe ingredients you want are: ")
	for ingredient in ingredients:
		print("-" + ingredient)
make_sandwiches('mushrooms','extra cheese')
make_sandwiches('pepperoni')
make_sandwiches('greem peppers','pepperoni','extra cheese')
#8-13
def build_profile(first, last, **user_info):
	profile = {}
	profile['first name'] = first
	profile['lase name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('yue','yu',location = 'xian',field = 'machine learning', gender = 'female')
print(user_profile)
#8-14
def make_car(manufacturer,version,**car_info):
	profile = {}
	profile['manufacturer'] = manufacturer
	profile['version'] = version
	for key, value in car_info.items():
		profile[key] = value
	return profile
car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)
#8-15
#printing_function.py
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)
#print_model.py
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#切片表示法[:]创建列表的副本，不改变unprinted_designs原列表
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
#------------------------------------------------------------------------#
