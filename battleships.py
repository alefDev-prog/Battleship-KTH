'''
	Allan Efendic
'''

from Board import Board
from random import randint
from Ship import Ship

BOARD_SIZE=9
NUMBER_SHIPS = 3


#Initializes the game with GUI etc
def initGame():
	Y_COORDINATES = ["A","B", "C", "D", "E", "F", "G", "H"]
	shipList = []
	boardArr = [['']*BOARD_SIZE for _ in range(BOARD_SIZE)]

	highScoreList = readHighScore()

	for y in range(0, BOARD_SIZE):
		for x in range(0, BOARD_SIZE):
			if(y == 0 and x != 0):
				boardArr[y][x]= x
			elif (x == 0 and y != 0):
				boardArr[y][x] = Y_COORDINATES[y-1]


	for i in range(2,5):
		randomizePositions(boardArr, i, shipList)
	myGUI = Board(BOARD_SIZE, boardArr, shipList, highScoreList)

                           
    
# Goes through the proposed positions of the boats and their neighbouring tiles, to ensure that
# there is no boat already there
def isValidPosition(arr, startX, startY, length, alignment):
	for dy in [-1,0,1]:
		for dx in [-1,0,1]:
			if alignment == 1:
				for y in range(startY + dy, startY+length+dy):
					if 0 <= startX + dx < BOARD_SIZE and 0 <= y < BOARD_SIZE and arr[startX+dx][y] == "X":
						return False
			else: 
				for x in range(startX + dx, startX+length+dx):
					if 0 <= startY + dy < BOARD_SIZE and 0 <= x < BOARD_SIZE and arr[x][startY+dy] == "X":
						return False
	return True


   

#Randomizes the boat positions until all the boats have permissible positions
# Three boats (1 squares, 2 squares and 3 squares)
def randomizePositions(arr, length, shipList):
    #0 for horizontal, 1 for vertical
	alignment = randint(0,1)
	valid = False
	while not valid:
		startX = 0
		startY = 0
		if alignment == 1:
			startX = randint(1,BOARD_SIZE-1)
			startY = randint(1,BOARD_SIZE-length)
			valid = isValidPosition(arr, startX, startY, length, alignment)
			shipList.append(Ship(alignment, length, startX, startY))

		else:
			startX = randint(1,BOARD_SIZE-length)
			startY = randint(1,BOARD_SIZE-1)
			valid = isValidPosition(arr, startX, startY, length, alignment)
			shipList.append(Ship(alignment, length, startX, startY))
			
	if alignment == 1:
		for y in range(startY, startY + length):
			arr[startX][y] = "X"
	else:
		for x in range(startX, startX+ length):
			arr[x][startY] = "X"
		

#Reads the highScoreList and sorts it
def readHighScore():
	f = open("highscore.txt", "r")
	strList = f.readlines()
	f.close()

	processedList = []

	for player in strList:
		player = player.strip()  # remove the newline character
		entry = player.split(",")
		processedList.append(entry)
	
	return processedList


	


def main():

	initGame()

if __name__ == "__main__":
	main()