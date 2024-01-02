import random
from words import words
import string

def get_valid_word(words):
    # randomly chooses something from the list
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character(s). Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word + '.')
    else:
        print('You guessed the word', word, '!!')


print('Welcome to hangman!\n')
print('The goal of the game is to find the word that the computer has selected.\n')
print('The word will be represented by dashes. You find the word by guessing one letter at a time. You can only guess a letter once.\n')
print("Guessing a letter correctly will display the letter in it's position. An incorrect guess will cost you one life.\n")
print('Good luck, and have fun!\n')

def startGame():
    while True:
        user_input = input('Type "start" to begin: ')
        if user_input == 'start' or user_input == 'Start':
            hangman()
            break
        else:
            print('Invalid input.')

startGame()
