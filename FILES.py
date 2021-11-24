#FILES


#01 QUESTION
#program to read text file

# opening a file in 'r'
file = open('sample.txt', 'r')
# read() - it used to all content from a file
# readline() - it used to read number of lines we want, it takes one argument which
is number of lines
# readlines() - it used to read all the lines from a file, it returns a list
# reading data from the file using read() method
data = file.read()
# printing the data
print(data)
# closing the file
file.close()



#02 QUESTION
#program to write text to .txt file using InputStream



lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')




#03 QUESTION
#Write a program to read a file stream


f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())





#04 QUESTION
#program to read a file stream supports random access


import sys,random
with open(sys.argv[1],"r") as f:
    f.seek(0,2)                 # seek to end of file
    bytes = f.tell()
    f.seek(int(bytes*random.random()))

    # Now seek forward until beginning of file or we get a \n
    while True:
        f.seek(-2,1)
        ch = f.read(1)
        if ch=='\n': break
        if f.tell()==1: break

    # Now get a line
    print f.readline()





#05 QUESTION
#program to read a file a just to a particular index using seek()



 f = open("testFile.txt", "r")
f.seek(9)
print(f.readline()




#06 QUESTION
#program to check whether a file is having read access and write access permission

>>> import os
>>> os.access('my_file', os.R_OK) # Check for read access
True
>>> os.access('my_file', os.W_OK) # Check for write access
True

