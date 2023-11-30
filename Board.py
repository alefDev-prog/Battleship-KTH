import tkinter as tk

#This is the class for the GUI
class Board:

    def __init__(self, size, arr):
        self.strArr = arr
        self.btnArr = [['']*size for _ in range(size)]
        self.size = size
        self.root = tk.Tk()
        self.root.title('Battleship')
        self.cheatBtn = tk.Button(self.root,text="Cheat", command=self.cheat)
        self.cheatBtn.grid(row=0, column=0)
        self.cheating = False

        #Initializes the button matrix
        for i in range(size):
            self.btnArr[i] = []
            for j in range(size):
                button = None
                if i == 0 or j == 0:
                    button = tk.Button(self.root, height=2, width=4, text=self.strArr[i][j])
                else:
                    button = tk.Button(self.root, height=2, width=4, text="")
                
                button.grid(row=i+1, column=j)
                self.btnArr[i].append(button)
        
        self.root.mainloop()

    #switches between cheating and not cheating
    def cheat(event):
        if not event.cheating:

            for i in range (event.size):
                for j in range(event.size):
                    if event.strArr[i][j] == "X":
                        event.btnArr[i][j].config(text="X")
            
          
        else:
            
            for i in range (event.size):
                for j in range(event.size):
                    if event.strArr[i][j] == "X":
                        event.btnArr[i][j].config(text="")
        event.cheating = not event.cheating
               

        



