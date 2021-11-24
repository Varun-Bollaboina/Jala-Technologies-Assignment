

#01 QUESTION
#two methods with the same name but different number of parameters of same type

class Dog{
    public void bark(){
        System.out.println("woof ");
    }
 
    //overloading method
    public void bark(int num){
    	for(int i=0; i<num; i++)
    		System.out.println("woof ");
    }
}



#02 QUESTION
#two methods with the same name but different number of parameters of different data type

# First product method.
# Takes two argument and print their
# product
def product(a, b):
	p = a * b
	print(p)
	
# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error	
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)



#03 QUESTION
#two methods with the same name and same number of parameters of same type

public void ChangeProfileInformation(User user)
{
   a
   b
}

public void ChangeProfileInformation(User user)
{
   a
   c
   d
}