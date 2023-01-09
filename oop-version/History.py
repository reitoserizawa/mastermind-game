class History:
    def __init__(self):
        self.history = {}
    
    def add_history(self, guess, hint):
        self.history[f"{guess}"] = hint
        return self.history
    
    def display_history(self):
        i = 1
        for k, v in self.history.items():
            print(f"\t  ROUND {i}")
            print("\t------------------------------------------------------")
            print(f"\t  Guess: {k}")
            print(f"\t  Hint: {v}")
            print("\t------------------------------------------------------")
            i += 1