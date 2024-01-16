# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| hangman.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/hangman.py) | ![screenshot](documentation/validation/py-validation-hangman.png) | Pass: No Errors |
| words.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/words.py) | ![screenshot](documentation/validation/py-validation-words.png) | Pass: No Errors |
| food.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/food.py) | ![screenshot](documentation/validation/py-validation-food.png) | Pass: No Errors |
| animals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/animals.py) | ![screenshot](documentation/validation/py-validation-animals.png) | Pass: No Errors |
| countries.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/countries.py) | ![screenshot](documentation/validation/py-validation-countries.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | hangman.py | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/edge.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | hangman.py | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile.png) |  Works as expected. Not designed for mobile compatibility. |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet.png) | Works as expected. Not designed for tablet compatibility. |
| Desktop | ![screenshot](documentation/browsers/chrome.png) | Works as expected |
| Sony Xperia 10 | ![screenshot](documentation/responsiveness/responsive-xperia.jpg) | Scaling starts to have issues. Not designed for mobile compatibility. |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| hangman.py | ![screenshot](documentation/lighthouse/lighthouse-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing (CTRL + C always interrupts the terminal):

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| `hangman.py` | | | | | |
| | Game is expected to display welcome message + rules when run | Tested the feature by running game | The game ran, and message + rules were displayed | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Game is expected to start when the user press ENTER (only) | Tested the feature by trying inputs (alphabetical input, multiple characters, numbers, special characters, keypress combinations) | The game started only when ENTER was pressed | Test concluded and passed | ![screenshot](documentation/feature-testing/feature02-1-test.png)![screenshot](documentation/feature-testing/feature02-2-test.png) |
| | Category is expected to be selected only when the user selects with up/down arrow keys + ENTER or single number input | Tested the feature by trying inputs (alphabetical input, numbers, special characters, keypress combinations) | The category was selected when up/down + ENTER or single number input was pressed. Pressing Q, ESC or CTRL + C causes TypeErrors. PG UP hovers the first category, PG DN hovers the last. | Test concluded. Known bugs. See "Unfixed Bugs" section | 
![screenshot](documentation/features/feature03.png) |
| | Tracking is expected to update the lives + used letters after the user has guessed a letter | Tested the feature by guessing a letter, make a correct guess to reduce lives, and guess a correct letter to have the lives stays the same | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/feature-testing/feature04-1-test.png)![screenshot](documentation/feature-testing/feature04-2-test.png)![screenshot](documentation/feature-testing/feature04-3-test.png) |
| | Input feedback message is expected to display colored text feedback based on correct/incorrect guess and if a letter has already been used | Tested the feature by guessing a letter, guessing an already used letter, make a correct guess to see green text, and guess an incorrect letter to see red text | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/features/feature05-1.png)![screenshot](documentation/features/feature05-2.png)![screenshot](documentation/features/feature05-3.png) |
| | Input alert-message is expected to display colored text feedback when user uses invalid input | Tested the feature by using invalid input (multiple characters, numbers, special characters, keypress combinations) | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/feature-testing/feature06-1-test.png)![screenshot](documentation/feature-testing/feature06-2-test.png)![screenshot](documentation/feature-testing/feature06-3-test.png)
![screenshot](documentation/feature-testing/feature06-4-test.png)![screenshot](documentation/feature-testing/feature06-5-test.png)![screenshot](documentation/feature-testing/feature06-6-test.png) |
| | End game screen is expected to inform the user about win/loss, display the chosen word, how many lives were remaining (if the user won), and request the user to play again. If the user selects to play again, take the user to the start game screen. If user selects to not play again, take user to exiting game screen. The feature will also display colored text feedback when invalid input is used | Tested the feature by guessing until the lives ran out, and guessing until I found the word with lives remaining. Selected to play again, and to not play again. Tried different inputs to test feedback (multiple characters, numbers, special characters, keypress combinations) | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/features/feature07-2.png)![screenshot](documentation/features/feature07-1.png)
![screenshot](documentation/feature-testing/feature07.png)![screenshot](documentation/feature-testing/feature07-1.png)![screenshot](documentation/feature-testing/feature07-2.png)![screenshot](documentation/feature-testing/feature07-3.png)![screenshot](documentation/feature-testing/feature07-4.png)![screenshot](documentation/feature-testing/feature07-5.png)![screenshot](documentation/feature-testing/feature07-6.png) |
| | Thank you for playing message is expected to display a message if the user choses to not play again | Tested the feature by finishing the game, and choosing to not play again | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/features/feature08.png) |

## Bugs

- Occasionally, the word that was selected did not match the selected category. 

    ![screenshot](documentation/bugs/bug01.png)

    - I used print statements to locate the bug. When words containing a "space" or "-" was selected, the function defaulted back to `words-py`.  To fix this, I had to replace "words" with "category" as the argument in the get_valid_word() while-loop.

- Python `E741` (ambiguous variable name)

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I changed the variable name.

- Python `E501` line too long (108 > 79 characters)

    ![screenshot](documentation/bugs/bug03.png)

    - There were several of these errors. Most of them were re-formatted. To fix line 238, I added # noqa.

## Unfixed Bugs

- When in the terminal menu, hitting ESC and Q will cause a TypeError.

   ![screenshot](documentation/unfixed-bugs/unfixed-bug01.png)

    - Could not find fix.
 
- CTRL + C will cause an KeyboardInterrupt (in category selecting it causes TypeError).

    ![screenshot](documentation/unfixed-bugs/unfixed-bug02.png)

    - Could not find fix.

- When using the web terminal in Heroku, the first menu option has a white square to the left.

    ![screenshot](documentation/unfixed-bugs/unfixed-bug03.png)

    - Could not find fix.

