# Day 25 – OOP: Abstraction

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def dog(self):
        pass

    @abstractmethod
    def cat(self):
        pass

class Animal_sound(Animal):
    def dog(self):
        print("Bark Bark!!")
    def cat(self):
        print("Meow Meow !!")

obj = Animal_sound()
obj.dog()
obj.cat()
