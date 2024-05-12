# Written by Thien K. M. Bui <kevinbui904@gmail.com>
# Adapted from Al Sweigart's twenty-forty-eight problem in Python
# Retrieved May 12, 2024 https://inventwithpython.com/bigbookpython/project79.html 

import random, sys

#blank constant to represent empty spaces on board
BLANK = ''

def main():
    print("Twenty Forty-Eight")

    input('Press Enter to begin...')
    gameBoard = getNewBoard()
    print(gameBoard)

    while True: #Main game loop
        print("hello")
        drawBoard(gameBoard)
        print('Score:', getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()


def getNewBoard():
    '''
    Return new board object (dictionary with keys of (x,y) tuples)
    Example:
        x0 1 2 3
        y+-+-+-+-+
        0|-|-|-|-|
         +-+-+-+-+
        1| | | | |
         +-+-+-+-+
        3|-|-|-|-|
         +-+-+-+-+
    '''

    newBoard = {} 

    #drawing blank board
    for x in range(4):
        for y in range(4):
            newBoard[(x,y)] = BLANK
    
    startingTwosPlaced = 0 #number of starting twos to be placed
    while startingTwosPlaced < 2: 
        randomSpace = (random.randint(0,3), random.randint(0,3))
        #make sure randomly selected space isn't taken
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] == 2
        
    return newBoard

def drawBoard(board):
    '''draw the board data structure'''

    labels = []
    for y in range(4):
        for x in range(4):
            tile = board[(x,y)] #getting tile at space
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|     |     |
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|     |     |
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|     |     |
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|     |     |
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))
 
def getScore(board):
    """Returns sum of all tiles"""
    score = 0
    for x in range(4):
        for y in range(4):
            #Only add non-blank tiles to the score
            if board[(x,y)] != BLANK:
                score = score + board[(x,y)]
    return score

def combineTilesInColumn(column):
    """Logic to combine the 4x4 tiles"""

    combinedTiles = []
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])
    
    #keep adding blanks until 4 tiles
    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)
    
    for i in range(3):
        if combinedTiles[i] == combinedTiles[i+1]:
            combinedTiles[i] *= 2 # Double number in tile
            for aboveIndex in range(i+ 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK #topmost space always blank to add more numbers

    return combinedTiles

def makeMove(board,move):
    """Carries out move on the board"""
    if move == 'W':
        allColumnsSpaces = [
            [(0,0), (0,1), (0,2), (0,3)],
            [(1,0), (1,1), (1,2), (1,3)],
            [(2,0), (2,1), (2,2), (2,3)],
            [(3,0), (3,1), (3,2), (3,3)],
        ]
    elif move == 'A':
        allColumnsSpaces = [
            [(0,0), (1,0), (2,0), (3,0)],
            [(0,1), (1,1), (2,1), (3,1)],
            [(0,2), (1,2), (2,2), (3,2)],
            [(0,3), (1,3), (2,3), (3,3)],
        ]
    elif move == 'S':
        allColumnsSpaces = [
            [(0,3), (0,2), (0,1), (0,0)],
            [(1,3), (1,2), (1,1), (1,0)],
            [(2,3), (2,2), (2,1), (2,0)],
            [(3,3), (3,2), (3,1), (3,0)],
        ]
    elif move == 'D':
        allColumnsSpaces = [
            [(3,0), (2,0), (1,0), (0,0)],
            [(3,1), (2,1), (1,1), (0,1)],
            [(3,2), (2,2), (1,2), (0,2)],
            [(3,3), (2,3), (1,3), (0,3)],
        ]
    
    boardAfterMove = {}

    for columnSpaces in allColumnsSpaces:
        firstTileSpace = columnSpaces[0]
        secondTileSpace = allColumnsSpaces[1]
        thirdTileSpace = allColumnsSpaces[2]
        fourthTileSpace = allColumnsSpaces[3]

        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]

        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)

        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]
    return boardAfterMove

def askForPlayerMove():
    """Asking for player to move"""

    print("Enter move: (WASD or Q to quit)")
    while True: #keep looping til player enter a valid move
        move = input('> ').upper()
        if move == 'Q':
            print("Thanks for playing!")
            sys.exit()
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Enter one of "WASD"')

def addTwoToBoard(board):
    while True:
        randomSpace = (random.randint(0,3), random.randint(0,3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return

def isFull(board):
    for x in range(4):
        for y in range(4):
            if board[(x,y)] == BLANK:
                return False
    return True
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()