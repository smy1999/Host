import random

print("1.Rock 2.Scissors 3.Paper")
player_choice = int(input("Input your choice : "))
print(player_choice)
bot_choice = random.randint(1, 3)
print("Your choice is ", end='')
if player_choice == 1:
    print("rock.")
elif player_choice == 2:
    print("scissors.")
else:
    print("paper.")
print("Bot choice is ", end='')
if bot_choice == 1:
    print("rock.")
elif bot_choice == 2:
    print("scissors.")
else:
    print("paper.")
if bot_choice - player_choice == 1:
    print("You win, I lose.")
elif bot_choice - player_choice == -1:
    print("You lose, I win.")
else:
    print("We draw.")
