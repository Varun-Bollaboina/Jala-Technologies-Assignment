#Loops


#01 QUESTION
# program to print “Bright IT Career” ten times using for loop

print("Bright IT Career\n"*10)




#02 QUESTION
#java program to print 1 to 20 numbers using the while loop

package IncludeHelp;

public class Print_1_To_20_UsingWhile 
{
   public static void main(String args[])
   {
      //loop counter initialisation
      int i=1;

      //print statement
      System.out.println("Output is : ");

      //loop to print 1 to 20.
      while(i<=20)   
      {
         System.out.println(i);
         i++;
      }
   }
}



#03 QUESTION
#Program to equal operator and not equal operators

a = 21
b = 10

if ( a == b ):
   print "Line 1 - a is equal to b"
else:
   print "Line 1 - a is not equal to b"



#04 QUESTION
#program to print the odd and even numbers


#Python program to print Even numbers from 1 to n
max=int(input("Please Enter the maximum value: "))

for num in range(2, max+1, 2):
    print("{0}".format(num))

    #Python program to print odd numbers from 1 to n
max=int(input("Please Enter the maximum value: "))

for num in range(1, max+1, 2):
    print("{0}".format(num))



 #05 QUESTION
 #program to print largest number among three numbers

 

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


#06 QUESTION
#program to print even number between 10 and 20 using while loop

x = int(input("Enter a number:"))
i = 1
while i <= x:
    if i % 2 == 0:
        print("Number is even:", i)
    i = i + 1


#07 QUESTION
#program to print 1 to 10 using the do-while loop statement



count = 1

while True:
    print(count)
    count += 1
    
    # test condition
    if count>10:
        break



#08 QUESTION
#program to find Armstrong number or not


# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



#09 QUESTION
#program to find the prime or not



num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")



#10 QUESTION
#program to palindrome or not


# function to check string is
# palindrome or not
def isPalindrome(str):

	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")



#11 QUESTION
#Program to check whether a number is EVEN or ODD using switch

# A number is even if division by 2 gives a remainder of 0
# If the remainder is 1, it is an odd number

if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))




#12 QUESTION
#Print gender (Male/Female) program according to given M/F using switch


Source Code:

#include <stdio.h>
#include<conio.h>
void main()
{
    char gender;

    //Reading gender from user
    printf("Enter gender (M/m or F/f): ");
    scanf("%c",&gender);

    switch(gender)
    {
        case 'M':
        case 'm':
            printf("Male");
            break;
        case 'F':
        case 'f':
            printf("Female");
            break;
        default:
            printf("Unspecified Gender\n");
    }

    getch();
}


