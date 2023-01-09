class Guess:
    def __init__(self, difficulty):
        self.guessed_code = self.generate_guessed_code(difficulty)
        self.current_winner = None
    
    def generate_guessed_code(self, difficulty):
        guessed_code = []
        while len(guessed_code) < difficulty:
            try:
                num = int(input(f"\t  guess {self.make_ordinal(len(guessed_code)+1)} number (from 0 to 7): "))
        # if value error, print out error message
            except ValueError:
                print("Please pick a number!")
                continue
        # if num is not valid, print out error message
            if num < 0 or num > 7:
                print("number is out of range, try again!")
            else:
                guessed_code.append(num)
        print('\n')
        return guessed_code

    @staticmethod
    # assign suffix depending on order of user input for guessed code
    def make_ordinal(num):
        # if num is between 11 and 13, suffix is th
        if 11 <= num <= 13:
            suffix = "th"
        else:
            # if 0, suffix is th, else if 1, suffix is st...
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(num%10 ,4)]
        return str(num) + suffix
