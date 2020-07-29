#chapter4
#4-1
pizzas = ['margerita pizza','extreme pizza','hawaii pizza']
for pizza in pizzas:
	print("I like "+ pizza.title())
print("I really love pizza!")
#4-2
animals = ['dog','cat','rabbit','elephant','giraffe','fox']
for animal in animals:
	print(animal)
	print("A "+animal+" would make a great pet.")
print("Any of these animals would make a great pet!")
#------------------------------------------------------------------------#
even_numbers=list(range(2,18,3))
print(even_numbers)
#------------------------------------------------------------------------#
squares=[]
for value in range(1,8):
	square = value**2
	squares.append(square)
print(squares)
#------------------------------------------------------------------------#
squares=[]
for value in range(1,8):
	squares.append(value**2)
print(squares)
#------------------------------------------------------------------------#
squares = [value**2 for value in range(1,11)]
print(squares)
#------------------------------------------------------------------------#
#4-3
numbers=[]
for value in range(1,21):
	print(value)
	numbers.append(value)
print(numbers)
#4-4
'''
numbers=[]
for value in range(1,1000001):
	numbers.append(value)
print(numbers)
'''
#4-5
numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#4-6
numbers = list(range(1,20,2))
for number in numbers:
	print(number)	
#4-7
numbers = list(range(3,30,3))
for number in numbers:
	print(number)
#4-8
for number in range(1,11):
	value = number**3
	print(value)
#4-9 列表解析
numbers = [number**3 for number in range(1,11)]
print(numbers)
#4-10
animals = ['dog','cat','rabbit','elephant','giraffe','fox','panda']
print('The first three items in the list are:')
print(animals[:3])
print('Three items from the middle of the list are:')
print(animals[2:5])
print('The last three items in the list are:')
print(animals[-3:])
#4-11
pizzas = ['margerita pizza','extreme pizza','hawaii pizza']
friend_pizzas = pizzas[:]
pizzas.append('fruit pizza')
friend_pizzas.append('mexican pizza')
print('My favourite pizzas are:')
for pizza in pizzas:
	print(pizza)
print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

#4-12
print('\n')
pizzas = ['margerita pizza','extreme pizza','hawaii pizza','fruit pizza']
friend_pizzas = ['extreme pizza','margerita pizza','mexican pizza','hawaii pizza']
a = len(pizzas)
b = len(friend_pizzas)
print(a,b)
for i in range(0,a):
	for j in range(0,b):
		if pizzas[i]==friend_pizzas[j]:
			print("we both like the pizza:")
			print(pizzas[i])
		else: 
			j = j+1
else:
	print("my friend donnot like the pizza:")
	print(pizzas[i])

#4-13
foods=('hamberger','fish ball soup','ice cream','noodles','coke')
#foods[0]='macaroni通心粉'
#'tuple' object does not support item assignment
for food in foods:
	print(food)
foods=('macaroni通心粉','potage法式浓汤','ice cream','noodles','coke')
print("\nNew Menu:")
for food in foods:
	print(food)
#------------------------------------------------------------------------#
