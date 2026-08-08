# Strings: String is immutable, which means that once a string is created, it cannot be changed. However, you can create a new string based on the original string.
name = "Shivam"
nameshort  = name[2:5]  # Create a new string by slicing the original string
print(nameshort)  # Output: iva
# Negative Slicing
name = "Shivam"
nameshort = name[-4:-1]  # Create a new string by slicing the original string using negative indices
print(nameshort)  # Output: iva
# Slicing with skip
name = "Shivam"
nameshort = name[0:6:2]  # Create a new string by slicing the original string with a step of 2
print(nameshort)  # Output: Siv


# Negative indexing
name = "Shivam"
print(name[-1])  # Output: m

# String Methods: Python provides a variety of built-in methods for string manipulation. Here are some commonly used string methods:
# 1. len(): Returns the length of the string.
name = "Shivam"
print(len(name))  # Output: 6   
# 2. upper(): Converts all characters in the string to uppercase.
name = "Shivam"
print(name.upper())  # Output: SHIVAM
# 3. lower(): Converts all characters in the string to lowercase.
name = "Shivam"
print(name.lower())  # Output: shivam
# 4. strip(): Removes leading and trailing whitespace from the string.
name = "   Shivam   "
print(name.strip())  # Output: Shivam
# 5. replace(): Replaces a specified substring with another substring.
name = "Shivam"
print(name.replace("Shivam", "Shiva"))  # Output: Shiva
# 6. split(): Splits the string into a list of substrings based on a specified delimiter.
name = "Shivam is a good boy"
print(name.split())  # Output: ['Shivam', 'is', 'a', 'good', 'boy']     
# 7. endswith(): Checks if the string ends with a specified suffix.
name = "Shivam"
print(name.endswith("am"))  # Output: True
# 8. startswith(): Checks if the string starts with a specified prefix.
name = "Shivam"
print(name.startswith("Shi"))  # Output: True
# 9.Capitalize(): Capitalizes the first character of the string.
name = "shivam"
print(name.capitalize())  # Output: Shivam
# 10. count(): Returns the number of occurrences of a specified substring in the string.
name = "Shivam is a good boy"
print(name.count("a"))  # Output: 2


# Excape Sequences: Escape sequences are special characters that are used to represent certain characters in a string. Here are some commonly used escape sequences:
# 1. \n: Represents a new line.
print("Hello\nWorld")  # Output:
# Hello
# World
# 2. \t: Represents a tab.
print("Hello\tWorld")  # Output: Hello   World   
