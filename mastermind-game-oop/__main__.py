import os
from sys import platform
from Game import Game
from CodeMaker import CodeMaker
from CodeBreakerList import CodeBreakerList
from Guess import Guess
from Hint import Hint
from Result import Result
from Ranking import Ranking

ranking = Ranking() #hold the result of the game if the code breaker breaks the secret code

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

def play(game):
    clear_console()
    print("\t  GAME START!")
    # loop the code breaker's action while there is a game attempt left
    while game.is_continued():
        for player in game.code_breaker_list.code_breaker_list:
            print()
            # if there are multiple code breakers:
                #  1. show whose turn it is
                #  2. ask for code breaker's input to show the history (avoid showing the history to others accidentally)
            if len(game.code_breaker_list.code_breaker_list) > 1:
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
                guess = Guess(game.code_maker.difficulty)
                if str(guess.guess) in player.history.history.keys():
                    print("\t  You already used the number combination, pick another one!")
                    continue
                else:
                    break
            # if the guess matces the secret code:
                # 1. print the result
                # 2. insert the result in the ranking and display it
            if guess.guess == game.code_maker.secret_code:
                print(f"\t  Congratulations, {player.name}! You won!")
                result = Result(player.name, False, game.code_maker.secret_code, 10-game.attempt+1)
                print(f"\t  {result}")
                ranking.insert_ranking(result)
                ranking.display_ranking()
                return
            # create the hint and add to the player's history with the guess
            hint = Hint(game.code_maker.secret_code, guess.guess)
            player.history.add_history(guess.guess, hint)
            player.history.display_history()
            # if there are multiple code breakers, ask for the input to go to the next person
            if len(game.code_breaker_list.code_breaker_list) > 1:
                input("\t  Please enter to go to the next code breaker: ")
                clear_console()
        game.attempt -= 1
    # when there is no more attempt left, the code maker wins the game
    print()
    print("\t  There is no more life left...")
    result = Result(game.code_maker.name, True, game.code_maker.secret_code, game.attempt)
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
            play(game)
        elif start == "instructions" or start == "i":
            Game.show_instructions()
        elif start == "quit" or start == "q":
            print("Thank you, bye!")
            exit()
        else:
            print("Please type a valid word.")