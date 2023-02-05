rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
cpu_choice = random.randint(0, 2)

if player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print(rock)

print("Computer chose:")
if cpu_choice == 1:
    print(paper)
elif cpu_choice == 2:
    print(scissors)
else:
    print(rock)

if player_choice == cpu_choice:
    print("Tie Game")
elif player_choice == 0 and cpu_choice == 1:
    print("You lose. Paper beats Rock")
elif player_choice == 1 and cpu_choice == 2:
    print("You lose. Scissors beats Paper")
elif player_choice == 2 and cpu_choice == 0:
    print("You lose. Rock beats Scissors")
elif player_choice == 0 and cpu_choice == 2:
    print("You win. Rock beats Scissors")
elif player_choice == 1 and cpu_choice == 0:
    print("You win. Paper beats Rock")
elif player_choice == 2 and cpu_choice == 1:
    print("You win. Scissors beats Paper")
else:
    print("You chose an invalid number. Try again.")
