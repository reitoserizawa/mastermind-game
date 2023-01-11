class Game:
    def __init__(self):
        self.attempt = 10
    
    @staticmethod
    def show_instructions():
        print("This is MasterMind Game. There is a secret code created by a code maker with number combinations.")
        print("Code breakers have to guess the number combination.")
        print("At first, you will pick vs. Computer or vs. Friends Mode. If you pick vs. Computer Mode, you will play against the computer's secret code (1 to 4 players).")
        print("If you pick vs. Friends Mode, the code maker will pick the number combinations and others will be code breakers (2 to 5p players).")
        print('There are 3 difficulty levels. "Easy" has a 4-number combination, "Medium" has a 5-number combination, and "Hard" has a 6-number combination (all combinations contain a number from 0 to 7).')
        print("Code breakers have 10 attempts to guess the right number combinations.")
        print("At the end of each guess, code breakers get feedback saying:")
        print("\t 1. Correct Number: How many numbers you used are in the secret code")
        print("\t 2. Correct Location: From the numbers you used, how many of them are in the right location")
        print("Please enjoy this game!")
        print()