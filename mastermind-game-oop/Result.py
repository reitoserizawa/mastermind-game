import __main__

# result class holds the information of code breaker winner and send it to the database
class Result:
    def __init__(self, name, secret_code, round):
        self.name = name
        self.secret_code = secret_code
        self.round = round