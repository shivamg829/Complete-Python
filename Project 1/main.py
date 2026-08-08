'''
1 for snake 
-1 for water 
0 for gun
'''
# Game logic: Snake drinks water, Water douses gun, Gun kills snake
computer = -1
you = input("Enter your choice (1 for snake, -1 for water, 0 for gun): ")
youDict = {"1": "snake", "-1": "water", "0": "gun"}
if you not in youDict:
    print("Invalid choice. Please enter 1, -1, or 0.")
else:
    you = int(you)
    print(f"You chose: {youDict[str(you)]}")
    print(f"Computer chose: {youDict[str(computer)]}")

    if you == computer:
        print("It's a tie!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")
    else:
        print("Computer wins!")