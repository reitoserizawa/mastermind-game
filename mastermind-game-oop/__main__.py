import os
from sys import platform
from Game import Game
from CodeMaker import CodeMaker
from CodeBreakerList import CodeBreakerList
from Guess import Guess
from Hint import Hint
from Result import Result
from Ranking import Ranking

# ranking of game
ranking = Ranking()

def clear_console():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

# used in code maker to cretae custom secret code and guess to generate guessed code
def make_ordinal(num):
        # if num is between 11 and 13, suffix is th
        if 11 <= num <= 13:
            suffix = "th"
        else:
            # if 0, suffix is th, else if 1, suffix is st...
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(num%10 ,4)]
        return str(num) + suffix

def play(game, code_maker, player_list):
    clear_console()
    print("\t  GAME START!")
    while game.attempt > 0:
        for player in player_list:
            print()
            if len(player_list) > 1:
                print(f"\t  {player.name}'s Turn...!\n")
                if len(player.history.history) >= 1:
                    input("\t  Please enter to see your history of guess(es) and hint(s): ")
                    print()
                    player.history.display_history()
                    print()
            print(f"\t  Life Remaining: {game.attempt}")
            print("\t------------------------------------------------------")
            while True:
                guess = Guess(game.difficulty)
                if str(guess.guess) in player.history.history.keys():
                    print("\t  You already used the number combination, pick another one!")
                    continue
                else:
                    break
            if guess.guess == code_maker.secret_code:
                print(f"\t  Congratulations, {player.name}! You won!")
                result = Result(player.name, False, code_maker.secret_code, 10-game.attempt)
                print(f"\t  {result}")
                ranking.insert_ranking(result)
                ranking.display_ranking()
                return
            hint = Hint(code_maker.secret_code, guess.guess)
            player.history.add_history(guess.guess, hint)
            player.history.display_history()
            if len(player_list) > 1:
                input("\t  Please enter to go to the next code breaker: ")
                clear_console()
        game.attempt -= 1
    print()
    print("\t  There is no more life left...")
    result = Result(code_maker.name, True, code_maker.secret_code, game.attempt)
    print(f"\t  {result}")
    ranking.display_ranking()
    return

if __name__ == "__main__":
    clear_console()
    print("WELCOME TO MATERMIND GAME!")
    while True:
        start = input("Would you like to (p)lay mastermind, read (i)nstructions, or (q)uit?: ").lower()
        print()
        if start == "play" or start == "p":
            game = Game()
            code_maker = CodeMaker(game.is_computer, game.difficulty)
            player_list = CodeBreakerList(game.player_num) if game.is_computer else CodeBreakerList(game.player_num-1)
            play(game, code_maker, player_list.players)
        elif start == "instructions" or start == "i":
            Game.show_instructions()
        elif start == "quit" or start == "q":
            print("Thank you, bye!")
            exit()
        else:
            print("Please type a valid word.")