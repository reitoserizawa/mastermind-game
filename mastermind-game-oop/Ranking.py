class Ranking:
    def __init__(self):
        self.ranking = []
    
    # result
    def insert_ranking(self, result):
        self.ranking.append(result)
        self.ranking.sort(key=lambda x:(x.attempt))
    
    def display_ranking(self):
        # show ranking
        print("\t------------------------------------------------------")
        print("\t  Top Code Breakers")
        print("\t------------------------------------------------------")
        if len(self.ranking) == 0:
            print("\t  None is in the ranking...")
        for i in range(len(self.ranking[:5])):
            print(f"\t  {i+1}. {self.ranking[i]}")
        print("\n")