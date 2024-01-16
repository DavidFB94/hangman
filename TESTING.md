# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| hangman.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/hangman.py) | ![screenshot](documentation/validation/py-validation-hangman.png) | Pass: No Errors |
| words.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/words.py) | ![screenshot](documentation/py-validation-words.png) | Pass: No Errors |
| food.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/food.py) | ![screenshot](documentation/py-validation-food.png) | Pass: No Errors |
| animals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/animals.py) | ![screenshot](documentation/py-validation-animals.png) | Pass: No Errors |
| countries.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/hangman/main/countries.py) | ![screenshot](documentation/py-validation-countries.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | HerokuApp | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/edge.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | HerokuApp | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile.png) |  Works as expected. Not designed for mobile compatibility. |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet.png) | Works as expected. Not designed for tablet compatibility. |
| Desktop | ![screenshot](documentation/browsers/chrome.png) | Works as expected |
| Sony Xperia 10 | ![screenshot](documentation/responsiveness/responsive-xperia.jpg) | Scaling starts to have issues. Not designed for mobile compatibility. |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| HerokuApp | ![screenshot](documentation/lighthouse/lighthouse-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-desktop) | Some minor warnings |
