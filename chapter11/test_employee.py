#11-3
import unittest
from employee import Employee

class Employeetest(Employee):
	def setUp(self):
		self.yue = Employee('yue','yu','100000')

	def test_give_default_raise(self):
		self.yue.give_raise()
		self.assertEqual(self.salary,105000)

	def test_give_custom_raise(self):
		self.yue.give_raise(10000)
		self.assertEqual(self.salary, 110000)
unittest.main()

