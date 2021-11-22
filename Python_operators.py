# operators

#01 QUESTION
#Arithmatic operators


# Store input numbers:  
num1 = input('Enter first number: 20 ')  
num2 = input('Enter second number: 10 ')  
  
# Add two numbers  
sum = float(20) + float(10)  
# Subtract two numbers  
min = float(20) - float(10)  
# Multiply two numbers  
mul = float(20) * float(10)  
#Divide two numbers  
div = float(20) / float(10)  
# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  




#02 QUESTION
# increment and decrement operators(++, --)
# A sample use of increasing the variable value by one.
count=0
count+=1
count=count+1
print('The Value of Count is',count)
 
# A Sample Python program to show loop (unlike many
# other languages, it doesn't use ++)
# this is for increment operator here start = 1,
# stop = 5 and step = 1(by default)
print("INCREMENTED FOR LOOP")
for i in range(0, 5):
   print(i)
 
# this is for increment operator here start = 5,
# stop = -1 and step = -1
print("\n DECREMENTED FOR LOOP")
for i in range(4, -1, -1):
   print(i)




#03 QUESTION
#program to find the two numbers equal or not

a=20
b=10
if a==b:
 print ("equal")
else:
 print ("unequal")



 #04 QUESTION
 #Program for relational operators (<,<==, >, >==)

# [<] operator
a = 9
b = 5
  
# Output
print(a < b)

# [<=]operator
a = 9
b = 5
  
# Output
print(a <= b)

# [>] operator
a = 9
b = 5
  
# Output
print(a > b)

# [>=] 0perator

a = 9
b = 5
  
# Output
print(a >= b)


#05 QUESTION
#Print the smaller and larger numbe

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

