class Ship:

    def __init__(self, vertical, length, startX, startY):
        self.vertical = vertical
        self.length = length
        self.startX = startX
        self.startY = startY
        
        self.sunken = False 
        

    def gotSunken(self):
        self.sunken = True 
           


    