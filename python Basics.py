#python Basics

#01 question  
#program for name

Name = "varun bollaboina"
Age = 23

print(Name)


#02 question
#program for single line commenting

# initializing two variables
a = 5
b = 7

# adding a and b
result = a + b

# printing the result of the addition
print(result)




#program for multi line commenting

# Read the input from the user
# Perform some operations on the input data
# Output the result
print("JALA TECHNOLOGIES")




#03 question
#program for variables for different data types

rating = 4.7
print(rating, type(rating))
Name = 'varun'
print(Name, type(Name))
Marks = 98
print(Marks, type(Marks))
is_passed = True
print(is_passed, type(is_passed))
My_complex_number = 4+5j
print(My_complex_number,type(My_complex_number))
fruits_list = ('Apple','Banana','mango')
print(fruits_list, type(fruits_list))



#04 question
#local and global variables with same name


def f():
     
    # local variable
    s = "I love joining JALA TECHNOLOGIES"
    print(s)
 
# Driver code
f()



# This function uses global variable s
def f():
    print("Inside Function", s)
 
# Global scope
s = "I love Joining JALA TECHNOLOGIES"
f()
print("Outside Function", s)
