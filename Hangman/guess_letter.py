import random
list = ["camel", "lion", "elephant"]
chosen_word = random.choice(list)
guess = input("guess a letter: ").lower()
for g in chosen_word:
    if g == guess :
        print("right")
    else:
        print("wrong")
print(chosen_word)