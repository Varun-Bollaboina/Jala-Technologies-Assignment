#Create a program to create two class


class A():
    def __init__(self):
        self.x = 0


class B():
    def __init__(self):
        self.x = 1


class Container():
    def __init__(self,objects):
        self.x = [obj.x for obj in objects]

a = A()
b = B()
c = Container([a,b])

c.x

[0,1]


