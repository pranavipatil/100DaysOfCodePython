# Day 17 – Lambda Functions in Python

#1. Lambda function to add two numbers
add = lambda a,b:a+b
print("Addition :",add(2,3))

#2. Lambda function to find square of a number
sqr = lambda n:n*n
print("Square of 5 :",sqr(5))

#3. Lambda function to check even or odd
even = lambda s: "Even Num" if s % 2 == 0 else "Odd Num"
print("Given Num is a :",even(4))

#4. Lambda function with conditional expression
cond = lambda m: "Pass" if m >= 50 else "Fail"
print("Result: ",cond(51))

#5. Using lambda with list
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, nums))
print("Squares: ",squares)

