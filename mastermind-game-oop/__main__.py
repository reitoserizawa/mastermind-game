import os
from sys import platform
from Game import Game
from CodeMaker import CodeMaker
from CodeBreakerList import CodeBreakerList
from Guess import Guess
from Hint import Hint
from Result import Result
import app # connection to the database

# show each result as a ranking
def display_ranking():
    # fetch the list of results from the database
    data = app.get_result()
    print("\t------------------------------------------------------")
    print("\t  Top Code Breakers")
    print("\t------------------------------------------------------")
    if len(data) == 0:
        print("\t  None is in the ranking...")
    # each reuslt item is a tuple so print by the index
    for i in range(len(data)):
        print(f"\t  {i+1}. {data[i][0]} decoded {data[i][1]} in the {make_ordinal(data[i][2])} round!")
    print()

def clear_console():
    # clear the terminal depeneding on the os system
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

# add an oridnal suffix to the number and return as a string
def make_ordinal(num):
    if 11 <= num <= 13:
        suffix = "th"
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(num%10 ,4)]
    return str(num) + suffix

def play(game, code_maker, code_breaker_list):
    clear_console()
    print("\t  GAME START!")
    # loop the code breaker's action while there is a game attempt left
    while game.is_continued():
        for player in code_breaker_list.code_breaker_list:
            print()
            # if there are multiple code breakers:
                #  1. show whose turn it is
                #  2. ask for code breaker's input to show the history (avoid showing the history to others accidentally)
            if len(code_breaker_list.code_breaker_list) > 1:
                print(f"\t  {player.name}'s Turn...!\n")
                if len(player.history.history) >= 1:
                    input("\t  Please enter to see your history of guess(es) and hint(s): ")
                    print()
                    player.history.display_history()
                    print()
            print(f"\t  Life Remaining: {game.attempt}")
            print("\t------------------------------------------------------")
            # if the same guess is input, ask for another guess
            while True:
                guess = Guess(code_maker.difficulty)
                if str(guess.guess) in player.history.history.keys():
                    print("\t  You already used the number combination, pick another one!")
                    continue
                else:
                    break
            # if the guess matces the secret code:
                # 1. create the result
                # 2. insert the result in the database
                # 3. display the ranking
            if guess.guess == code_maker.secret_code:
                result = Result(player.name, code_maker.secret_code, 10-game.attempt+1)
                print(f'\t  Congratulations, {player.name}! You guessed the secret code in the {make_ordinal(result.round)} round!')
                app.insert_result(result)
                # ranking.insert_ranking(result)
                display_ranking()
                return
            # create the hint and add to the player's history with the guess
            hint = Hint(code_maker.secret_code, guess.guess)
            player.history.add_history(guess.guess, hint)
            player.history.display_history()
            # if there are multiple code breakers, ask for the input to go to the next person
            if len(code_breaker_list.code_breaker_list) > 1:
                input("\t  Please enter to go to the next code breaker: ")
                clear_console()
        game.attempt -= 1
    # when there is no more attempt left for code breakers, the code maker wins the game
    print()
    print("\t  There is no more life left for code breakers...")
    print(f"\t  {code_maker.name} won as a code maker with a secret code of {code_maker.secret_code}")
    display_ranking()
    return

if __name__ == "__main__":
    clear_console()
    print("WELCOME TO MATERMIND GAME!")
    while True:
        start = input("Would you like to (p)lay mastermind game, read (i)nstructions, check the (r)anking, or (q)uit?: ").lower()
        print()
        if start == "play" or start == "p":
            code_maker = CodeMaker()
            code_breaker_list = CodeBreakerList()
            game = Game()
            play(game, code_maker, code_breaker_list)
        elif start == "instructions" or start == "i":
            Game.show_instructions()
        elif start == "r" or start == "ranking":
            display_ranking()
        elif start == "quit" or start == "q":
            print("Thank you, bye!")
            exit()
        else:
            print("Please type a valid word.")