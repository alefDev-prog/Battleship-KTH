import tkinter as tk
from Game import Game

#This is the class for the GUI
class Board:

    def __init__(self, size, arr, shipList, highScoreList):
        
        self.gameOver = False

        self.strArr = arr
        self.btnArr = [['']*size for i in range(size)]
        self.size = size
        self.shipList = shipList
        self.highScoreList = highScoreList

        self.root = tk.Tk()
        self.root.title('Battleship')

        self.button_frame = tk.Frame(self.root)
        self.other_frame = tk.Frame(self.root)

        self.other_frame.pack(side=tk.TOP)
        self.button_frame.pack()

        self.endBTN = tk.Button(self.other_frame, text="End", command=self.end)
        self.endBTN.grid(row=0, column=1)

        self.cheatBtn = tk.Button(self.other_frame, text="Cheat", command=self.cheat)
        self.cheatBtn.grid(row=0, column=0)
        self.cheating = False

        self.score = 0.0
        self.strScore = tk.StringVar()
        self.strScore.set("")
        self.scoreLabel = tk.Label(self.other_frame, text="Hit-percentage:")
        self.scoreLabel.grid(row=1, column=0)
        self.scoreResult = tk.Label(self.other_frame, textvariable=self.strScore)
        self.scoreResult.grid(row=1, column=1)

        self.initButtons(self.size)

        self.game = Game()
                
        self.root.mainloop()
    

    def initButtons(self, size):
        for i in range(size):
            self.btnArr[i] = []
            for j in range(size):
                button = tk.Button(self.button_frame, height=2, width=4)
                button.grid(row=i, column=j)
                self.btnArr[i].append(button)
                
                if i == 0 or j == 0:
                    button.config(text=self.strArr[i][j])
                else:
                    button.config(command=lambda button=button: self.shoot(button))

    #switches between cheating and not cheating
    def cheat(event):
        if not event.cheating:

            for i in range (event.size):
                for j in range(event.size):
                    if event.strArr[i][j] == "#":
                        continue
                    elif event.strArr[i][j] == "X":
                        event.btnArr[i][j].config(text="X")
            
          
        else:
            
            for i in range (event.size):
                for j in range(event.size):
                    if event.strArr[i][j] == "#":
                        continue
                    elif event.strArr[i][j] == "X":
                        event.btnArr[i][j].config(text="")
        event.cheating = not event.cheating

    

    #user shoots on a box
    def shoot(event, button):
        
        if(event.gameOver):
            return

        gridInfo = button.grid_info()
        row = gridInfo["row"]
        col = gridInfo["column"]
       
        if(event.strArr[row][col] == "X"):
            event.game.hit()
            button.config(text="#")
            event.strArr[row][col] = "#"

            event.updateShips(row, col)
        elif event.strArr[row][col] == "#" or event.strArr[row][col] == "O":
            return
        else:
            event.game.miss()
            button.config(text = "O")
            event.strArr[row][col] = "O"
        
        shots = event.game.shots
        hits = event.game.hits


        newScore = round(hits/shots,3)
        event.score = newScore
        
        event.strScore.set((str(round(newScore*100)))+"%")

        #Checks win
        if(hits == 9):
            print("You have won!!!")
            event.gameOver = True
            event.victory()



    #updates the status of the ships in shipList
    def updateShips(self, row, col):
        for ship in self.shipList:
            if ship.sunken:
                print("going over")
                continue
            
            hitCounter = 0    
            if ship.vertical:
                for y in range(ship.startY, ship.startY + ship.length):
                    if self.strArr[ship.startX][y] == "#":
                        print("#")
                        hitCounter +=1
            else:
                for x in range(ship.startX, ship.startX + ship.length):
                    if self.strArr[x][ship.startY] == "#":
                        print("#")
                        hitCounter +=1
            
            #checks if newly sunken ship
            if hitCounter == ship.length:
                ship.sunken = True
                print("Sunken")
                self.showAlert("You have sunken a ship!")
                self.newlySunken(ship)
        
        
               
    def newlySunken(self, ship):
        startX = ship.startX
        startY = ship.startY
        vertical = ship.vertical
        length = ship.length

        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if vertical:
                    for y in range(startY + dy, startY+length+dy):
                        if 1 <= startX + dx < self.size and 1 <= y < self.size and self.strArr[startX+dx][y] != "#":
                            self.strArr[startX + dx][y] = "O"
                            self.btnArr[startX + dx][y].config(text = "O")
                else: 
                    for x in range(startX + dx, startX+length+dx):
                        if 1 <= startY + dy < self.size and 1 <= x < self.size and self.strArr[x][startY+dy] != "#":
                            self.strArr[x][startY + dy] = "O"
                            self.btnArr[x][startY + dy].config(text = "O")


    
    #Shows a pop-up message at the bottom of the window, for 2 sec
    def showAlert(self, message):
        self.alertLabel = tk.Label(self.root, text=message)
        self.alertLabel.pack()
        self.root.after(2000, self.clearAlert) 

    #Clears the pop-up message by removing the Tkinter widget
    def clearAlert(self):
        self.alertLabel.pack_forget()

    
    #sets the name of the gamer
    def setName(self, name):
        if(name == ""):
            return 
        
        score = str(self.score*100)
        self.highScoreList.append([name, score])
        sortedHighScoreList = sorted(self.highScoreList, key=lambda x: float(x[1]),reverse=True)


        with open("highscore.txt", "w") as f:
            for sub_list in sortedHighScoreList:
                f.write(",".join(map(str, sub_list))+"\n")

        self.end()


    def checkTenBest(self):
        counter = 0
        print(self.highScoreList)
        for player in self.highScoreList:
            print(player)
            if self.score*100 < float(player[1]):
                counter +=1
        if counter < 10:
            return True
        else:
            return False
        

        
    #Ends the program by the click of a button
    def end(event):
        event.root.destroy()

    
    #Controls the end of the game, when a user has sunken all ships
    def victory(self):
        
        openForm = self.checkTenBest()

        if openForm:

            congratsLabel = tk.Label(self.root, text="You were among the top 10")
            congratsLabel.pack()
            formLabel = tk.Label(self.root, text="Enter your name:")
            formLabel.pack()

            self.nameEntry = tk.Entry(self.root)
            self.nameEntry.pack()

            submit_button = tk.Button(self.root, text="Submit", command=lambda: self.setName(self.nameEntry.get()))        
            submit_button.pack()
        else:
            congratsLabel = tk.Label(self.root, text="You won, but are not among top 10")
            congratsLabel.pack()

    


