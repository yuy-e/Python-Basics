#11-3
class Employee():
	def __init__(self, first_name, last_name, annual_salary):
		self.first = first_name.title()
		self.last = last_name.title()
		self.salary = annual_salary

	def give_raise(self, raise_salary = 5000):
		self.salary += raise_salary
		