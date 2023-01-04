import requests

# create master code
def generate_secretcode():
    code = requests.get("https://www.random.org/integers/?num=4&min=1&max=6&col=1&base=10&format=plain&rnd=new")
    code = code.content.split(b'\n')
    # convert byte string to integer
    code = [int(num.decode()) for num in code[:-1]]
    print("secret code created")
    return code

# input user's guess
def generate_guessedcode():
    guessedcode = []
    while len(guessedcode) < 4:
        try:
            num = int(input(f"guess {len(guessedcode)+1}th number (from 0 to 7): "))
        except ValueError:
            print("Please pick a number!")
            continue
        if num < 0 or num > 7:
            print("number is out of range, try again!")
        else:
            guessedcode.append(num)
    return guessedcode

def create_hint(secretcode, guessedcode):
    correct_num = 0
    correct_location = 0
    secretcode = secretcode.copy()
    guessedcode = guessedcode.copy()
    for i in range(4):
        if secretcode[i] == guessedcode[i]:
            secretcode.pop(i)
            secretcode.insert(i, '*')
            correct_num += 1
    
    for i in range(4):
        if guessedcode[i] in secretcode:
            guessedcode.pop(i)
            guessedcode.insert(i, '-')
            correct_location += 1
    
    if correct_num == 0 and correct_location == 0:
        return "all incorrect!"
    else:
        return f"{correct_num} correct number and {correct_location} correct location!"

def game():
    life = 10
    secretcode = generate_secretcode()
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
        guessedcode = generate_guessedcode()
        if str(guessedcode) in used_code.keys():
            print("you already used the code! pick another one!")
            continue
        if secretcode == guessedcode:
            print("congratulations! you won!")
            break
        hint = create_hint(secretcode, guessedcode)
        print(hint)
        used_code[f"{guessedcode}"] = hint
        life -= 1
    print("game over! you lost...")

if __name__ == "__main__":
    game()