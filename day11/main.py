# Day 11 – Functions in Python

#Q1. Create a function to print a greeting
def greet():
    print("Hello World !!")
greet()

#Q2. Function to add two numbers
def add(a,b):
    print("Sum :",a+b)
add(9,5)

#Q3. Function to check even or odd
def even(n):
    if n % 2 == 0:
        print(f"{n} is Even Number ")
    else:
        print(f"{n} is Odd Number ")
even(9)

#Q4. Function to find maximum of two numbers
def find_max(a,b):
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
find_max(6,5)

#Q5. Function with return value
def square(n):
    return n * n
print("Square :",square(5))