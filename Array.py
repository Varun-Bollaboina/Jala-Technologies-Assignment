# 01 QUESTION
#function to add integer values of an array

lst = []
num = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for n in range(num):
  numbers = int(input())
  lst.append(numbers)
print("Sum:", sum(lst))


#02 QUESTION
#function to calculate the average value of an array of integers

avreage_cost = cost
    avg = sum(avreage)/len(avreage) 
    print("The average amout you spent is ", round(avg,2))

# Python program to get average of a list
def Average(lst):
	return sum(lst) / len(lst)

# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

# Printing average of the list
print("Average of the list =", round(average, 2))



#03 QUESTION
# program to find the index of an array element

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print the index of '4' in list1
print(list1.index(4))

list2 = ['cat', 'bat', 'mat', 'cat', 'pet']

# Will print the index of 'cat' in list2
print(list2.index('cat'))



# 04 QUESTION
# function to test if array contains a specific value

USE THE in KEYWORD TO CHECK IF AN ELEMENT EXISTS IN AN ARRAY


#05 QUESTION
#function to remove a specific element from an array

USE list.pop() TO REMOVE AN ELEMENT FROM A LIST BY INDEX


# 06 QUESTION
#function to copy an array to another array


STEP 1: Declare and initialize an array.
STEP 2: Declare another array of the same size as of the first one
STEP 3: Loop through the first array from 0 to length of the array and copy an element from the first array to the second array that is arr1[i] = arr2[i].


#07 QUESTION
#function to insert an element at a specific position in the array


The insert() method inserts an element to the list at the specified index



#08 QUESTION
# function to find the minimum and maximum value of an array


min() is used for find out minimum value in an array, max() is used for find out maximum value in an array. index() is used for finding the index of the element.



#09 QUESTION
#function to reverse an array of integer values


Python also provides a built-in method reverse() that directly reverses the order of list items right at the original place


#10 QUESTION
#function to find the duplicate values of an array


#Initialize array     
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     
print("Duplicate elements in given array: ");    
#Searches for duplicate element    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);  








