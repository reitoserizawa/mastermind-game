class Hint:
    def __init__(self, secret_code, guessed_code):
        self.correct_num, self.correct_location = self.generate_hint(secret_code, guessed_code)
    
    @staticmethod
    def generate_hint(secret_code, guessed_code):
        # make copies of codes to avoid chnaging originals since using to display history
        secret_code = secret_code.copy()
        guessed_code = guessed_code.copy()
        correct_num = 0
        correct_location = 0
        # mark matched num to avoid miss counting with duplicate numbers
        for i in range(len(secret_code)):
            if secret_code[i] == guessed_code[i]:
                secret_code[i] = '*'
                guessed_code[i] = '-'    
                correct_num += 1
                correct_location += 1
        for i in range(len(secret_code)):
            if guessed_code[i] in secret_code:
                secret_code[secret_code.index(guessed_code[i])] = '*'
                guessed_code[i] = '-'
                correct_num += 1
        return correct_num, correct_location
    
    # return string to save in histroy
    def __repr__(self):
        if self.correct_num == 0 and self.correct_location == 0:
            return "All incorrect!"
        else:
            return f"{self.correct_num} correct number(s) and {self.correct_location} correct location!"