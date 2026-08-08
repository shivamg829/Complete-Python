# Tuple with one element
my_tuple = (42,)
print(my_tuple)  # Output: (42,)

# Tuple with multiple elements
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
print(my_tuple[2])  # Output: 3 

# Can't change the values of a tuple
# my_tuple[0] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment

# Methods for tuples
# Tuples have fewer methods than lists because they are immutable
print(my_tuple.count(2))  # Output: 1 (counts the occurrences of 2 in the tuple)
print(my_tuple.index(3))  # Output: 2 (returns the index of the first occurrence of 3 in the tuple)
