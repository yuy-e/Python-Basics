#chapter11
#------------------------------------------------------------------------#
#11-1
#city_functions.py 测试通过
def city_country(city, country):
	formatted_city_country = city.title() + ', ' + country.title()
	return formatted_city_country

#test_cities.py
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_city_country = city_country('santiago','chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')
unittest.main()
#------------------------------------------------------------------------#
#11-2
#city_functions.py 测试未通过
def city_country(city, country,population):
	formatted_city_country = city.title() + ', ' + country.title() + " - population " + population
	return formatted_city_country

#test_cities.py 未变
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_city_country = city_country('santiago','chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')
unittest.main()
#------------------------------------------------------------------------#
#11-2
#city_functions.py 形参population可选，测试通过
def city_country(city, country,population=0):
	formatted_city_country = city.title() + ', ' + country.title()
	if population:
		formatted_city_country += " - population " + str(population)
	return formatted_city_country

#test_cities.py
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_city_country = city_country('santiago','chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')

unittest.main()
#------------------------------------------------------------------------#
#11-2
#city_functions.py
def city_country(city, country,population=0):
	formatted_city_country = city.title() + ', ' + country.title()
	if population:
		formatted_city_country += " - population " + str(population)
	return formatted_city_country

#test_cities.py
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_city_country = city_country('santiago','chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')

	def test_city_country_population(self):
		formatted_city_country_population = city_country('santiago','chile',5000000)
		self.assertEqual(formatted_city_country_population, 'Santiago, Chile - population 5000000')

unittest.main()

#------------------------------------------------------------------------#
#11-3
class Employee():
	def __init__(self, first_name, last_name, annual_salary):
		self.first = first_name.title()
		self.last = last_name.title()
		self.salary = annual_salary

	def give_raise(self, raise_salary = 5000):
		self.salary += raise_salary
		return self.salary









