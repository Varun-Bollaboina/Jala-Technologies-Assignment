
#01 QUESTION
#class with a default constructor

class Jalatechnologies:
 
    # default constructor
    def __init__(self):
        self.varun = "jalatechnologies"
 
    # a method for printing data members
    def print_varun(self):
        print(self.varun)
 
 
# creating object of the class
obj = jalatechnologies()
 
# calling the instance method using the object obj
obj.print_varun()



#02 QUESTION
#Calling a Super Class Constructor



# this is the class which will become
# the super class of "Subclass" class
class Class():
    def __init__(self, x):
        print(x)
  
# this is the subclass of class "Class"
class SubClass(Class):
    def __init__(self, x):
  
        # this is how we call super
        # class's constructor
        super().__init__(x)
  
# driver code
x = [1, 2, 3, 4, 5]
a = SubClass(x)



#03 QUESTION
#Apply private, public, protected and default access modifiers to the constructor


# defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name;   # protected attribute 
        self._sal = sal;     

# defining class Employee
class Employee:
    def __init__(self, name, sal):
        self.__name = name;    # private attribute 
        self.__sal = sal;    

# defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):  #Public attribute
        self.name = name;
        self.sal = sal;



#04 QUESTION
#program which illustrates the concept of attributes of a constructor


class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
  
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)  
  
# accessing display() method to print employee 1 information  
  
emp1.display()  
  
# accessing display() method to print employee 2 information  
emp2.display() 