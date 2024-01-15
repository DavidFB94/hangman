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

# auto-resets styling after each row
colorama.init(autoreset=True)


def clear():
    """
    Clear function to clean-up the terminal to avoid text clutter.
    """
    os.system("cls" if os.name == "nt" else "clear")


def select_category():
    """
    Category selection. Presents a simple terminal menu
    and instructions how to navigate it.
    Returns the selected category for use in get_valid_word().
    """
    print('Use the up/down arrow keys to cycle the options, ENTER to select,')
    print('or press a number key\n')
    print('Pick your category:\n')
    options = [
        "[1] Mixed Words", "[2] Animals", "[3] Countries", "[4] Food & drinks"
    ]
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
    """
    Pulls word from category list, based on selected category.
    Checks that the word is one word, with no spaces or hyphens.
    Returns a valid word from the category list, in uppcase.
    """
    category = select_category()
    # randomly chooses a word from the chosen category list
    word = random.choice(category)
    # checks the word for spaces or hyphens
    while '-' in word or ' ' in word:
        word = random.choice(category)

    return word.upper()


def hangman():
    """
    Main game function. Sets lives and displays the word as dashes.
    Calls for user input to guess letters, and displays feedback messages.
    """
    word = get_valid_word()
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    word_length = len(word)

    lives = None

    # set lives depending on word length
    if word_length <= 4:
        lives = 8
    elif 4 < word_length <= 8:
        lives = 7
    else:
        lives = 6

    while len(word_letters) > 0 and lives > 0:
        # displays lives as pluras or singular, based on lives remaining
        lives_or_life = 'lives'
        if lives == 1:
            lives_or_life = 'life'
        # letters used and lives remaining
        print(
            f'\nYou have {Style.BRIGHT}{Fore.MAGENTA}{lives} '
            f'{lives_or_life}{Style.RESET_ALL} left '
            'and you have used these letters:',
            end=' '
        )
        for letter in used_letters:
            print(f'{Fore.YELLOW}{letter}', end=' ')

        # current word progress (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word
        ]
        print('\n\nCurrent word:', ' '.join(word_list))

        # getting user input and feedback messages
        user_letter = input('\nGuess a letter: ').upper()
        clear()
        # checks if the guessed letter is in the word, if the character is
        # from the alphabet, removes if from word_letters,
        # and adds it to used_letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # feedback if guess was correct
                print(f'{Fore.GREEN}{user_letter} is in the word{Fore.RESET}')

            else:
                # takes away a life if wrong, and alerts the user
                lives = lives - 1
                print(
                    f'{Fore.RED}{user_letter} is not in the word'
                )

        # input alert and if letter has already been used
        elif user_letter in used_letters:
            print(
                f'{Fore.RED}You have already used {user_letter}. '
                f'Try again.'
            )

        else:
            print(
                f'{Fore.RED}{user_letter} is invalid. '
                'Please use alphabetical letters.'
            )

    # gets here when len(word_letters) == 0 OR when lives == 0
    # end of game messages
    if lives == 0:
        clear()
        print(f'{Fore.RED}You died{Fore.RESET}\n')
        print(
            'The word was '
            f'{Style.BRIGHT}{Fore.GREEN}{word}{Style.RESET_ALL}.\n'
        )
    else:
        clear()
        print(f'{Fore.GREEN}You won!\n')
        print(
            'You found the word: '
            f'{Style.BRIGHT}{Fore.GREEN}{word}{Style.RESET_ALL}!\n'
        )
        print(
            'You had '
            f'{Style.BRIGHT}{Fore.MAGENTA}{lives} '
            f'{lives_or_life}{Style.RESET_ALL} remanining.\n'
        )


def play_again():
    """
    Request user input (lowercase) when game is ended.
    If y, return again as True.
    If n, return again as False.
    If n, display exiting game message.
    """
    again = True
    while True:
        user_input = input(
            f'Do you want to {Style.BRIGHT}{Fore.BLUE}play again?'
            f'{Style.RESET_ALL} y/n + ENTER: '
        ).lower()
        clear()
        if user_input == 'y':
            break
        elif user_input == 'n':
            again = False
            print(
                'Thank you for playing '
                f'{Style.BRIGHT}HANGMAN{Style.RESET_ALL}!'
            )
            time.sleep(3)
            clear()
            break
        else:
            # input alert message
            print(
                f'{Fore.RED}{user_input} is invalid. '
                'Please use the correct input.\n'
                )
    return again


def start_game():
    """
    Run game function. Displays welcome message and rules.
    Requests user input to start game.
    Stops game if play_again() returns again as False.
    If again = True, restarts the game.
    """
    print(f'Welcome to {Style.BRIGHT}HANGMAN{Style.RESET_ALL}!\n')
    print(
        'The goal of the game is to find the '
        f'{Fore.GREEN}word{Fore.RESET} that the computer has selected.\n'
    )
    print(
        f'The {Fore.GREEN}word{Fore.RESET} will be represented by dashes. '
        f'You find the {Fore.GREEN}word{Fore.RESET} by guessing\n'
        f'one {Fore.YELLOW}letter{Fore.RESET} at a time. '
        f'You can only guess a {Fore.YELLOW}letter{Fore.RESET} once.\n'
    )
    print(
        f'Guessing a {Fore.YELLOW}letter{Fore.RESET} '
        f'{Fore.GREEN}correctly{Fore.RESET} will display the '
        f'{Fore.YELLOW}letter{Fore.RESET} in its position.\n'
        f'An {Fore.RED}incorrect{Fore.RESET} guess will cost you one '
        f'{Style.BRIGHT}{Fore.MAGENTA}life{Style.RESET_ALL}.\n'
    )
    print(
        'When you run out of '
        f'{Style.BRIGHT}{Fore.MAGENTA}lives{Style.RESET_ALL}, '
        f'you {Fore.RED}die{Fore.RESET}, and the game ends.\n'
        f'If you guess the {Fore.GREEN}word{Fore.RESET} before running out of '
        f'{Style.BRIGHT}{Fore.MAGENTA}lives{Style.RESET_ALL}, '
        f'{Fore.GREEN}you win!\n'
    )
    print(
        f'To restart{Fore.RESET} the game while playing: \n'
        f'Press the {Back.RED}RUN PROGRAM{Back.RESET} '
        'button in the top left,\nabove the terminal.\n'
    )
    print(f'{Style.BRIGHT}Good luck, and have fun!\n')
    while True:
        user_input = input(f'Press {Back.WHITE}{Fore.BLACK}{Style.BRIGHT} ENTER {Style.RESET_ALL} to start')  # noqa
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
