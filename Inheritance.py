#Inheritance

#Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C
#Call an overridden method with super class reference to B and C class’s objects


class A:
    def m(self):
        print("m of A called")
class B(A):
    pass
class C(A):
    def m(self):
        print("m of C called")
class A(B,C):
    pass
x = D()
x.m()