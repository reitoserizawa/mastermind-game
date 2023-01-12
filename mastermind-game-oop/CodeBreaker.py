from History import History 

# this class is the code maker and related to the history class to show their history
class CodeBreaker:
    def __init__(self, name):
        self.name = name
        self.history_list = []
    
    def check_duplicate_guess(self, guess):
        if any(guess == history.guess for history in self.history_list):
            return True
        else:
            return False

    def add_history(self, difficulty, secret_code):
        while True:
            history = History(difficulty, secret_code)
            if self.check_duplicate_guess(history):
                continue
            else:
                self.history_list.append(history)
                return

    def display_history_list(self):
        i = 1
        for history in self.history_list:
            print(f"\t  ROUND {i}")
            print("\t------------------------------------------------------")
            print(f"\t  Guess: {history.guess}")
            print(f"\t  Hint: {history.hint}")
            print("\t------------------------------------------------------")
            i += 1