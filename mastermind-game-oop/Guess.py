import __main__

# this class generates the guess
class Guess:
    def __init__(self, difficulty):
        self.guess = self.generate_guess(difficulty)
    
    @staticmethod
    def generate_guess(difficulty):
        guess = []
        # make a guess till the guess matches the number of difficulty(how many numbers a secret code has)
        while len(guess) < difficulty:
            try:
                num = int(input(f"\t  Guess {__main__.make_ordinal(len(guess)+1)} number (from 0 to 7): "))
                # error handling if the number is out of range or not integer
                if num < 0 or num > 7:
                    print("\t  Number is out of range, try again!")
                else:
                    guess.append(num)
            except ValueError:
                print("\t  Please pick a number!")
                continue
        print('\n')
        return guess