# Day 13 – Modules in Python

#Q1. Used math module functions
'''
Task 1: Use math module
Find square root of 25
Find factorial of 6
'''
import math
print("Squre root of 25 : ",math.sqrt(25))
print("Factorial of 6 :",math.factorial(6))


#Q2. Generated random numbers using random module
'''
Generate a random number between 1 and 10
'''
import random
print("Random Number :",random.randint(1,10))

#Q3. Worked with current date using datetime module
'''
Print today's date
'''
import datetime
print("Today's Date :",datetime.date.today())

#Q4. Used module alias
'''
Import math module as m
Print value of π
'''
import math as m
print("Value of π :",m.pi)

#Q5. Created and used a user-defined module
'''
Create my_module.py and inside that file write short code
'''
import my_module
my_module.greet("Pranavi")