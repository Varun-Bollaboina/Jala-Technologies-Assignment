#Access modifiers

#01 QUESTION
#Create a class with PRIVATE fields.

class myClass:
   __privateVar = 27;
   def __privMeth(self):
      print("I'm inside class myClass")
   def hello(self):
      print("Private Variable value: ",myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privateMeth


#02 QUESTION
# Create a class with PROTECTED fields and methods


# program to illustrate protected
# data members in a class


# Defining a class
class VARUN:
	
	# protected data members
	_name = "R2J"
	_roll = 1706256
	
	# public member function
	def displayNameAndRoll(self):

		# accessing protected data members
		print("Name: ", self._name)
		print("Roll: ", self._roll)


# creating objects of the class		
obj = VARUN()

# calling public member
# functions of the class
obj.displayNameAndRoll()




#03 QUESTION
#Create a class with PUBLIC fields and methods



# program to illustrate public access modifier in a class

class Varun:
	
	# constructor
	def __init__(self, name, age):
		
		# public data members
		self.VarunName = name
		self.VarunAge = age

	# public member function	
	def displayAge(self):
		
		# accessing public data member
		print("Age: ", self.VarunAge)

# creating object of the class
obj = Varun("R2J", 20)

# accessing public data member
print("Name: ", obj.VarunName)

# calling public member function of the class
obj.displayAge()
