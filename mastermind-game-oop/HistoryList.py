from History import History

# this class connects with the history and add them in a list
class HistoryList:
    def __init__(self):
        self.history_list = []
    
    def add_history(self, guess, hint):
        # save the history in the list with the guess and hint
        self.history_list.append(History(guess, hint)) 
        return self.history_list
    
    def display_history(self):
        i = 1
        for history in self.history_list:
            print(f"\t  ROUND {i}")
            print("\t------------------------------------------------------")
            print(f"\t  Guess: {history.guess.guess}")
            print(f"\t  Hint: {history.hint}")
            print("\t------------------------------------------------------")
            i += 1
    
    # if the guess is already in the history list, return True else False
    def find_duplicate_guess(self, guess):
        for history in self.history_list:
            if history.guess.guess == guess.guess:
                return True
        return False