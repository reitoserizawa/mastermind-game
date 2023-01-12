# this class holds the result as ranking
class Ranking:
    def __init__(self):
        self.ranking = []
    
    # inserting the result in the ranking
    def insert_ranking(self, result):
        self.ranking.append(result)
        # sort by how many attemps code breakers made an attemp to guess the secre code
        self.ranking.sort(key=lambda result:(result.round))
    
    def display_ranking(self):
        print("\t------------------------------------------------------")
        print("\t  Top Code Breakers")
        print("\t------------------------------------------------------")
        if len(self.ranking) == 0:
            print("\t  None is in the ranking...")
        # only showing top 5 results of the ranking
        for i in range(len(self.ranking[:5])):
            print(f"\t  {i+1}. {self.ranking[i]}")
        print("\n")