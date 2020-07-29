'''Answer for 9-12'''
from user import User

class Privileges():
	def __init__(self, privileges = []):
		self.privileges = privileges

	def show_privileges(self):
		print("\nThe user's privileges include: ")
		for privilege in self.privileges:
			print("\t"+privilege)

class Admin(User):
	def __init__(self, first_name, last_name, gender, username, email):
		super().__init__(first_name, last_name, gender, username, email)
		self.privileges = Privileges()
