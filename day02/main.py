# Day 02 - Input & Type Conversion

# Taking user input
name = input("Enter your name: ")

# Taking age (needs to conversion)
age = int(input("Enter your age: "))

# Taking percentage (float conversion)
percentage = float(input("Enter your percentage: "))

# Printing information
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)

# A small calculation
next_year_age = age + 1
print(f"Next year you will be {next_year_age} years old.")


