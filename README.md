# [HANGMAN](https://hangman-ci-c8eaf2c13598.herokuapp.com)
## Overview
Hangman is a terminal based game that let the user test their word knowledge.

The user will compete against the computer to guess a randomly chosen word, one letter at a time. The amount of guesses are limited, so use the them with caution!

The user can choose between different word categories, and based on the word length, the amount of guesses will be set. 

This game was built as a project for the Diploma in Full Stack Software Development at Code Institute.

### Mock-up

![screenshot](documentation/mockup.png)

## UX

I started out with a flowchart to determine the mapping of the app. After that I followed a tutorial to create the base structure, and adjusted the code to align with the ideas I had for the game.

Once the game was created, I wanted to add some color to the text, to make it a bit more interesting/easy to look at. I imported Colorama, and added the styling to the code.

## Features

### Existing Features

- **Welcome message and rules**

    - Greets the user and explains the rules

![screenshot](documentation/features/feature01.png)

- **User input to start game**

    - Makes sure the user has time to read the message/rules, and  has control over starting the game

![screenshot](documentation/features/feature02.png)

- **Category selection with simple terminal menu**

    - Multiple ways to select categories. Arrow keys or number input. 

![screenshot](documentation/feature03.png)

- **Used letters and lives tracking**

    - User stays informed about which letters has been guessed, and of lives remaining

![screenshot](documentation/features/feature04.png)

- **Input feedback messages **

    - Offers feedback to the user that the input has been received, if the guess was correct or not, and if the letter has been used already

![screenshot](documentation/features/feature05-1.png)
![screenshot](documentation/features/feature05-2.png)
![screenshot](documentation/features/feature05-3.png)

- **Input alert-messages**

    - Informs the user about invalid input

![screenshot](documentation/features/feature06-1.png)
![screenshot](documentation/features/feature06-2.png)

- **End game screen with "play again?" option**

    - Informs the user if they have won/lost and displays the word. Request to play again.

![screenshot](documentation/features/feature07-1.png)
![screenshot](documentation/features/feature07-2.png)

- **"Thank you for playing" message**

    - Lets the user know that the app is exiting

![screenshot](documentation/features/feature08.png)

### Future Features
- Add hints
    - Add functionality to receive word hints
- Add timer
    - Add functionality to limit response time
- Add more valid characters
    - Add functionality to use words with spaces and/or hyphens

## Tools & Technologies Used

- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [ChatGPT](https://chat.openai.com/) used for creating list for `food.py`.

## Data Model

### Flowchart

To follow best practice, a flowchart was created for the app's logic,
and mapped out before coding began using a free version of [Miro](https://www.miro.com/).

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png)

###  Functions

The primary functions used on this application are:

- `start_game()`
    - Runs game on startup
- `select_category()`
    - Menu for category selection
- `get_valid_word()`
    - Pulls a valid word for the user to guess
- `hangman()`
    - The game. Sets lives, word and asks for user input, with feedback
- `play_again()`
    - Requests user to play again
- `clear()`
    -  Clears the terminal

### Imports

I've used the following Python packages and/or external imported packages.

- `time`: used for adding time delays
- `os`: used for adding a `clear()` function
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list
- `string.ascii_uppercase`: used to create a set of alphabetical letters in uppercase for letters in word
- `simple_term_menu`: used for adding a simple terminal menu for category choices

