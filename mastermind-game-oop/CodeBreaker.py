from History import History 

# this class is the code maker and related to the history class to show their history
class CodeBreaker:
    def __init__(self, name):
        self.name = name
        self.history = History()