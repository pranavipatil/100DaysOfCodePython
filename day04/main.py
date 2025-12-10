# Day 04 – If / Else Conditions

## Check if a number is EVEN or ODD
n = int(input("Enter Any Number : "))
if n % 2 == 0:
    print("Given Number is an Even Number")
else:
    print("Given Number is an odd Number")


## Check if a person is ELIGIBLE TO VOTE
age = int(input("Enter Age : "))
if age >= 18:
    print("You are Eligible For Vote !!")
else:
    print("You are Not an Eligible For Vote !!")


## Find the Largest of 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)
elif b > a and b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

## Simple Grading System

marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 0:
    print("Grade: Fail")
else:
    print("Invalid marks entered")

