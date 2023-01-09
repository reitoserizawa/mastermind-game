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
            difficulty_mode = "easy" if i.difficulty == 4 else "medium" if i.difficulty == 5 else "hard"
            print(f"\t  {number}. {i.winner} won {difficulty_mode} mode with {10 - i.attempt} attempts!")
            number +=1
        print("\n")