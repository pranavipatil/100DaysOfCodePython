# Day 32 – String Practice Programs

#1. Find length of a string
n = input("Enter Any String: ")
print(len(n))

# #2. Reversed a string
n = input("Enter String: ")
rev = ''
for i in n:
    rev = i + rev
print(rev)

#3. Counted vowels in a string
n = input("Enter String: ")
count = 0
for i in n:
    if i in 'aeiouAEIOU':
        count += 1
print(count)

#4. Checked palindrome string
n = input("Enter String: ")
rev = ''
for i in n:
    rev = i + rev
if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")