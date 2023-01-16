# hint class generates
    # 1. how many of the number from the guess is in the secret code
    # 2. from the number, how many of them are in the correct location
class Hint:
    def __init__(self, secret_code, guess):
        self.correct_num, self.correct_location = self.generate_hint(secret_code, guess)
    
    def generate_hint(self, secret_code, guess):
        # make copies of the secret code and guess to avoid chnaging originals since using to display history
        secret_code = secret_code.copy()
        guess = guess.copy()
        # set 0 for each variable to start with
        correct_num = 0
        correct_location = 0
        # in case there is duplicated numbers in the secret code, the secret code and guess should be marked as we check
        for i in range(len(secret_code)):
            if secret_code[i] == guess[i]:
                # mark the matched number for both
                secret_code[i] = '*' 
                guess[i] = '-'
                # add 1 for both variables since we found a number that matches the secret code and the location is correct
                correct_num += 1
                correct_location += 1
        for i in range(len(secret_code)):
            if guess[i] in secret_code:
                # by marking the number that is in the secret code and guess, we will not double count them
                secret_code[secret_code.index(guess[i])] = '*'
                guess[i] = '-'
                correct_num += 1
        return correct_num, correct_location
    
    # return a printable string to save in the histroy
    def __repr__(self):
        if self.correct_num == 0 and self.correct_location == 0:
            return "All incorrect!"
        else:
            return f"{self.correct_num} correct number(s) and {self.correct_location} correct location!"