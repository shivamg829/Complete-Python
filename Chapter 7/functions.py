# Functions
def avg(a, b):
    return (a + b) / 2

print(avg(10, 30))
print(avg(10, 20))
print(avg(40, 20))

# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
