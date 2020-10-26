
class Human(object):
	def __init__(self, name, age):
		self.name = name 
		self.age = age

class DriversLicense(Human):
	def __init__(self, license_no, name, age):
		super().__init__(name, age)
		self.license_no = license_no


person = DriversLicense(name='Carl', age=27, license_no=123456789)

print(person.license_no)