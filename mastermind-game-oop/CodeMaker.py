import requests
import os
import __main__

class CodeMaker:
    def __init__(self, auto_mode, difficulty):
        # define create or auto-generate secret code
        self.auto_mode = auto_mode
        self.name = "Computer" if self.auto_mode == True else input("\nCode maker, please enter your name: ")
        self.secret_code = self.autogenerate_secret_code(difficulty) if self.auto_mode else self.create_secret_code(difficulty)
    
    @staticmethod
    def autogenerate_secret_code(difficulty):
        secret_code = requests.get(f"https://www.random.org/integers/?num={difficulty}&min=1&max=6&col=1&base=10&format=plain&rnd=new")
        # convert byte string to integer
        secret_code = secret_code.content.split(b'\n')
        secret_code = [int(num.decode()) for num in secret_code[:-1]]
        print()
        print("The secret code is created!\n")
        return secret_code
    
    @staticmethod
    def create_secret_code(difficulty):
        secret_code = []
        print("")
        print("Please make a number combination for the secret code.")
        print("------------------------------------------------------")
        while len(secret_code) < difficulty:
            try:
                num = int(input(f"Pick {__main__.make_ordinal(len(secret_code)+1)} number (from 0 to 7): "))
            # if not number, print out error message
            except ValueError:
                print("Please pick a number!")
                continue
            # if number is not valid, print out error message
            if num < 0 or num > 7:
                print("Number is out of range, try again!")
            else:
                secret_code.append(num)
        os.system('clear')
        return secret_code