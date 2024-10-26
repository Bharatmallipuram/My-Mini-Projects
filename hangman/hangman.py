from logo import *
from words import *
import random as r

print(logo)

main_word = r.choice(word_list)
#print(main_word)

check = ['_']*len(main_word)
c = ' '.join(check)
print(f"\nThe WORD IS: {c}")
print(f"IT IS AN {len(check)} LETTER WORD!")

count = 1
life = 6
while life >= 0:
    user_choice = input("\nGUESS THE LETTER BEFORE HANGMAN DIES \"ENTER LETTER IN LOWER-CASE\":  ")

    if user_choice in main_word:
        for i in range (0, len(main_word)):
            if user_choice == main_word[i]:
                check[i] = user_choice 
                c = " ".join(check)
                print(c)
                if "_" not in check:
                    print("\nGAME OVER U WON!!!")
                    print("YOU SAVED THE HANGMAN :)")
                    life = -1
    else:
        print(f"{stages[life]}\n")
        life -= 1
        print(c)

if "_" in check:
    print("\nGAME OVER U LOST!!!")
    print(F"THE HANGMAN DIED :( \n\nTHE WORD IS: {main_word}\n")
    

# import tkinter as tk
# from tkinter import messagebox
# import random as r
# from logo import logo, stages    
# from words import word_list

# class HangmanGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Hangman Game")
#         self.main_word = r.choice(word_list)
#         self.check = ['_'] * len(self.main_word)
#         self.life = 6

#         # Create widgets
#         self.logo_label = tk.Label(root, text=logo, font=("Courier", 16))
#         self.logo_label.pack()

#         self.word_label = tk.Label(root, text=" ".join(self.check), font=("Courier", 20))
#         self.word_label.pack()

#         self.instruction_label = tk.Label(root, text=f"IT IS A {len(self.check)} LETTER WORD!", font=("Courier", 16))
#         self.instruction_label.pack()

#         self.entry = tk.Entry(root, font=("Courier", 16))
#         self.entry.pack()
#         self.entry.bind("<Return>", self.guess_letter)

#         self.hangman_label = tk.Label(root, text=stages[self.life], font=("Courier", 16))
#         self.hangman_label.pack()

#         self.message_label = tk.Label(root, font=("Courier", 16))
#         self.message_label.pack()

#     def guess_letter(self, event=None):
#         user_choice = self.entry.get().lower()
#         self.entry.delete(0, tk.END)

#         if not user_choice or len(user_choice) != 1 or not user_choice.isalpha():
#             messagebox.showwarning("Invalid Input", "Please enter a single letter.")
#             return

#         if user_choice in self.main_word:
#             for i in range(len(self.main_word)):
#                 if user_choice == self.main_word[i]:
#                     self.check[i] = user_choice
#             self.word_label.config(text=" ".join(self.check))
#             if "_" not in self.check:
#                 self.message_label.config(text="GAME OVER! YOU WON!!!\nYOU SAVED THE HANGMAN :)")
#                 self.entry.config(state=tk.DISABLED)
#         else:
#             self.life -= 1
#             self.hangman_label.config(text=stages[self.life])
#             if self.life < 0:
#                 self.message_label.config(text=f"GAME OVER! YOU LOST!!!\nTHE HANGMAN DIED :( \nTHE WORD WAS: {self.main_word}")
#                 self.entry.config(state=tk.DISABLED)

# if __name__ == "__main__":
#     root = tk.Tk()
#     game = HangmanGame(root)
#     root.mainloop()

