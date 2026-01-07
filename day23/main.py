# Day 23 – OOP: Polymorphism

class Animal:
    def sound(self):
        print("Animal Makes a sound!!")

class Dog(Animal):
    def sound(self):
        print("Dogs barks!!")

class Cat(Animal):
    def sound(self):
        print("Cat meows!!")

d = Dog()
c = Cat()

d.sound()
c.sound()