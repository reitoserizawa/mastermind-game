import __main__

# this class holds the information of code breaker winners
class Result:
    def __init__(self, name, secret_code, round):
        self.name = name
        self.secret_code = secret_code
        self.round = round