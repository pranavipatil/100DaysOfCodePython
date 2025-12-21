# Day 15 – Error Handling in Python

#1. Handle ZeroDivisionError
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Program executed successfully!")


#2. Handle ValueError
try:
    a = int(input("Enter Any Number: "))
    print(a)
except ValueError:
    print("Please enter a valid number!")
else:
    print("Program executed successfully!")


#4. Handle Error With general Exception Handling
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Result: ",a/b)
except Exception:
    print("An exception occurred!")
else:
    print("Program executed successfully!")


#5. Use finally block
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero!!")
else:
    print("Program executed successfully!")
finally:
    print("Program Ended!")