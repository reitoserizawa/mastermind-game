import requests
import __main__

# this class has the secret code
class CodeMaker:
    def __init__(self):
        # if it is computer, auto generate the secret code. otherwise the player pick the code
        self.auto_mode = self.set_auto_mode()
        self.name = "Computer" if self.auto_mode == True else input("\nCode maker, please enter your name: ")
        # the difficulty relates to how many numbers a secret code has
        self.difficulty = self.set_difficulty()
        self.secret_code = self.autogenerate_secret_code(self.difficulty) if self.auto_mode else self.create_secret_code(self.difficulty)
    
    # ask the player if they want to play agains the computer or friends
    def set_auto_mode(self):
        print("1. vs. Computer (play against the computer's secret code)")
        print("\t1 to 4 players: All the players will be code breakers")
        print()
        print("2. vs. Friends (play against your friend's secret code)")
        print("\t2 to 5 players: 1 player will be a code maker and others will be code breakers")
        print("------------------------------------------------------")
        while True:
            try:
                game_mode = int(input("Please pick the game mode (1/2): "))
                if game_mode == 1: return True
                elif game_mode == 2: return False
                else:
                    print("Please pick a valid number 1 or 2.")
            except ValueError:
                print("Please pick a number 1 or 2.")
    
    # the dificculty decides how many numbers are used in the secret code
    def set_difficulty(self):
        print()
        print("(E)asy: 4 numbers of secret code")
        print("(M)edium: 5 numbers of secret code")
        print("(H)ard: 6 numbers of secret code")
        print("------------------------------------------------------")
        while True:
            difficulty = input("Please select the difficulty level: ").lower()
            if difficulty == "easy" or difficulty == "e" or difficulty == "4" : return 4
            elif difficulty == "medium" or difficulty == "m" or difficulty == "5": return 5
            elif difficulty == "hard" or difficulty == "h" or difficulty == "6": return 6
            else:
                print("Please select a valid difficulty. (E/M/H)")
    
    # if the player is against the computer, it automatically generates a secret code form the api
    def autogenerate_secret_code(self, difficulty):
        secret_code = requests.get(f"https://www.random.org/integers/?num={difficulty}&min=1&max=6&col=1&base=10&format=plain&rnd=new") # fetch the api data
        secret_code = secret_code.content.split(b'\n') # access the byte string data from the api and convert it into a string diving by the new line
        secret_code = [int(num.decode()) for num in secret_code[:-1]] # convert the byte string to integer
        print()
        print("The secret code is created!")
        return secret_code
    
    def create_secret_code(self, difficulty):
        secret_code = []
        print("")
        print("Please make a number combination for the secret code.")
        print("------------------------------------------------------")
        # the player will pick the number combination depeding on the difficulty
        while len(secret_code) < difficulty:
            # if user input is not a number or number is out of the range, print out error message
            try:
                num = int(input(f"Pick {__main__.make_ordinal(len(secret_code)+1)} number (from 0 to 7): "))
                if num < 0 or num > 7:
                    print("Number is out of range, try again!")
                else:
                    secret_code.append(num)
            except ValueError:
                print("Please pick a number!")
                continue
        __main__.clear_console()
        return secret_code