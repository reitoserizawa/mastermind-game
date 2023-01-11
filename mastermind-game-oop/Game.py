<<<<<<< HEAD
class Game:
    def __init__(self):
        self.attempt = 10
        self.is_computer = self.set_computer()
        self.difficulty = self.set_difficulty()
        self.player_num = self.set_player_number()
    
    def set_player_number(self):
        print()
        if self.is_computer:
            while True:
                try:
                    player_num = int(input("How many players? (from 1 to 4): "))
                    if player_num >= 1 and player_num <= 4:
                        return int(player_num)
                    else:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid number from 1 to 4.")
                    continue
        else:
            while True:
                try:
                    player_num = int(input("How many players? (from 2 to 4): "))
                    if player_num >= 2 and player_num <= 4:
                        return int(player_num)
                    else:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid number from 2 to 4.")
                    continue
    
    def game_over(self):
        if self.attempt == 0:
            return False
        else:
            return True
    
    @staticmethod
    def set_computer():
        print("1. vs. Computer (play against the computer's secret code)")
        print("2. vs. Friends (play against your friend's secret code)")
        print("------------------------------------------------------")
        while True:
            game_mode = input("Please pick the game mode (1 or 2): ")
            if game_mode == "1": return True
            elif game_mode == "2": return False
            else:
                print("Please pick a valid number.")
    
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
                print("Please select the valid difficulty.")
=======
# this class holds how many attempts code makers have
class Game:
    def __init__(self):
        self.attempt = 10
>>>>>>> parent of 66ecbff (game data sturcture edited)
    
    @staticmethod
    def show_instructions():
        print("This is MasterMind Game. There is a secret code created by a code maker with number combinations.")
        print("Code breakers have to guess the number combination.")
        print("At first, you will pick vs. Computer or vs. Friends Mode. If you pick vs. Computer Mode, you will play against the computer's secret code (1 to 4 players).")
        print("If you pick vs. Friends Mode, the code maker will pick the number combinations and others will be code breakers (2 to 4 players).")
        print('There are 3 difficulty levels. "Easy" has a 4-number combination, "Medium" has a 5-number combination, and "Hard" has a 6-number combination (all combinations contain a number from 0 to 7).')
        print("Code breakers have 10 attempts to guess the right number combinations.")
        print("At the end of each guess, code breakers get feedback saying:")
        print("\t 1. Correct Number: How many numbers you used are in the secret code")
        print("\t 2. Correct Location: From the numbers you used, how many of them are in the right location")
        print("Please enjoy this game!")
        print()