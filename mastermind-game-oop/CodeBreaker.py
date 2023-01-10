from History import History 

class CodeBreaker:
    def __init__(self, name):
        self.name = name
        self.history = History()
    
    def display_history(self):
        while len(self.history.history) > 0:
            show_history = input("\t  Do you want to see your past guess(es) and hint(s)? (y/n): ")
            if show_history == "y" or show_history == "yes":
                print("\t------------------------------------------------------")
                self.history.display_history()
                return
            elif show_history == "n" or show_history == "no":
                return
            else:
                print("\t  Please type a valid answer. (y/n)")