# Day 09 – Sets in Python

#1. Create a set with duplicate values
nums = {10,20,30,20,30,40,50,60}
print("Original Set :",nums)

#2. Add and remove elements from a set
nums.add(70)
print("Adding 70 in Set :",nums)

nums.discard(60)
print("Removing 60 from Set :",nums)

#3️. Create two sets and perform operations
'''
-->Union
-->Intersection
-->Difference (a - b)
'''
set1 = {1,2,3,4,5,6}
set2 = {3,4,9,7,10,8}

print("Set1 :",set1)
print("Set2 :",set2)

union = set1.union(set2)
print("Union :",union)

intersection = set1.intersection(set2)
print("Intersection :",intersection)

difference = set1.difference(set2)
print("Difference of set1 :",difference)

difference1 = set2.difference(set1)
print("Difference of set2 :",difference1)

#4. Check membership in a set
print("Check 70 in Set :",70 in nums)

#5️. Find length of the set
print("Length of OG set :",len(nums))