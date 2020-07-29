'''Answer for 9-11'''
class User():
	def __init__(self, first_name, last_name, gender, username, email):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.username = username
		self.email = email
		self.full_name = self.first_name+" "+self.last_name

		self.login_attempts = 0
	def describe_user(self):
		print("\nThe user's name is "+self.full_name.title()+".")
		print("\tUser's gender: "+self.gender)
		print("\tUser's username: "+self.username)
		print("\tUser's email: "+self.email)
	def greet_user(self):
		print("\nHello, " + self.full_name.title() + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print("User's attempts to log in: " + str(self.login_attempts))

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("User's attempts to log in have been reset: 0 .")

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
