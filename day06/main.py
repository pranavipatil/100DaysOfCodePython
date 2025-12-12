# Day 06 – Pattern Printing

# Q1.  Print a left triangle pattern 
n = 5
for i in range(n):
    for j in range(n):
        if i >= j:
            print("*",end = ' ')
    print()

# Q2. Print a reverse left triangle pattern  
n = 5
for i in range(n):
    for j in range(n):
        if i <= j:
            print("*",end = ' ')
    print()

# Q3. Print a square of stars (5x5)  
n = 5
for i in range(n):
    for j in range(n):
        print("*",end = ' ')
    print()

# Q4. Print a number triangle pattern  
for i in range(1,6):
    for j in range(1,6):
        if i >= j :
            print(j,end=' ')
    print()
