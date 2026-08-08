# Guess the number game
import random
n = random.randint(1, 100)
print("Welcome to the Guess the Number Game!")
a = -1
guess_count = 0
while a != n:
    a = int(input("Guess a number between 1 and 100: "))
    guess_count += 1
    if a < n:
        print("Too low! Try again.")
    elif a > n:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
print(f"It took you {guess_count} guesses to find the number.")