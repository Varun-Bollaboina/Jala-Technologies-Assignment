#Abstact class



#01 QUESTION
#Create an abstract class with abstract and non-abstract methods



abstract class AbstractDemo { // Abstract class
   private int i = 0;
   public void display() { // non-abstract method
      System.out.print("Welcome to Jala technologies");
   }
}
public class InheritedClassDemo extends AbstractDemo {
   public static void main(String args[]) {
      AbstractDemo demo = new InheritedClassDemo();
      demo.display();
   }
}





#02 QUESTION
#Create an instance for the child class in child class and call abstract methods



# implementation of abstract
# class through subclassing

import abc

class parent:	
	def varun(self):
		pass

class child(parent):
	def varun(self):
		print("child class")

# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))



#03 QUESTION
#Create an instance for the child class in of parent class.


class A(object):
    def __init__(self):
        print "A created"
P = A()


class B(A):
    def __init__(self):
        print super((B), self).__init__ 
        print self.__class__.__name__
        print super(B, self).__class__.__name__




