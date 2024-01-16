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

