'''Answer for 9-10'''
class Restaurant():
	def __init__(self, restaurant_name, restaurant_type):
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		self.number_served = 0

	def describe_restaurant(self):
		print("\nThe restaurant name is " + self.restaurant_name.title() + ".")
		print("The type of the restaurant is " + self.restaurant_type.title() + ".")
		print("The restaurant has served " + str(self.number_served) + " customers.")

	def open_restaurant(self):
		print("The restaurant is opening.")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		self.number_served += additional_served

