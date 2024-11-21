print("""          _                                     _     _                 _ 
         | |                                   (_)   | |               | |
         | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
         | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
         | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
          \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|\n""")
print("                        WELCOME TO TREASURE ISLAND.             ")
print("                    Your mission is to find the treasure.")
step_1 = input("You're at a cross road, Where do you want to go? Type left or right.\n")
lowercase = step_1.lower()
if lowercase == "right":
    print("You fell into a hole. Game Over.")
elif lowercase == "left":
    step_2 = input("'You've' come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. type 'swim' to swim across.\n")
    lowercase1 = step_2.lower()
    if lowercase1 == "swim":
        print("You got attacked by an angry trout. Game Over.")
    elif lowercase1 == "wait":
        step_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        lowercase2 = step_3.lower()
        if lowercase2 == "yellow":
            print("You found the treasure! You win!")
        elif lowercase2 == "red":
            print("Its a room full of fire. Game Over.")
        elif lowercase2 == "blue":
            print("Its a room full of fire. Game Over.")
        else:
            print("Invalid input.")
    else:
            print("Invalid input.")
else:
            print("Invalid input.")