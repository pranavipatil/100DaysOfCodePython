# Day 19 – JSON Handling in Python

#1. Convert Python dict to JSON string
import json
data = {"name":"Pranavi","age":22,"course":"Python"}
json_str = json.dumps(data)
print(json_str)

#2. Convert JSON string to Python dict
json_str = '{"name":"Pranavi","age":22,"course":"Python"}'
data = json.loads(json_str)
print(data)

#3. Write dictionary to JSON file
data = {"name":"Pranavi","age":22,"course":"Python"}
with open("data.json","w") as file:
    json.dump(data,file)

#4. Read dictionary from JSON file
with open("data.json","r") as f:
    data_from_file = json.load(f)
    print(data_from_file)

