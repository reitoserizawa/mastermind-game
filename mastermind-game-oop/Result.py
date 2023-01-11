# this class holds the information of who won the game
class Result:
    def __init__(self, name, is_code_maker, secret_code, attempt):
        self.name = name
        self.is_code_maker = is_code_maker
        self.secret_code = secret_code
        self.attempt = attempt
    
    def __repr__(self):
        if self.is_code_maker:
            return f'{self.name} won as a code maker with {self.secret_code}'
        else:
            return f'{self.name} decoded {self.secret_code} by {self.attempt} attempt(s)!'