# Day 10 – Dictionaries in Python

#Q1. Create a dictionary with student details
student = {"name":"Pranavi","age":22,"course":"Python","Marks":85}
print("Original Dictionary :",student)

#Q2. Access values using keys
print("Access Name :",student["name"])
print("Access Marks :",student["Marks"])

#Q3. Add and update key–value pairs
student["Loc"] = "pune"
print("Add new Element :",student)

student["Marks"] = 90
print("Update Marks :",student)

#Q4. Remove a key from dictionary
print("Remove Element :",student.pop("Loc"))

#Q5. Iterate through dictionary
'''
Print all keys
Print all values
Print key-value pairs
'''
print("All Keys :",student.keys())
print("All Values :",student.values())
print("All Key-Value ",student.items())

#Q6. Find length of dictionary
print("Length of Dict :",len(student))

