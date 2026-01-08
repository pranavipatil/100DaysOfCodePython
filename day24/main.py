# Day 24 – OOP: Encapsulation

class Student:
    def __init__(self,n,cur,mark):
        self.name = n
        self._course = cur
        self.__marks = mark

    def show(self):
        print("Name: ",self.name)    
        print("Course: ",self._course)    
        print("Marks: ",self.__marks)      

    def get_marks(self):
        return self.__marks

    def set_marks(self,new_marks):
        self.__marks = new_marks
        
    
s1 = Student("Pranavi","Python",90)
s1.show()

print()
# Access marks using getter
print("Access Marks Via Getter: ",s1.get_marks())  

#Update marks using setter
s1.set_marks(95)
print("Updated Marks:", s1.get_marks())
