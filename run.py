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