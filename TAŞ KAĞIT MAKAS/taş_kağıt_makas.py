# Rock Paper Scissors ASCII Art

import random

# #Rock
tas='''
     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# # Paper
kagit='''
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''

# # Scissors
makas='''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# #--------------------------------------------------------------------------------
choices = [tas, kagit, makas]

user_choice = int(input("Make your selection: 0 for Rock, 1 for Paper, or 2 for Scissors? \n"))

if user_choice < 0 or user_choice >= 3:
     print("Yanlış seçim, üzgünüm kaybettin.")
else:
     print("Sen seçimini yaptın!")
     print(choices[user_choice])

     computer_choice = random.randint(0, 2)
     print("Bilgisayarın seçimi:")
     print(choices[computer_choice])

     # Sonuç belirleme
     if user_choice == computer_choice:
         print("Berabere!")
     elif (user_choice == 0 and computer_choice == 2) or \
          (user_choice == 1 and computer_choice == 0) or \
          (user_choice == 2 and computer_choice == 1):
         print("Tebrikler, kazandın!")
     else:
         print("Kaybettin!")
