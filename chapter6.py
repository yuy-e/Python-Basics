#chapter6
alien={'color':'green','point':5}
print(alien['color'])
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)
#------------------------------------------------------------------------#
alien={}
alien['color'] = 'green'
alien['point'] = 5
print(alien)
alien['point'] = 15
print(alien)
#------------------------------------------------------------------------#
alien={'x_position': 0, 'y_position':5, 'speed':'medium'}
print("Original x_position: "+ str(alien['x_position']))
if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien['x_position'] = alien['x_position'] + x_increment
print("New x_position: "+ str(alien['x_position']))
#------------------------------------------------------------------------#
alien={'x_position':0,'y_position':5,'point':5}
print(alien)
del alien['point']
print(alien)
#------------------------------------------------------------------------#
#6-1
information={
'first_name': 'yue',
'last_name': 'yu',
'age': 21,
'city': 'hefei',
}
print(information['first_name'])
print(information['last_name'])
print(information['age'])
print(information['city'])
#6-2
favourite_numbers={
	'yue yu': 9,
	'hua tian': 3,
	'luge wang': 7,
}
print("yue's favourite number is: " + str(favourite_numbers['yue yu']))
print("hua's favourite number is: "+ str(favourite_numbers['hua tian']))
print("luge's favourite number is: "+ str(favourite_numbers['luge wang']))
#6-3
vocabularies = {
	'del': 'delete',
	'string': 'a series of characters.',
	'comment': 'a note in a program that the Python interpreter ignores.',
	'list': 'a collection of iems in a particular order.',
	'dictionary': 'a collection of key-value pairs.',
	'loop': 'work through a collection of items, one at a time.',
}
print('del:'+vocabularies['del'])
print('string:'+vocabularies['string'])
print('comment:'+vocabularies['comment'])
print('list:'+vocabularies['list'])
print('dictionary:'+vocabularies['dictionary'])
print('loop:'+vocabularies['loop'])
#------------------------------------------------------------------------#

user={
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
}
for key, value in user.items():
	print("\nKey: "+ key)
	print("Value: "+ value)
#------------------------------------------------------------------------#
favourite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
for name in favourite_languages.keys():
	print(name.title())
print('^^^^^^^^^^^^^^^^^')
for name in favourite_languages:
	print(name.title())
print('^^^^^^^^^^^^^^^^^')
for name in favourite_languages:
	print(favourite_languages[name])
for language in favourite_languages.values():
	print(language.title())
#------------------------------------------------------------------------#
friends = ['edward','sarah']
for name in favourite_languages:
	print(name.title())
	if name in friends:
		print("  Hi "+name.title()+", I see your favorite language is "+ favourite_languages[name].title()+"!")
for name in sorted(favourite_languages):
	print(name.title()+", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
	print(language.title())
#------------------------------------------------------------------------#

#6-4
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
#6-5
waters = {
	'nile': 'egypt',
	'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}
for name in waters.keys():
	print(name.title())
for country in waters.values():
	print(country.title())
#6-6
favourite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
lists = ['jen', 'sarah', 'edward','phil','yue yu']
for name in lists:
	if name in favourite_languages.keys():
		print("Thank you for participate into the investigation.")
	else:
		print(name.title()+", would you like to participate into our survey?")

#------------------------------------------------------------------------#
#在列表中存储字典
alien_0={'color':'green','speed':'slow','points':5}
alien_1={'color':'red','speed':'medium','points':10}
alien_2={'color':'yellow','speed':'quick','points':5}

aliens=[]
for alien_number in range(31):
	new_alien = {'color':'green','speed':'slow','points':5}
	aliens.append(new_alien)
for alien in aliens[:3]:
	if alien['color']=='green':
		alien['color']='red'
		alien['points']='10'
		alien['speed']='medium'
for alien in aliens[:5]:
	print(alien)
print("...")
print("The total number of aliens are "+str(alien_number))
#------------------------------------------------------------------------#
#在字典中存储列表 *['python']*即使列表中只有一个元素还是要加[]
favourite_languages = {
	'jen':['python'],
	'sarah':['c','python'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],	
}

for name,languages in favourite_languages.items():
	if len(languages)==1:
		print(name.title()+"'s favourite language is: ")
	else:
		print(name.title()+"'s favourite languages are: ")
	for language in languages:
		print("\t"+language.title())
#------------------------------------------------------------------------#
#在字典中存储字典
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
	},

	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
	},	
}
for username, user_info in users.items():
	full_name = user_info['first']+" "+user_info['last']
	location = user_info['location']
	print("\nUsername: " + username)
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
#-----------------------------------  IMPORTSNT PART  -------------------------------------#

#6-7 
information_0={'first_name': 'yue','last_name': 'yu','age': 21,'city': 'hefei'}
information_1={'first_name': 'hua','last_name': 'tian','age': 22,'city': 'hefei'}
information_2={'first_name': 'luge','last_name': 'wang','age': 20,'city': 'hebei'}
people = [information_0, information_1, information_2]
for person in people:
	print(person)
#6-8
coco = {'dog':'yue yu'}
mimi = {'cat':'luge wang'}
bob = {'rabbit':'hua tian'}
pets = [coco, mimi, bob]
for pet in pets:
	print(pet)
#6-9
favourite_places={
	'yue yu':['hefei','xizang','london'],
	'hua tian':['hefei','xian','new york'],
	'luge wang':['hebei','changsha','tokyo']
}
for name, places in favourite_places.items():
	if len(places) == 1:
		print(name + "'s favourite place is " + places + ".")
	else:
		print(name.title()+"'s favourite places are:")
		for place in places:
			print("\t"+place.title())
#6-10
favourite_numbers={
	'yue yu': 9,
	'hua tian': [3,5],
	'luge wang': [7,22],
}
for name, favourite_number in favourite_numbers.items():
	if len(str(favourite_number))==1:
		print(name.title() + "'s favourite number is: " + "\n\t"+str(favourite_number))
	else:
		print(name.title() + "'s favourite number are: ")
		for number in favourite_number:
			print("\t"+str(number))
#6-11
cities = {
	'hefei':{
		'country':'china',
		'population':'8.2million',
		'fact':'Mount Huang is in Hefei.'
	},
	'tokyo':{
		'country':'japan',
		'population':'9.46million',
		'fact':'Sensoji Temple is in Tokyo.'
	},
	'london':{
		'country':'england',
		'population':'8.9million',
		'fact':'London Eye is in London.'
	},
}
for name, info in cities.items():
	#country = info['country']
	#population = info['population']
	#fact = info['fact']
	print("\nCity Name:"+name)
	print("\tLocated Country: "+info['country'].title())
	print("\tPopulation: "+info['population'].title())
	print("\tFact: "+info['fact'].title())
#------------------------------------------------------------------------#




