# List
list = ["Rolf", "Bob", "Jen", False, 42, 3.14]
print(list[0])  # Output: Rolf
print(list[1])  # Output: Bob
print(list[2])  # Output: Jen
print(list[3])  # Output: False
print(list[4])  # Output: 42
print(list[5])  # Output: 3.14

# List Methods
list.append("Smith")  # Adds "Smith" to the end of the list
print(list)  # Output: ['Rolf', 'Bob', 'Jen', False, 42, 3.14, 'Smith']
list.remove("Bob")  # Removes "Bob" from the list
print(list)  # Output: ['Rolf', 'Jen', False, 42, 3.14, 'Smith']
list.insert(1, "Alice")  # Inserts "Alice" at index 1
print(list)  # Output: ['Rolf', 'Alice', 'Jen', False, 42, 3.14, 'Smith']
list.sort()  # Sorts the list in ascending order
print(list)  # Output: ['Alice', 'Jen', 'Rolf', 'Smith', 3.14, 42, False]
list.reverse()  # Reverses the order of the list
print(list)  # Output: [False, 42, 3.14, 'Smith', 'Rolf', 'Jen', 'Alice']    

# Can change the values of a list
list[0] = "Charlie"  # Changes the first element to "Charlie"
print(list)  # Output: ['Charlie', 42, 3.14, 'Smith', 'Rolf', 'Jen', 'Alice']