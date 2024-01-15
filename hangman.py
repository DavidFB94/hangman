import os
import random
import string
import time
import colorama
from colorama import Fore, Back, Style
from simple_term_menu import TerminalMenu
from words import words
from animals import animals
from countries import countries
from food import foods


colorama.init(autoreset=True)


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def select_category():
    print('Use the up/down arrow keys to cycle the options, ENTER to select,')
    print('or press a number key\n')
    print('Pick your category:\n')
    options = ["[1] Mixed Words", "[2] Animals", "[3] Countries", "[4] Food & drinks"]
    terminal_menu = TerminalMenu(options)
    menu_number = terminal_menu.show()
    clear()
    print(f"You have selected {Fore.CYAN}{options[menu_number]}{Fore.RESET}!")
    if menu_number == 0:  # mixed words
        return words
    elif menu_number == 1:  # animals
        return animals
    elif menu_number == 2:  # countries
        return countries
    elif menu_number == 3:  # food & drinks
        return foods


def get_valid_word():
    category = select_category()
    # randomly chooses a word from the chosen category list
    word = random.choice(category)
    # checks the word for spaces or hyphens
    while '-' in word or ' ' in word:
        word = random.choice(category)

    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    word_length = len(word)

    lives = None

    if word_length <= 4:
        lives = 8
    elif 4 < word_length <= 8:
        lives = 7
    else:
        lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used and lives remaining
        l = 'lives'
        if lives == 1:
            l = 'life'
        print(f'\nYou have {Style.BRIGHT}{Fore.MAGENTA}{lives} {l}{Fore.RESET}{Style.RESET_ALL} left and you have used these letters:', end=' ')
        for letter in used_letters:
            print(f'{Fore.YELLOW}{letter}', end=' ')

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('\n\nCurrent word:', ' '.join(word_list))

        # getting user input
        user_letter = input('\nGuess a letter: ').upper()
        clear()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f'{Fore.GREEN}{user_letter} is in the word{Fore.RESET}')

            else:
                lives = lives - 1 #takes away a life if wrong
                print(f'{Fore.RED}{user_letter} is not in the word{Fore.RESET}')

        elif user_letter in used_letters:
            print(f'You have already used {user_letter}. Try again.')

        else:
            print(f'{user_letter} is invalid. Please use alphabetical letters.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        clear()
        print(f'{Fore.RED}You died{Fore.RESET}\n')
        print(f'The word was {Style.BRIGHT}{Fore.GREEN}{word}{Fore.RESET}{Style.RESET_ALL}.\n')
    else:
        clear()
        print(f'{Fore.GREEN}You won!\n')
        print(f'You found the word: {Style.BRIGHT}{Fore.GREEN}{word}{Fore.RESET}{Style.RESET_ALL}!!!\n')
        print(f'You had {Style.RESET_ALL}{Fore.MAGENTA}{lives} {l}{Fore.RESET}{Style.RESET_ALL} remanining.\n')


def play_again():
    again = True
    while True:
        user_input = input(f'Do you want to {Style.BRIGHT}{Fore.BLUE}play again?{Style.RESET_ALL}{Fore.RESET} y/n + ENTER: ').lower()
        clear()
        if user_input == 'y':
            break
        elif user_input == 'n':
            again = False
            print(f'Thank you for playing {Style.BRIGHT}HANGMAN{Style.RESET_ALL}!')
            time.sleep(3)
            clear()
            break
        else:
            print(f'{user_input} is invalid. Please use the correct input.')
    return again


def start_game():
    """
    Run game function. Displays welcome message with rules.
    Requests user input to start game.
    Stops game if play_again() returns again as False.
    If again = True, restarts the game.
    """
    print(f'Welcome to {Style.BRIGHT}HANGMAN{Style.RESET_ALL}!\n')
    print(f'The goal of the game is to find the {Fore.GREEN}word{Fore.RESET} that the computer has selected.\n')
    print(f'The {Fore.GREEN}word{Fore.RESET} will be represented by dashes. You find the {Fore.GREEN}word{Fore.RESET} by guessing\n one {Fore.YELLOW}letter{Fore.RESET} at a time. You can only guess a {Fore.YELLOW}letter{Fore.RESET} once.\n')
    print(f'Guessing a {Fore.YELLOW}letter{Fore.RESET} {Fore.GREEN}correctly{Fore.RESET} will display the {Fore.YELLOW}letter{Fore.RESET} in its position.\n An {Fore.RED}incorrect{Fore.RESET} guess will cost you one {Fore.MAGENTA}life{Fore.RESET}.\n')
    print(f'When you run out of {Style.RESET_ALL}{Fore.MAGENTA}lives{Fore.RESET}{Style.RESET_ALL}, you {Fore.RED}die{Fore.RESET}.\n')
    print(f'{Style.BRIGHT}Good luck, and have fun!\n')
    while True:
        user_input = input(f'Press {Back.WHITE}{Style.BRIGHT} ENTER {Style.RESET_ALL}{Back.RESET} to start')
        clear()
        # simulating game loading
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
