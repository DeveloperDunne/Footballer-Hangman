# Footballers Hangman
<br>
Welcome to Footballers Hangman!
<br>

Footballers hangman is a python terminal game which runs through Heroku and is based on the classic game, Hangman.

Will you succeed in guessing before your guesses run out or will you be dangling from above.

![Responsivness](./readme-images/spc-responsive.webp)

How to play:

Here your knowledge will be tested on famous footballers.

A random footballer will be generated for you to guess. As with the classic hangman game, you will have oppotunites to guess letters in which to guess the correct footballer. If you guess the correct letter the blank will be filled in, however get it worng and you will be one step closer to being hanged.

# Table of contents

- [1. Live Game](#1-live-game)
- [2. Goals](#2-goals)
- [3. Features](#3-features)
- [4. Technologies Used](#4-technologies-used)
- [5. Testing](#5-testing)
- [6. Deployment](#6-deployment)
- [7. Acknowledgements and Credits](#7-acknowledgements-and-credits)

<br>

## 1. Live Game:
Please see the live version here: Footballers Hangman. (https://footballers-hangman-cf411def0ec1.herokuapp.com/)

## 2. Goals:

### Developer Goals:

- I would like the game to be fun but testing.
- I wanted the game to be easy to use and navigate through.

### User stories /Goals:

- As a user I would like to be able to play the game in the command line.
- As a user I would like ot see when I guess correctly.
- As a user I would like to see how many guesses I have left if I guess wrong.
- As a user I would like to see the answer if I dont get it in time.
- As a user I would like to be asked to play again at the end of the game.


<br>

## 3. Features:

### The Welcome Screen:

- When you run the game you will have a welcome screen loaded which shows the game and rules.

![Welcome Screen](./readme-images/welcome-screen.webp)


### Random Footballer

- The game will choose a random footballer for you to try and guess. Each time you play there should be a different footballer chosen from within 20 footballers.

### Choosing an answer / invalid answer:

- Once you enter a letter the game will tell you if you are right or wrong. If you enter a number or more than one letter you will get a message asking you to input the correct data.

![Choosing an answer](./readme-images/choose.webp)

### The correct answer:

- If correct you will be advised you are right and all blank spaces in which that letter is correct will fill in to give you a better idea of who the footballer may be.

![Correct answer](./readme-images/correct-answer.webp)

### The wrong answer:

- However, if you enter a letter which is not one of the chosen fottballer you will be told you are wrong and shown how many guesses you have left.

![Wrong answer](./readme-images/incorrect-answer.webp)

### Future Features:
- I would have liked to have implemented an enter name function where your score could then be stored on a leaderboard at the end of the game but ran out of time.

## 4. Technologies Used:

### Languages:

- Python

This game was created using the Python Language.

<br>

## 5. Testing:

### Manual:

|Game Testing|Yes/No|
|---|:---:|
|Lets you know when correct and enters letter in the correct location within the word|✓|
|Lets you know when incorrect and notifies you how many guesses remain✓|
|Hangman picture updates if wrong|✓|
|If answer is not a letter or singular letter asks again for valid input|✓|
|If guesses run out, game shows correct answer|✓|
|Asks you to play again when game is complete|✓|
---

### 5. Testing programmes run:


#### CI Python Linter:

- Code was put through CI Python Linter with no issues reported.

 <br>
  ### Bugs solved:



### Unfixed Bugs:



 <br>

 ### Heroku Deployment

* This site was deployed by completing the following steps:

1. Log in to Heroku or create an account.
2. On the main page click Create New App.
3. Select your region.
4. Click on the Create App button
5. The next page is the project’s Deploy Tab, click the Settings Tab.
6. Next, scroll down to the Build pack section and click ‘Add Build pack’ select Python and click Save Changes
7. Add Node.JS after adding Python. (Please be aware: Python must be above Node.JS in that order).
8. Go to the Deploy tab.
9. Select Github as your deployment method.
10. Connect to GitHub.
11. Search your repository name and connect.
12. Click either Enable Automatic Deploys for automatic deployment when you push updates to GitHub or maunal to do this manually.

### Cloning:

- Go to the repository on GitHub.
- Click on the Code button and copy the https URL under Clone
- Open a terminal.
- Go to the folder you want to store the cloned repository.
- In the terminal type git clone and paste the URL of the cloned repository after it then press Enter.
- The site will then be cloned to that directory.

<br>