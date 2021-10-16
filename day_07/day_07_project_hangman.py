import random
import hangman_words
import hangman_art
import os
clear = lambda: os. system('cls')
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
#Testing Code
print(f"Pssst, the solution is {chosen_word}")
lives = 6
endgame = False

display = []
guesses = []
for l in range(0,len(chosen_word)):
    display += "_"
print(display)

while not endgame:
    guess_letter = input("Guess a letter: ").lower()
    clear()
    print(hangman_art.stages[lives])
    print(display)
    if guess_letter not in chosen_word:
        lives -= 1
        print(f"You guessed [{guess_letter}], that's not in the word. You lose a life.")
    if guess_letter in guesses:
        print(f"You've already guessed [{guess_letter}]")
        continue
    else:
        guesses.append(guess_letter)

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if guess_letter == letter:
            display[position] = letter
    
    if lives == 0:
        print("You lose.")
        print(hangman_art.stages[lives])
        endgame = True
            
    
    if "_" not in display:
        endgame = True
        print("You win.")
