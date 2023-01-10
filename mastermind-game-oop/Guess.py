import __main__

class Guess:
    def __init__(self, difficulty):
        self.guess = self.generate_guess(difficulty)
    
    @staticmethod
    def generate_guess(difficulty):
        guess = []
        while len(guess) < difficulty:
            try:
                num = int(input(f"\t  Guess {__main__.make_ordinal(len(guess)+1)} number (from 0 to 7): "))
        # if value error, print out error message
            except ValueError:
                print("\t  Please pick a number!")
                continue
        # if num is not valid, print out error message
            if num < 0 or num > 7:
                print("\t  Number is out of range, try again!")
            else:
                guess.append(num)
        print('\n')
        return guess