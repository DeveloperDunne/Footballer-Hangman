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

    