# Day 12 – Recursion in Python

#Q1.  Print numbers from 1 to n using recursion
def num(n=1):
    if n == 0:
        return
    num(n-1)
    print(n)
num(5)

#Q2. Find factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#Q3. Find sum of first n natural numbers using recursion
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
print(sum(5))

#Q4. Find nth Fibonacci number using recursion
def fibonacci(n):
    if n == 0:          
        return 0
    elif n == 1:       
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))


