import time
from CodeMaker import CodeMaker
from Guess import Guess
from History import History
from Hint import Hint
from Ranking import Ranking

class Game:
    def __init__(self):
        self.attempt = 10
        self.difficulty = self.set_difficulty()
        self.winner = None
    
    def set_difficulty(self):
        print("\nplease select the difficulty")
        while True:
            difficulty = input("(e)asy: 4 numbers of secret code\n(m)edium: 5 numbers of secret code\n(h)ard: 6 numbers of secret code\n").lower()
            if difficulty == "easy" or difficulty == "e" : return 4
            elif difficulty == "medium" or difficulty == "m": return 5
            elif difficulty == "hard" or difficulty == "h": return 6
            else:
                print("please select the valid difficulty")
    
    @staticmethod
    def show_instructions():
        print("at the start, computer will randomly select a pattern of numbers from a total of 8 different numbers(from 0 to 7)")
        print("a player will have 10 lives to guess the number combinations")
        print("at the end of each guess, computer will provide a feedback\n")

# ranking
ranking = Ranking()

def play(game, code_maker):
    history = History()
    while game.attempt > 0:
        # start timer for ranking
        start_time = time.time()
        print(f"\t  Life Remaining: {game.attempt}")
        print("\t------------------------------------------------------")
        if len(history.history) > 0:
            history.display_history()
        guess = Guess(game.difficulty)
        # guess.generate_guessed_code(game.difficulty)
        if guess.guessed_code == code_maker.secret_code:
            # end timer
            end_time = time.time()
            total_time = int(end_time - start_time)
            game.winner = input("congratulations, you won! please tell me your name: ")
            ranking.insert_ranking(game)
            ranking.display_ranking()
            # below needs adding
            return
        if str(guess.guessed_code) in history.history.keys():
            print("you already used the code! pick another one!")
            continue
        hint = Hint(code_maker.secret_code, guess.guessed_code)
        history.add_history(guess.guessed_code, hint)
        print(code_maker.secret_code)
        game.attempt -= 1
    print("game over! you lost....")
    return

if __name__ == "__main__":
    while True:
        start = input("would you like to (p)lay mastermind, read (i)nstructions, or (q)uit?\n").lower()
        if start == "play" or start == "p" or start == "mastermind":
            game = Game()
            # play against the computer
            auto_mode = input("\ndo you wanna be a code (b)reaker or (m)aker?\n").lower()
            if auto_mode == "b" or auto_mode == "breaker":
                code_maker = CodeMaker(True, game.difficulty)
                play(game, code_maker)
            elif auto_mode == "m" or auto_mode == "maker":
                code_maker = CodeMaker(False, game.difficulty)
                play(game, code_maker)
            else:
                print("please enter b or m")
            # play within friends
        elif start == "instructions" or start == "i":
            Game.show_instructions()
        elif start == "quit" or start == "q":
            print("bye!")
            exit()
        else:
            print("please type a valid word\n")