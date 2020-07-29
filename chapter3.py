#Chapter 3
methods = ['motorcycle', 'Private Car', 'Train', 'Airplane']
print(methods)
#------------------------------------------------------------------------#
#3-1
names =['hua tian', 'luge wang', 'yue yu', 'wenxuan wang']
print(names[0].title())
print(names[1].title())
print(names[-2].title())
print(names[-1].title())
#3-2
message = names[0].title() + ', Hi!'
print(message)
message = names[1].title() + ', Hi!'
print(message)
message = names[2].title() + ', Hi!'
print(message)
message = names[3].title() + ', Hi!'
print(message)
#3-3
methods = ['Motorcycle', 'Private Car', 'Train', 'Airplane']
print(methods)
print('I would like to own a Honda'+' '+methods[0].lower()+'.')
print('I would like to own a pink'+" "+ methods[1].lower()+'.')
#------------------------------------------------------------------------#
#del xxx[]    but xxx.del()不可以用
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
#------------------------------------------------------------------------#
#pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#popped_motorcycle = motorcycles.pop()
second_owned = motorcycles.pop(1)
print('The second motorcycles I owned was '+second_owned.title()+'.')
print(motorcycles)
#------------------------------------------------------------------------#
#remove()
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is too expensive for me.')
#------------------------------ IMPORTANT NOTE------------------------------------------#

# motorcycles.del() do not work.
# print(motorcycles.remove()) do not work.

#------------------------------------------------------------------------#
#3-4
guests = ['hua tian','luge wang','wenxuan wang','wenxuan xie','yuyin an','liping guo']
print('Welcome to party, '+guests[0].title()+'!')
print('Welcome to party, '+guests[1].title()+'!')
print('Welcome to party, '+guests[2].title()+'!')
print('Welcome to party, '+guests[3].title()+'!')
print('Welcome to party, '+guests[4].title()+'!')
print('Welcome to party, '+guests[5].title()+'!')
#3-5
print('******************Method1********************')
print('It is a pity '+guests[4].title()+" cannot come.")
del guests[4]
guests.insert(4,'yue yu')
print(guests)
print('*******************Method2*******************')
guests = ['hua tian','luge wang','wenxuan wang','wenxuan xie','yuyin an','liping guo']
notcome_guests = guests.pop(4)
guests.insert(4,'yue yu')
print('It is a pity '+notcome_guests+" cannot come.")
print(guests)
print('*******************Method3*******************')
guests = ['hua tian','luge wang','wenxuan wang','wenxuan xie','yuyin an','liping guo']
notcome_guests = 'yuyin an'
guests.remove(notcome_guests)
print('It is a pity '+notcome_guests+" cannot come.")
guests.append('yue yu')
print(guests)
#3-6
guests = ['hua tian','luge wang','wenxuan wang','wenxuan xie','yuyin an','liping guo']
notcome_guests = 'yuyin an'
guests.remove(notcome_guests)
print('It is a pity '+notcome_guests+" cannot come.")
guests.append('yue yu')
print('I found a bigger table.')
guests.insert(0,'new_guest01')
guests.append('new_guest03')
guests.insert(4,'new_guests02')
print(guests)
print('Welcome to party, '+guests[0].title()+'!')
print('Welcome to party, '+guests[1].title()+'!')
print('Welcome to party, '+guests[2].title()+'!')
print('Welcome to party, '+guests[3].title()+'!')
print('Welcome to party, '+guests[4].title()+'!')
print('Welcome to party, '+guests[5].title()+'!')
print('Welcome to party, '+guests[6].title()+'!')
print('Welcome to party, '+guests[7].title()+'!')
print('Welcome to party, '+guests[8].title()+'!')
#3-7
print('\nSorry, there are only two places left.')
uninvited_guests = guests.pop(-1)
print('Sorry, '+uninvited_guests+'. The wedding is cancelled.')
uninvited_guests = guests.pop(-1)
print('Sorry, '+uninvited_guests+'. The wedding is cancelled.')
uninvited_guests = guests.pop(-1)
print('Sorry, '+uninvited_guests+'. The wedding is cancelled.')
uninvited_guests = guests.pop(-1)
print('Sorry, '+uninvited_guests+'. The wedding is cancelled.')
uninvited_guests = guests.pop(-1)
print('Sorry, '+uninvited_guests+'. The wedding is cancelled.')
uninvited_guests = guests.pop(-1)
print('Sorry, '+uninvited_guests+'. The wedding is cancelled.')
uninvited_guests = guests.pop(-1)
print('Sorry, '+uninvited_guests+'. The wedding is cancelled.')
print('Welcome to party, '+guests[0].title()+'!')
print('Welcome to party, '+guests[1].title()+'!')
del guests[-1]
del guests[-1]
print(guests)

#3-8 xxx.sorted()不可用
places = ['paris', 'newyork', 'beijing', 'seattle', 'santiago', 'berlin', 'tokyo']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
#3-9
a = len(guests)
print('The number of guests is '+ str(len(guests)))
#3-10
print('*****************************************************')
books = ['house of cards','suff matters','harry potter','the life of pi','a street cat named bob','the giver']
print("The number of books I'm gonna read this year is "+str(len(books))+'.')
print(books)
books.insert(1,'what is?')
print(books)
del books[-1]
print(books)
books.append('the giver')
print(books)
popped_book = books.pop(3)
print("I don't want to read "+popped_book.title()+' anymore.')
remove_book='the giver'
books.remove(remove_book)
print(books)
print("Sequence of books: "+str(sorted(books)))
print("Reverse sequence of books: "+str(sorted(books, reverse=True)))
books.sort()
print(books)
books.sort(reverse=True)
print(books)
print("The number of my new booklists is "+str(len(books))+'.')
print('*****************************************************')
#------------------------------------------------------------------------#

