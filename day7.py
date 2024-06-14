""" Hangman """
import random 

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = [];
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")

#TODO-1: 
# Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' 
# has no more blanks ("_"). Then you can tell the user they've won.

guess = input("Guess a letter.\n").lower()

for i in range(word_length):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)