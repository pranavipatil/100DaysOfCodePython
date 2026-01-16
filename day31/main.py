# Day 31 – Number Practice Programs

#1. Checked even or odd number
n = int(input("Enter Any Number: "))
if n % 2 == 0:
    print("Given number is even number")
else:
    print("Given number is odd number")

#2. Checked positive or negative number
n = int(input("Enter Any Number: "))
if n > 0:
    print("Given Number is Positive number")
elif n < 0:
    print("Given Number is Negative number")
else:
    print("Given Number is Zero")

#3. Found sum of digits
n = int(input("Enter Any Number: "))
res = 0
while n > 0:
    digit = n % 10
    res += digit
    n //= 10
print(res)

#4. Reversed a number
n = int(input("Enter Any Number: "))
rev = 0
while n > 0:
    res = n % 10
    rev = rev * 10 + res
    n//=10
print(rev)
