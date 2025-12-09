# Day 03 – Strings in Python

## Take your name as a string
n = "Pranavi Patil"

### printing First character using indexing 
print(n[0])

### printing Last character using indexing
print(n[-1])

### printing First 4 character using sclicing
print(n[:4:1])

### printing Last 3 character using sclicing
print(n[10::1])

## Apply these string methods 

### Convert to uppercase
print(n.upper())

### Convert to Lowercase
print(n.lower())

### Replace a letter (example: replace 'a' with '@')
print(n.replace("a","@"))

### Remove extra spaces (use strip())
print(n.strip())

## Print the total length of your name
print(len(n))