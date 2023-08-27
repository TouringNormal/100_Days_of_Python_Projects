import random
import os
from hangman_art import stage, logo
from hangman_words import word_list



print(logo)
clear = lambda: os.system('cls')
chosen_word = random.choice(word_list)

print(chosen_word)
word = []
for blank in chosen_word:
    word += ('_')
print(word)
length = len(chosen_word)

lives = 6
game_end = False
while game_end != True:

    guess = input ("Guess a letter: ").lower() 

    for position in range(0, length):
        letter = chosen_word[position]
        if letter == guess:
            word[position] = letter
            clear()
            print(word)


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
                game_end = True
                print("You lost!")
        print(stage[lives])

    if "_" not in word:
        game_end = True        
        print("You win!")
