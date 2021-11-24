#Exceptions



#01 QUESTION
# Python program to demonstrate finally
# No exception Exception raised in try block


try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')





#02 QUESTION
#Handle the Arithmetic exception using try-catch block

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)


#03 QUESTION
#program with multiple catch blocks


import math


def square(x):
    if int(x) is 0:
        raise ValueError('Input argument cannot be zero')
    if int(x) < 0:
        raise TypeError('Input argument must be positive integer')
    return math.pow(int(x), 2)


#04 QUESTION
#program to throw exception with your own message


class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'


# raise MyCustomError

raise MyCustomError('We have a problem')



#05 QUESTION
#program to create your own exception


lass YourException(Exception):
  def __init__(self, message):
    self.message = message
 
try:
  raise YourException("Something is fishy")
 
except YourException as err:
  # perform any action on YourException instance
  print("Message:", err.message)


#06 QUESTION
#program with finally block

try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished"



#07 QUESTION
# program to generate Arithmetic Exception


try:  
    a = 10/0  
    print (a)
except ArithmeticError:  
        print ("This statement is raising an arithmetic exception.")
else:  
    print ("Success.")




#08 QUESTION
#program to generate FileNotFoundException

# trying to open a file, which does not exist
try:
    #trying to open a file in read mode
    fo = open("myfile.txt","rt")
    print("File opened")
except FileNotFoundError:
    print("File does not exist")
except:
    print("Other error")



#09 QUESTION
#program to generate IOException


import sys
def whatever():
try:
f = open ( "foo.txt", 'r' )
except IOError, e:
print e
print sys.exc_type
whatever()


#10 QUESTION
#program to generate NoSuchFieldException

public Field getField (String name) throws NoSuchFieldException {
  for (Field f : getFields()) {
    if (f.name.equals(name)) return f;
  }
  throw new NoSuchFieldException();
}





#11 QUESTION
#program to generate classnotfoundexception


// Java Program to Illustrate ClassNotFoundException
public class GFG {

	// Main driver method
	public static void main(String args[])
	{

		// Try block to check for exceptions
		try {

			Class.forName("GeeksForGeeks");
		}

		// Catch block to handle exceptions
		catch (ClassNotFoundException ex) {

			// Displaying exceptions on console along with
			// line number using printStackTrace() method
			ex.printStackTrace();
		}
	}
}





