import requests

class CodeMaker:
    def __init__(self, auto_mode, difficulty):
        self.auto_mode = auto_mode
        self.secret_code = self.autogenerate_secret_code(difficulty) if self.auto_mode else self.create_secret_code(difficulty)
    
    def autogenerate_secret_code(self, difficulty):
        secret_code = requests.get(f"https://www.random.org/integers/?num={difficulty}&min=1&max=6&col=1&base=10&format=plain&rnd=new")
        # convert byte string to integer
        secret_code = secret_code.content.split(b'\n')
        secret_code = [int(num.decode()) for num in secret_code[:-1]]
        print("\nSecret Code Created...\n")
        return secret_code

    def create_secret_code(self, difficulty):
        secret_code = []
        while len(secret_code) < difficulty:
            try:
                num = int(input(f"Pick {self.make_ordinal(len(secret_code)+1)} number (from 0 to 7): "))
            # if value error, print out error message
            except ValueError:
                print("Please pick a number!")
                continue
            # if num is not valid, print out error message
            if num < 0 or num > 7:
                print("Number is out of range, try again!")
            else:
                secret_code.append(num)
        print("\nSecret Code Created...\n")
        return secret_code
    
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
