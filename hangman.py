import random
from words import words


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


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


print('Welcome to hangman!\n')
print('The goal of the game is to find the word that the computer has selected.\n')
print('The word will be represented by dashes. You find the word by guessing one letter at a time. You can only guess a letter once.\n')
print("Guessing a letter correctly will display the letter in it's position. An incorrect guess will cost you one life.\n")
print('Good luck, and have fun!\n')

def start_game():
    while True:
        user_input = input('Type "start" to begin: ')
        if user_input == 'start' or user_input == 'Start':
            hangman()
            break
        else:
            print('Invalid input.')

startGame()
