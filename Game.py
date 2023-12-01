
class Game:

    def __init__(self):
        self.hits = 0
        self.shots = 0
        self.sunkenBoats = 0
        self.score = 0.0

    #Update data if missed
    def miss(self):
        self.shots += 1
    
    #Update data if hit
    def hit(self):
        self.hits +=1
        self.shots +=1
