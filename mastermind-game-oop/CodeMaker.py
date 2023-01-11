import requests
import __main__

# this class has the secret code
class CodeMaker:
    def __init__(self):
        # if it is computer, auto generate the secret code. otherwise the player pick the code
        self.auto_mode = self.set_computer()
        self.name = "Computer" if self.auto_mode == True else input("\nCode maker, please enter your name: ")
        self.difficulty = self.set_difficulty()
        self.secret_code = self.autogenerate_secret_code(self.difficulty) if self.auto_mode else self.create_secret_code(self.difficulty)
    
    @staticmethod
    def set_computer():
        print("1. vs. Computer (play against the computer's secret code)")
        print("\t1 to 4 players: All the players will be code breakers")
        print()
        print("2. vs. Friends (play against your friend's secret code)")
        print("\t2 to 5 players: 1 player will be a code maker and others will be code breakers")
        print("------------------------------------------------------")
        while True:
            game_mode = input("Please pick the game mode (1/2): ")
            if game_mode == "1": return True
            elif game_mode == "2": return False
            else:
                print("Please pick a number. (1/2)")
    
    @staticmethod
    def set_difficulty():
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
    
    @staticmethod
    def autogenerate_secret_code(difficulty):
        secret_code = requests.get(f"https://www.random.org/integers/?num={difficulty}&min=1&max=6&col=1&base=10&format=plain&rnd=new") #api returns a byte string of the secret code
        # convert byte string to integer
        secret_code = secret_code.content.split(b'\n')
        secret_code = [int(num.decode()) for num in secret_code[:-1]]
        print()
        print("The secret code is created!")
        return secret_code
    
    @staticmethod
    def create_secret_code(difficulty):
        secret_code = []
        print("")
        print("Please make a number combination for the secret code.")
        print("------------------------------------------------------")
        # the player will pick the number combination - the number of its set depends on the difficulty
        while len(secret_code) < difficulty:
            try:
                num = int(input(f"Pick {__main__.make_ordinal(len(secret_code)+1)} number (from 0 to 7): "))
            # if user input is not a number, print out error message
            except ValueError:
                print("Please pick a number!")
                continue
            # if number is out of the range, print out the error message
            if num < 0 or num > 7:
                print("Number is out of range, try again!")
            else:
                secret_code.append(num)
        __main__.clear_console()
        return secret_code