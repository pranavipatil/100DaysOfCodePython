# Day 16 – List Comprehensions in Python

#1. Create a list of numbers using list comprehension
'''
Create a list of numbers from 1 to 10
'''
list1 = [i for i in range(1,11)]
print("Noraml List: ",list1)

#2. Create a list of squares
sqr = [i*i for i in range(1,11)]
print("Squares: ",sqr)

#3. Create a list of even numbers
even = [i for i in range(1,11) if i % 2 == 0]
print("Even Numbers: ",even)

#4. Create a list with condition
'''
Create a list of numbers divisible by 3(1,30)
'''
div = [i for i in range(1,31) if i % 3 == 0]
print("Divisible by 3: ",div)

#5. Convert string characters to list
name = "Pranavi"
typc = [ch for ch in name]
print("Characters: ",typc)