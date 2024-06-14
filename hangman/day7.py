""" Hangman """
import random
from hangman_words import word_list
from hangman_art import logo, stages

playing = False
chosen_word = random.choice(word_list)
lives = 6
display = [];
word_length = len(chosen_word)

print(logo)

for _ in range(word_length):
    display.append("_")

while not playing:
    guess = input("Guess a letter.\n").lower()
    
    if guess in display:
      print(f"Letter {guess} has already been used. Please choose another letter.")

    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess
            print(display)
      
    if "_" not in display:
        playing = True
        print("You win!")      
    
    if guess not in chosen_word:
        print(f"The letter {guess} is not in word.")
        lives -= 1
        if lives == 0:
            playing = True
            print("You lose!")
    print(stages[lives])
    
print(display)
print(chosen_word)