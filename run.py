import random
import time

def welcomeScreen():
   

    hangmanLogo = """
     __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.   
    |  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |    
    |  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |   
    |   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |    
    |  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |    
    |__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|     
    
---------------------------------------------------------------------------------------
                                                                                     """
    print(hangmanLogo)

class hangmanGame:
    def __init__(self):
        """
        Initialise the game class.
        """
        self.restart()

    def restart(self):
        """
        Resets all game states.
        """
        self.hidden_player = self.chosen_player()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_guesses = 6
        self.playGame()

    def chosen_player(self):
        """
        Chooses a random footballer from the list for the user to guess.
        """
        footballers = [' messi', 'ronaldo', 'kane', 'haaland', 'mbappe', 'lewandowski', 'bellingham', 'neymar', 'son', 'foden', 'kroos', 'benzema', 'modric', 'salah', 'rashford', 'neuer', 'rooney', 'gerrard', 'lampard','maradona']
        return random.choice(footballers)

    def display_player(self):
        """
        Checks what letters have been guessed and displays if correct.
        """
        display = ""
        for letter in self.hidden_player:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def hangman_picture(self):
        """
        Hangman pictures as they progeess depending on answers.
        """
        if self.incorrect_guesses == 0:
            print("  ________      ")
            print("  |      |      ")
            print("  |             ")
            print("  |             ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 1:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |             ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 2:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /       ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 3:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|      ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 4:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|\\    ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 5:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|\\    ")
            print("  |     /       ")
            print("*_| _*          ")
        else:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|\\    ")
            print("  |     / \\    ")
            print("*_| _*          ")
            print("You lose man, do you even know ball?")

    def playGame(self):
        """
        Start of Footballers Hangman and allows user to start guessing letters.
        """
        welcome = ("Welcome to Footballers Hangman, can you guess the footballer I'm thinking of??")
        for char in welcome:
            print(char, end='', flush=True)
            time.sleep(.05)
      
        while self.incorrect_guesses < self.max_guesses:
            current_display = self.display_player()
            print(f"\nFootballer: {current_display}")
            self.hangman_picture()

            guess = input("Please guess a letter:").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid letter (A single lowercase leter).")
                continue

            if guess in self.guessed_letters:
                print("You have already tried that letter, try another.")
                continue
            self.guessed_letters.append(guess)


            if guess not in self.hidden_player:
                self.incorrect_guesses += 1
                print(f"Unlucky thats not one of the letters! You have {self.max_guesses - self.incorrect_guesses} guesses left!")
            else:
                print("Thats correct, keep going!")

            if all(letter in self.guessed_letters
                   for letter in self.hidden_player):
                print(f"Well done! You guessed {self.hidden_player} or did you just read my mind?!")
                self.reset()
                break

        if self.incorrect_guesses == self.max_guesses:
            self.hangman_picture()
            print(f"Ahh unlucky, you have run out of guesses! The player I was thinking of was {self.hidden_player}. Better luck next time!")
            


welcomeScreen()
hangmanGame()
playGame()