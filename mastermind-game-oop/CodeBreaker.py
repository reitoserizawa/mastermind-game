from History import History 

# this class is the code maker and related to the history object to show their history of guesses and hints
class CodeBreaker:
    def __init__(self, name):
        self.name = name
        self.history = History()