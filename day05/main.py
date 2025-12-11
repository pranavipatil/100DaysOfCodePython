# Day 05 – Loops (for & while)

# 1. Print numbers from 1 to 10 using while loop and for loop

# While Loop:
n = 1
while n <= 10:
    print(n ,end =' ')
    n+=1

# For Loop:
for i in range(1,11):
    print(i, end = ' ')


# 2. Print even numbers between 1–20 using While and For Loop

# While Loop:
n = 1
while n <= 20:
    if n % 2 == 0:
         print(n,end = ' ')
    n+=1
print()

#For Loop:
for i in range(1,21):
     if i % 2 == 0:
          print(i,end=' ')

# 3.  Print the table of a given number using While and For Loop

# While Loop:
n = int(input("Enter ANy number : "))
i = 1
while i <= 10:
     print(n * i,end=' ')
     i+=1
print()

# For Loop:
n = int(input("Enter Any Number : "))
for i in range(1,11):
     print(n*i,end=' ')

# 4. Sum of first 10 natural numbers using While and For Loop

# While Loop:
sum = 0
n = 1
while n <= 10:
     sum += n
     n += 1
print(sum)

# For Loop:
sum = 0
for i in range(1,11):
     sum += i
print("sum = ",sum)

# 5.Print a countdown from 10 to 1 using while and For loop

# While Loop:
i = 10
while i >= 1:
    print(i)
    i-=1

# For Loop:
for i in range(10,0,-1):
    print(i)
