from History import History 

# code breaker class has name and history attributes to show their own history of guesses and hints
class CodeBreaker:
    def __init__(self, name):
        self.name = name
        self.history = History()