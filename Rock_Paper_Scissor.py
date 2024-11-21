Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
inpt = int(input("What do you choose? Type 0 for Rock, 1 for Paper & 2 for Scissors.\n"))
if inpt == 0:
    print(Rock)
elif inpt == 1:
    print(Paper)
elif inpt == 2:
    print(Scissors)
else:
    print("Invalid option.")
print(inpt)
print("Computer")
import random
random_move = random.randint(0, 2)
if random_move == 0:
    print(Rock)
elif random_move == 1:
    print(Paper)
elif random_move == 2:
    print(Scissors)
else:
    print("Invalid option.")
print(random_move)

if inpt == 0 and random_move == 1:
    print("Computer wins")
elif inpt == 0 and random_move == 2:
    print("You win")
elif inpt == 1 and random_move == 0:
    print("You win")
elif inpt == 1 and random_move == 2:
    print("Computer wins")
elif inpt == 2 and random_move == 0:
    print("Computer wins")
elif inpt == 2 and random_move == 1:
    print("You win")
else:
    print("Draw")