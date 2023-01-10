import __main__
from CodeBreaker import CodeBreaker

class CodeBreakerList:
    def __init__(self, num):
        self.players = self.set_players(num)

    @staticmethod
    def set_players(num):
        player_list = []
        if num == 1:
            name = input("Code breaker, please type your name: ")
            return [CodeBreaker(name)]
        else:
            for i in range(num):
                name = input(f'{__main__.make_ordinal(i+1)} code breaker, please type your name: ')
                player_list.append(CodeBreaker(name))
            return player_list