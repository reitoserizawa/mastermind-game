import __main__
from CodeBreaker import CodeBreaker

class CodeBreakerList:
    def __init__(self):
        self.code_breaker_count = self.set_code_breaker_count()
        self.code_breaker_list = self.set_code_breaker_list(self.code_breaker_count)

    @staticmethod
    def set_code_breaker_count():
        print()
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
    
    @staticmethod
    def set_code_breaker_list(num):
        player_list = []
        if num == 1:
            name = input("Code breaker, please type your name: ")
            return [CodeBreaker(name)]
        else:
            for i in range(num):
                name = input(f'{__main__.make_ordinal(i+1)} code breaker, please type your name: ')
                player_list.append(CodeBreaker(name))
            return player_list