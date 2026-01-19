# Day 33 – List Practice Programs

#1. Created a list of numbers
l = [1,2,3,4,5,6]
print("List: ",l)

#2. Find sum of list elements
total = 0
for i in l:
    total += i
print("Sum of Elements: ",total)

#3. Find maximum element
max_num = l[0]
for i in l:
    if i > max_num:
        max_num = i
print("Maximum Element: ",max_num)

#4. Counted even and odd numbers
even = 0
odd = 0
for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers: ",even)
print("Odd numbers: ",odd)

#5. Reversed a list
rev = []
for i in l:
    rev = [i] + rev
print("Reverse List: ",rev)