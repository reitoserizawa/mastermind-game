import __main__
from CodeBreaker import CodeBreaker

# this class holds the number of code breakers and each object in the list
class CodeBreakerList:
    def __init__(self):
        self.code_breaker_list = self.set_code_breaker_list()

    @staticmethod
    def set_code_breaker_count():
        print()
        # if the number of code breakers are not correct, print an error message
        while True:
            try:
                player_num = int(input("How many code breakers? (from 1 to 4): "))
                if player_num >= 1 and player_num <= 4:
                    return int(player_num)
                else:
                    print("Please type a number from 1 to 4.")
            except ValueError:
                    print("Please type a number.")
                    continue
    
    def set_code_breaker_list(self):
        # if there is only one code breaker, simply ask for the code breaker's name
        # otherwise, ask each code breaker to input their name and add them to the list
        code_breaker_count = self.set_code_breaker_count()
        if code_breaker_count == 1:
            name = input("Code breaker, please type your name: ")
            return [CodeBreaker(name)]
        else:
            player_list = []
            for i in range(code_breaker_count):
                name = input(f'{__main__.make_ordinal(i+1)} code breaker, please type your name: ')
                player_list.append(CodeBreaker(name))
            return player_list