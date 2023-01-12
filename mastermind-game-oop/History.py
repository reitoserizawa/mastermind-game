from Guess import Guess
from Hint import Hint
# this class holds the guess and hint in the dictionary
class History:
    def __init__(self, difficulty, secret_code):
        self.guess = Guess(difficulty)
        self.hint = Hint(secret_code, self.guess)
    
    def add_history(self, guess, hint):
        self.history[f"{guess}"] = hint # save the guess in the key as a string since the keys need to be immutable
        return self.history