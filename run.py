import random

"""Initialise the game class."""
class hangmanGame:
    def _init_(self):
        self.reset()


"""Resets all game states."""
def reset(self):
    self.hidden_player = self.chosen_player()
    self.guessed_letters = []
    self.incorrect_guesses = 0
    self.max_attempts = 6
    self.playGame()

"""Chooses a random footballer from the list for the user to guess"""
def chosen_player(self):
        footballers = [' messi', 'ronaldo', 'kane', 'haaland', 'mbappe', 'lewandowski', 'bellingham', 'neymar', 'son', 'foden', 'kroos', 'benzema', 'modric', 'salah', 'rashford', 'neuer', 'rooney', 'gerrard', 'lampard','maradona']
        return random.choice(footballers)

"""Hangman pictures"""
def hangman_picture(self):
     if self.incorrect_guesses == 0:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif self.incorrect_guesses == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("YOU LOSE!")

"""Checks what letters have been guessed and displays if correct""" 
def display_player(self):
    display = ""
    for letter in self.hidden_player:
        if letter in self.guessed_letters:
             display += letter
        else:
            display += "_"
    return display    

"""Start of Footballers Hangman and allows user to start guessing letters"""
def playGame(self):
      print("Welcome to Footballers Hangman, can you guess the footballer I'm thinking of??")

      while self.incorrect_guesses < self.max_attempts:
            current_display = self.display_player()
            print(f"Footballer: {current_display}")
            self.hangman_picture()

            guess = input("Please gess a letter:").lower()

            if len(guess) !=1 or not guess.is alpha():