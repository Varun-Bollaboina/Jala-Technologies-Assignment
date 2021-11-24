# Strings




#01 QUESTION
#Different ways creating a string


Strings can be created by enclosing characters inside a single quote or double-quotes


#02 QUESTION
#Concatenating two strings using + operator

str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1+str2
print("Concatenated two different strings:",str)



#03 QUESTION
#Finding the length of the string


# using len

str = "geeks"
print(len(str))


#04 QUESTION
#Extract a string using Substring



myString = "Mississippi"
print(myString[:]) # Line 1
print(myString[4 : ]) # Line 2
print(myString[ : 8]) # Line 3
print(myString[2 : 7]) # Line 4
print(myString[4 : -1]) # Line 5
print(myString[-6 : -1]) # Line 6



#05 QUESTION
#Searching in strings using index()

text = 'Python is fun'

# find the index of is
result = text.index('is')
print(result)



#06 QUESTION
#Matching a String Against a Regular Expression With matches()

If you need to know if a string matches a regular expression RegExp , use RegExp. test() . If you only want the first match found, you might want to use RegExp.


#07 QUESTION
#Comparing strings

Python comparison operators can be used to compare strings in Python. These operators are: equal to ( == ), not equal to ( != ), greater than ( > ), less than ( < ), less than or equal to ( <= ), and greater than or equal to ( >= ).


#08 QUESTION
#startsWith(), endsWith() and compareTo()


startswith() function checks if a string starts with a specified substring.
endswith() checks if a string ends with a substring.
Both functions return True or False.

cmp() is an in-built function in Python, it is used to compare two objects and returns value according to the given values.


#09 QUESTION
#Trimming strings with strip()

Python string.strip() function basically removes all the leading as well as trailing spaces from a particular string. Thus, we can use this method to completely trim a string in Python.


#10  QUESTION
#Replacing characters in strings with replace()

USE str.replace() TO REPLACE CHARACTERS IN A STRING


#11 QUESTION
#Splitting strings with split()

The split() method splits a string into a list.

You can specify the separator, default separator is any whitespace.



#12 QUESTION
#Converting integer objects to Strings


To convert an integer to string in Python, use the str() function. This function takes any data type and converts it into a string, including integers. Use the syntax print(str(INT)) to return the int as a str , or string. Python includes a number of data types that are used to distinguish a particular type of data.


#13 QUESTION
#Converting to uppercase and lowercase

The lower() method converts all uppercase characters in a string into lowercase characters and returns it.

The upper() method converts all lowercase characters in a string into uppercase characters and returns it.