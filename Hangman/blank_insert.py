import random
import hangman_words
list = ["camel", "lion", "elephant"]
chosen_word = random.choice(hangman_words.list)
word_length = len(chosen_word)
lives = 6
from handman_art import logo, HANGMANPICS
print(logo)
display = []
for _ in range(word_length):
    display += "_"
end = False
while not end:
    guess = input(" guess a letter: ").lower()
    if guess in display:
      print(f"You've already guessed {guess}")
    for g in range(word_length):
        letter = chosen_word[g]
        if letter == guess:
            display[g] = letter
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives == 0:
            end = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end = True
        print("You Win")
    print(HANGMANPICS[lives])
