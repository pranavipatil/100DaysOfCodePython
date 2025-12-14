# Day 08 – Tuples in Python

# Q1. Create a tuple of 5 numbers
nums = (10,20,30,40,50)
print("Original Tuple :",nums)

# Q2. Access first, last, and middle elements
print("First Element :",nums[0])
print("Last Element :",nums[-1])
print("Middle Element :",nums[len(nums)//2])

# Q3. Slice a tuple 
'''
First 3 elements
Last 2 elements
'''
print("First 3 Elements :",nums[:3:1])
print("Last 2 Elements :",nums[-2::])

# Q4. Use tuple functions
'''
Length of tuple
Minimum value
Maximum value
Count how many times a number appears
Find index of a value
'''
print("Length of Tuple :",len(nums))
print("Minimum Value :",min(nums))
print("Maximum Value :",max(nums))
print("Count of 30 :",nums.count(30))
print("Index of 40 :",nums.index(40))

# Q5. Convert tuple to list and list to tuple
a = list(nums)
a.append(60)
print(a)

print(tuple(a))


