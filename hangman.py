import os
import random
import string
import time
from simple_term_menu import TerminalMenu
from words import words
from animals import animals
from countries import countries
from food import foods


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def select_category():
    print('Use the up/down arrow keys to cycle the options, ENTER to select,')
    print('or press a number key\n')
    print('Pick your category:\n')
    options = ["[1] Mixed Words", "[2] Animals", "[3] Countries", "[4] Food"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    clear()
    print(f"You have selected {options[menu_entry_index]}!")
    return menu_entry_index


def get_valid_word():
    menu_entry_index = select_category()
    # selects which list to pick a word from, based on selected category
    if menu_entry_index == 0:
        word = random.choice(words)
    elif menu_entry_index == 1:
        word = random.choice(animals)
    elif menu_entry_index == 2:
        word = random.choice(countries)
    elif menu_entry_index == 3:
        word = random.choice(foods)
    # randomly chooses a word from the chosen category list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used and lives remaining
        l = 'lives'
        if lives == 1:
            l = 'life'
        print(f'\nYou have {lives} {l} left and you have used these letters:', end=' ')
        for letter in used_letters:
            print(letter, end=' ')

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('\nCurrent word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        clear()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f'{user_letter} is in the word.')

            else:
                lives = lives - 1 #takes away a life if wrong
                print(f'{user_letter} is not in the word.')

        elif user_letter in used_letters:
            print(f'You have already used {user_letter}. Please try again.')

        else:
            print(f'{user_letter} is invalid. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word + '.')
    else:
        print('You guessed the word', word, '!!')


def play_again():
    again = True
    while True:
        user_input = input('Do you want to play again? y/n: ').lower()
        clear()
        if user_input == 'y':
            break
        elif user_input == 'n':
            again = False
            print('Thank you for playing Hangman!')
            time.sleep(3)
            clear()
            break
        else:
            print(f'{user_input} is invalid. Please try again.')
    return again


def start_game():
    print('Welcome to hangman!\n')
    print('The goal of the game is to find the word that the computer has selected.\n')
    print('The word will be represented by dashes. You find the word by guessing\n one letter at a time. You can only guess a letter once.\n')
    print('Guessing a letter correctly will display the letter in its position.\n An incorrect guess will cost you one life.\n')
    print('Good luck, and have fun!\n')
    while True:
        user_input = input('Press ENTER to start')
        clear()
        print('Loading game...')
        time.sleep(1)
        clear()
        hangman()
        again = play_again()
        if not again:
            break


if __name__ == '__main__':
    clear()
    start_game()
