s = set() # Create an empty set
s = {1, 3, 4, 1, 3, "Shivam"}
print(s, type(s))  # Output: {1, 3, 4, 'Shivam'} <class 'set'>

# Methods
# 1. add()
s.add(5)
print(s)  # Output: {1, 3, 4, 5, 'Shivam'}
# 2. remove()
s.remove(3)
print(s)  # Output: {1, 4, 5, 'Shivam'}
# 3. discard()
s.discard(4)
print(s)  # Output: {1, 5, 'Shivam'}    

# union
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)  # Output: {1, 2, 3, 4, 5}

# intersection
s4 = s1.intersection(s2)
print(s4)  # Output: {3}