# Dictionary
marks = {
    "Shivam": 90,
    "Rohit": 85,
    "Amit": 95,
}
print(marks, type(marks))  # Output: {'Shivam': 90, 'Rohit': 85, 'Amit': 95} <class 'dict'>

# Methods
# 1. keys()
print(marks.keys())  # Output: dict_keys(['Shivam', 'Rohit', 'Amit'])
# 2. values()
print(marks.values())  # Output: dict_values([90, 85, 95])
# 3. items()
print(marks.items())  # Output: dict_items([('Shivam', 90), ('Rohit', 85), ('Amit', 95)])
# 4. get()
print(marks.get("Shivam"))  # Output: 90            
# 5. update()
marks.update({"Rohit": 88, "Amit": 97})
print(marks)  # Output: {'Shivam': 90, 'Rohit': 88, 'Amit': 97}
# 6. pop()
marks.pop("Amit")
print(marks)  # Output: {'Shivam': 90, 'Rohit': 88}
# 7. popitem()
marks.popitem()
print(marks)  # Output: {'Shivam': 90}