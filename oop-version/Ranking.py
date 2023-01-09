class Ranking:
    def __init__(self):
        self.ranking = []
    
    def insert_ranking(self, game):
        self.ranking.append(game)
        self.ranking.sort(key=lambda x:(10 - x.attempt))
    
    def display_ranking(self):
        number = 1
        # show ranking
        print("\t------------------------------------------------------")
        print("\t  Top Players")
        print("\t------------------------------------------------------")
        for i in self.ranking[:5]:
            print(f"\t  {number}. {i.winner} won {i.difficulty} mode with {10 - i.attempt}")
            number +=1
        print("\n")