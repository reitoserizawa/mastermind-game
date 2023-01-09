import requests
import time
import sys
from threading import Thread

# used to store ranking results even after returning game() func
ranking = []

# create master code
def generate_secretcode(difficulty):
    code = requests.get(f"https://www.random.org/integers/?num={difficulty}&min=1&max=6&col=1&base=10&format=plain&rnd=new")
    # convert byte string to integer
    code = code.content.split(b'\n')
    code = [int(num.decode()) for num in code[:-1]]
    print("\nsecret code created\n")
    return code

# create user's guessed code
def generate_guessedcode(difficulty):
    guessedcode = []
    while len(guessedcode) < difficulty:
        try:
            num = int(input(f"\t  guess {make_ordinal(len(guessedcode)+1)} number (from 0 to 7): "))
        # if value error, print out error message
        except ValueError:
            print("Please pick a number!")
            continue
        # if num is not valid, print out error message
        if num < 0 or num > 7:
            print("number is out of range, try again!")
        else:
            guessedcode.append(num)
    print('\n')
    return guessedcode

# assign suffix depending on order of user input for guessed code
def make_ordinal(num):
    # if num is between 11 and 13, suffix is th
    if 11 <= num <= 13:
        suffix = "th"
    else:
        # if 0, suffix is th, else if 1, suffix is st...
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(num%10 ,4)]
    return str(num) + suffix

# create hint
def create_hint(secretcode, guessedcode):
    correct_num = 0
    correct_location = 0
    # make copies of codes to avoid chnaging originals since using to display history
    secretcode = secretcode.copy()
    guessedcode = guessedcode.copy()
    # mark matched num to avoid miss counting with duplicate numbers
    for i in range(len(secretcode)):
        if secretcode[i] == guessedcode[i]:
            secretcode[i] = '*'
            guessedcode[i] = '-'    
            correct_num += 1
            correct_location += 1
    for i in range(len(secretcode)):
        if guessedcode[i] in secretcode:
            secretcode[secretcode.index(guessedcode[i])] = '*'
            guessedcode[i] = '-'
            correct_num += 1
    # return hint
    if correct_num == 0 and correct_location == 0:
        return "all incorrect!"
    else:
        return f"{correct_num} correct number and {correct_location} correct location!"

# pick difficulty (easy = 4, medium = 5, hard = 6)
def set_difficulty():
    print("\nplease select the difficulty")
    while True:
        difficulty = input("(e)asy: 4 numbers of secret code\n(m)edium: 5 numbers of secret code\n(h)ard: 6 numbers of secret code\n").lower()
        if difficulty == "easy" or difficulty == "e" : return 4
        elif difficulty == "medium" or difficulty == "m": return 5
        elif difficulty == "hard" or difficulty == "h": return 6
        else:
            print("please select the valid difficulty")

# display guessed code and hint
def display_history(used_code):
    i = 1
    for k, v in used_code.items():
        print(f"\t  ROUND {i}")
        print("\t------------------------------------------------------")
        print(f"\t  Guess: {k}")
        print(f"\t  Hint: {v}")
        print("\t------------------------------------------------------")
        i += 1

# display result with ranking
def display_result(ranking, secretcode, life, total_time):
    name = input("congratulations! you won! what's your name?\n")
    rank = 1
    # convert total time to minutes and seconds
    minutes, seconds = divmod(total_time, 60)
    ranking.append({"name": name, "code": secretcode, "time": total_time})
    # rank player depending on time spent to match secretcode
    ranking.sort(key=lambda x:x["time"])
    print(f"{name}, you guessed {secretcode} in {10 - life + 1} guesses over {minutes}min {seconds}sec\n")
    # show ranking
    print("\t------------------------------------------------------")
    print("\t  Top Players")
    print("\t------------------------------------------------------")
    for i in ranking[:5]:
        minutes, seconds = divmod(i['time'], 60)
        print(f"\t  {rank}. {i['name']} decoded {i['code']} over {minutes}min {seconds}sec!")
        rank +=1
    print("\n")

def countdown(num):
    while num >= 0:
        print('\r00:{:02} left'.format(num), end="")
        time.sleep(1)
        num -= 1
    print("TIME OUT!")

def game():
    life = 10
    difficulty = set_difficulty()
    secretcode = generate_secretcode(difficulty)
    print(secretcode)
    used_code = dict()
    while life > 0:
        # start timer for ranking
        start_time = time.time()
        print(f"\t  Life Remaining: {life}")
        print("\t------------------------------------------------------")
        if len(used_code) > 0:
            display_history(used_code)
        # start countdown timer for guess code input
        # Thread(target=countdown, args=[30]).start()
        # guessedcode = Thread(generate_guessedcode(difficulty)).start()
        guessedcode = generate_guessedcode(difficulty)
        if str(guessedcode) in used_code.keys():
            print("you already used the code! pick another one!")
            continue
        if secretcode == guessedcode:
            # end timer
            end_time = time.time()
            total_time = int(end_time - start_time)
            display_result(ranking, secretcode, life, total_time)
            return
        hint = create_hint(secretcode, guessedcode)
        used_code[f"{guessedcode}"] = hint
        life -= 1
    if life == 0:
        print("game over! you lost...")
        return

if __name__ == "__main__":
    while True:
        start = input("would you like to (p)lay mastermind, read (i)nstructions, or (q)uit?\n").lower()
        if start == "play" or start == "p":
            game()
        elif start == "instructions" or start == "i":
            print("at the start, computer will randomly select a pattern of numbers from a total of 8 different numbers(from 0 to 7)")
            print("a player will have 10 lives to guess the number combinations")
            print("at the end of each guess, computer will provide a feedback\n")
        elif start == "quit" or start == "q":
            print("bye!")
            exit()
        else:
            print("please type the valid words\n")