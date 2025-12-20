# Day 14 – File Handling in Python

#1. Write text to a file
'''
Create sample.txt
Write your name and a sentence
'''
file = open("sample.txt","w")
file.write("Hello I am Pranavi, and i am Learning File Handling !!!")
file.close()
print("Written File Successfully !!!")

#2. Read text from a file
'''
Read and print content
'''
file = open("sample.txt","r")
print("Reading a File :",file.read())
file.close()

#3. Append text to the file
file = open("sample.txt","a")
file.write("\nI am adding New Line !!!")
file.close()

#4. Read updated content
file = open("sample.txt","r")
print(file.read())
file.close()

#5. Use with statement

print("\nReading file using with statement:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)