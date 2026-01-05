# Day 21 – OOP Basics: Classes & Objects

#1. Created a class named `Person`
class Person:
#2. Used a constructor to initialize attributes
    def __init__(self,n,age):
        self.name = n
        self.myage = age

#3. Created methods inside a class
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.myage)

#4. Created multiple objects from the same class
p1 = Person("Pranavi",22)
p2 = Person("Shresha",10)

#5. Accessed object data using methods
p1.show()
p2.show()
