import requests

# create master code
def generate_secretcode(difficulty):
    code = requests.get(f"https://www.random.org/integers/?num={difficulty}&min=1&max=6&col=1&base=10&format=plain&rnd=new")
    code = code.content.split(b'\n')
    # convert byte string to integer
    code = [int(num.decode()) for num in code[:-1]]
    print("secret code created")
    return code

# create user's guessed code
def generate_guessedcode(difficulty):
    guessedcode = []
    while len(guessedcode) < difficulty:
        try:
            num = int(input(f"guess {len(guessedcode)+1}th number (from 0 to 7): "))
        # if value error, print out error message
        except ValueError:
            print("Please pick a number!")
            continue
        # if num is not valid, print out error message
        if num < 0 or num > 7:
            print("number is out of range, try again!")
        else:
            guessedcode.append(num)
    return guessedcode

# create hint
def create_hint(secretcode, guessedcode):
    correct_num = 0
    correct_location = 0
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
            guessedcode[i] = '-'
            correct_num += 1
            
    # return message
    if correct_num == 0 and correct_location == 0:
        return "all incorrect!"
    else:
        return f"{correct_num} correct number and {correct_location} correct location!"

def set_difficulty():
    print("please select the difficulty")
    while True:
        difficulty = input("easy: 4 numbers of secret code\nmedium: 5 numbers of secret code\nhard: 6 numbers of secret code\n")
        if difficulty == "easy": return 4
        elif difficulty == "medium": return 5
        elif difficulty == "hard": return 6
        else:
            print("please select the valid difficulty(easy/medium/hard)")

def game():
    life = 10
    difficulty = set_difficulty()
    secretcode = generate_secretcode(difficulty)
    used_code = dict()
    while life != 0:
        print(secretcode)
        print("\n")
        print(f"you have {life} life left!")
        if len(used_code) > 0:
            print("used codes and hints:")
            for k, v in used_code.items():
                print(f"\tcode: {k}")
                print(f"\thint: {v}")
                print("\n")
        guessedcode = generate_guessedcode(difficulty)
        if str(guessedcode) in used_code.keys():
            print("you already used the code! pick another one!")
            continue
        if secretcode == guessedcode:
            print("congratulations! you won!")
            return
        hint = create_hint(secretcode, guessedcode)
        print(hint)
        used_code[f"{guessedcode}"] = hint
        life -= 1
    print("game over! you lost...")

if __name__ == "__main__":
    while True:
        start = input("would you like to play mastermind, read instructions, or quit?\n")
        if start == "play":
            game()
        elif start == "instructions":
            print("at the start, computer will randomly select a pattern of numbers from a total of 8 different numbers(from 0 to 7)")
            print("a player will have 10 lifes to guess the number combinations")
            print("at the end of each fuessm computer will provide a feedback")
        elif start == "quit":
            print("thank you")
            exit()
        else:
            print("please type the valid words")