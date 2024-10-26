import random as r
from move import *

moves = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
c_choice = r.randint(0, 2)

print(moves[user_choice])
print("\n Its now computer turn: ")
print(moves[c_choice])

if (user_choice == 0 and c_choice == 0):
    print("Its a Draw!\n")
elif user_choice == 1 and c_choice == 1:
    print("Its a Draw!\n")
elif (user_choice == 2 and c_choice == 2):
    print("Its a Draw!\n")

if (user_choice == 0 and c_choice == 1):
    print("Computer wons the match!")
elif (user_choice == 0 and c_choice == 2):
    print("You won the match!\n")

elif (user_choice == 1 and c_choice == 0):
    print("You won the match!\n")
elif (user_choice == 1 and c_choice == 2):
    print("You won the match!\n")

elif (user_choice == 2 and c_choice == 0):
    print("Its a Draw!\n")
elif (user_choice == 2 and c_choice == 1):
    print("You won the match!\n")


