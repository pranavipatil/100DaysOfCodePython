# Day 18 – map(), filter(), reduce() in Python

#1. Use map() to square numbers
l = [1,2,3,4,5]
sqr = lambda n: n*n
print(list(map(sqr,l)))

#2. Use filter() to get even numbers
m = [11,12,13,14,15,16,17,18,19,20]
even = lambda n: n % 2 == 0
print(list(filter(even,m)))

#3. Use reduce() to find sum of numbers
from functools import reduce
nums = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, nums)
print("Sum:", total)

#4. Use reduce() to find product of numbers
num = [1,2,3,4,5]
pro = reduce(lambda a,b:a*b,num)
print("Product: ", pro)


