# Day 26 – Exception Hierarchy in Python

#1. Handled ZeroDivisionError
try:
    a = int(input("Enter Number: "))
    b = int(input("Enter Another Number: "))
    print(a/b)
except ZeroDivisionError:
    print("You can not divide by Zero !!")
else:
    print("Program Executed Successfully !!")

#2. Handled ValueError
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    result = a + b
    print(result)
except ValueError:
    print("Please Enter valid Number !!")
else:
    print("Program executed successfully")

#3. Used multiple except blocks
try:
    a = int(input("Enter Number: "))
    b = int(input("Enter Another Number: "))
    print(a*b)
except ZeroDivisionError:
    print("You cannot divide by Zero !!")
except ValueError:
    print("Please Enter valid Number !!")
else:
     print("Program executed successfully")

#4. Used general Exception block
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print(a-b)
except Exception:
    print("Exception Occurred !!")
else:
    print("Program executed successfully")

#5. Observed exception hierarchy behavior
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception:
    print("Some error occurred")
