import tkinter as tk


class Board:

    def __init__(self, size, arr):
        self.root = tk.Tk()
        self.root.title('Battleship')
        self.arr = arr
        

        for i in range(size):
            for j in range(size):
                button = tk.Button(self.root, height=2, width=4, text=self.arr[i][j])
                button.grid(row=i, column=j)
        
        self.root.mainloop()

        



