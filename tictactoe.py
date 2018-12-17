#X WINS
#O WINS
#DRAW
#ERROR

#Get the board
gridX, gridY = map(int, input().split(" "))
board = []
for i in range(gridY):
    board.append(list(input()))
print(board)


def NumberOfTics(board):
    Xs = 0
    Os = 0
    Empty = 0
    for i in board:
        for item in i:
            if item == "X":
                Xs += 1
            elif item =="O":
                Os += 1
            elif item ==".":
                Empty += 1
            else:
                print("ERROR")

    return Xs, Os, Empty

def Winner(board, letter):
    existsInRows = 0
    positionInRow = []
    currentPosition
    #Horizontally and Diagonally
    for i in board:
        for item in range(len(i)):
            if letter == i:
                existsInRows += 1
    if existsInRows >= 3:


    #Vertically



#Interpret the board

#Measure amount of both tics
#Measure amount of turns
