# Types
n : int = 10
name : str = "Advance"

def greet() -> str:
    return f"Hello, {name}! You have {n} new messages."
print(greet())

def add_numbers(a: int, b: int) -> int:
    return a + b
print(add_numbers(5, 7))

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed.") 