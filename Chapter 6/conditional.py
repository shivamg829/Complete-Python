# Conditional statements
a = int(input("Enter a Age: "))

if a >= 18:
    print("You are eligible to vote.")
elif a < 0:
    print("Age cannot be negative.")
else:
    print("You are not eligible to vote.")  
