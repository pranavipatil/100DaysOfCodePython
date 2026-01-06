# Day 22 – OOP: Inheritance

class Parent:
    def __init__(self,n,age):
        self.name = n
        self.Age = age
        
    def show_parent(self):
        print("Name: ",self.name)
        print("Age: ",self.Age)
    
class Child(Parent):
    def __init__(self, n, age,roll):
        super().__init__(n, age)
        self.rollno = roll

    def show_Child(self):
        self.show_parent()
        print("RollNo: ",self.rollno)

child1 = Child("Pranavi",22,109)
child1.show_Child()