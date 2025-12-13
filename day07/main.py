# Day 07 – Lists in Python

#Q1. Create a list of 5 numbers
nums = [10, 20, 30, 40, 50]
print("Original List : ",nums)

# Q2. Access first, last, and middle elements
print("First Element :",nums[0])
print("Last Element :",nums[-1])
print("Middle Element :",nums[len(nums)//2])

# Q3. Add and remove elements
#Add elements:
'''
Add one number at the end
Insert one number at index 2
'''
nums.append(60)
nums.insert(2,1)
print(nums)

#  Remove Elements:
'''
Remove a specific value
Remove last element
'''
nums.remove(1)
nums.pop()
print(nums)

# Q4. Sort and reverse a list
nums.sort()
nums.reverse()
print(nums)

# Q5. Find length of the list
print("Length Of List : ",len(nums))

