# this class holds the guess and hint in the dictionary
class History:
    def __init__(self):
        self.history = {}
    
    def add_history(self, guess, hint):
        self.history[f"{guess}"] = hint # save the guess in the key as a string since the keys need to be immutable
        return self.history
    
    def display_history(self):
        i = 1
        for guess, hint in self.history.items():
            print(f"\t  ROUND {i}")
            print("\t------------------------------------------------------")
            print(f"\t  Guess: {guess}")
            print(f"\t  Hint: {hint}")
            print("\t------------------------------------------------------")
            i += 1