import random
from tabulate import tabulate


def createBeginnerTrueFalseMatrix(height, width, mineCount):
    """ creates a 8x8 matrix with 10 true, 54 false randomly placed """

    # use a list comprehension to initialize a 2d array of "false"
    matrix = [[False for x in range(width)] for y in range(height)]

    while mineCount > 0:
        # generate a random height and width
        randHeight = random.randint(0, height-1)
        randWidth  = random.randint(0, width-1 )

        # verify not already a mine
        # place and decrease counter
        if matrix[randHeight][randWidth] is not True:
            matrix[randHeight][randWidth] = True
            mineCount -= 1

    return matrix


def isValidTile(matrix, x, y):
    """ validates that x and y are within grid """
    if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
        return True
    return False


def changeIfValid(matrix, x, y):
    """ validates that x and y are within grid and not a bomb """
    if isValidTile(matrix, x, y) and matrix[x][y] != '!':
        matrix[x][y] += 1
        return True
    return False


def revealIfValid(numberMatrix, blankMatrix, x, y):
    """ checks that x,y is a valid tile, not a bomb, not yet selected and reveals the tile """
    if isValidTile(blankMatrix, x, y) and numberMatrix[x][y] != '!' and blankMatrix[x][y] == '?':
        if numberMatrix[x][y] == 0:
            blankMatrix[x][y] = ' '
            revealNeighbors(numberMatrix, blankMatrix, x, y)
        else:
            blankMatrix[x][y] = numberMatrix[x][y]
        return True
    return False


def numberFill(matrix):
    """ generates bomb neighbor counters for each tile """

    # fetch matrix of zeros
    newMatrix = createNewZeroMatrix(matrix)

    # increase counter for neighbors of bombs
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is True:
                newMatrix[i][j] = '!'
                changeIfValid(newMatrix, i  , j-1)
                changeIfValid(newMatrix, i  , j+1)
                changeIfValid(newMatrix, i+1, j  )
                changeIfValid(newMatrix, i+1, j-1)
                changeIfValid(newMatrix, i+1, j+1)
                changeIfValid(newMatrix, i-1, j  )
                changeIfValid(newMatrix, i-1, j-1)
                changeIfValid(newMatrix, i-1, j+1)

    # return the matrix with counters and blanks for bombs
    return newMatrix


def createNewZeroMatrix(matrix):
    """ creates a matrix of zeros """
    return [[0 for x in y] for y in matrix]


def createNewBlankMatrix(matrix):
    """ generates '?' matrix, this is the matrix visible to the user """
    # TODO: Change this to appropriate visual
    return [['?' for x in y] for y in matrix]


def tabulateMatrix(matrix):
    """ formats any matrix into uniform table """
    return tabulate(matrix, tablefmt="fancy_grid")


def revealClick(x, y, numberMatrix, blankMatrix):
    """ processes the user input to reveal a tile """

    if isValidTile(numberMatrix, x, y):
        if numberMatrix[x][y] == '!':
            return False, revealEndBoard(blankMatrix, numberMatrix)
        elif numberMatrix[x][y] == 0:
            blankMatrix[x][y] = ' '
            revealNeighbors(numberMatrix, blankMatrix, x, y)
        else:
            blankMatrix[x][y] = numberMatrix[x][y]
        return True, blankMatrix
    else:
        # request a valid number 'Please provide a valid number!'
        return False, blankMatrix


def revealNeighbors(numberMatrix, blankMatrix, x, y):
    """ selects the neighbors of a selection for revealing """
    revealIfValid(numberMatrix, blankMatrix, x  , y-1)
    revealIfValid(numberMatrix, blankMatrix, x  , y+1)
    revealIfValid(numberMatrix, blankMatrix, x+1, y  )
    revealIfValid(numberMatrix, blankMatrix, x+1, y-1)
    revealIfValid(numberMatrix, blankMatrix, x+1, y+1)
    revealIfValid(numberMatrix, blankMatrix, x-1, y  )
    revealIfValid(numberMatrix, blankMatrix, x-1, y-1)
    revealIfValid(numberMatrix, blankMatrix, x-1, y+1)


def revealWinningBoard(matrix):
    withBlanksBoard = [[' ' if x == 0 else x for x in y] for y in matrix]
    withFlagsBoard = [['?' if x == '!' else x for x in y] for y in withBlanksBoard]

    return withFlagsBoard


def revealEndBoard(currentBoard, numberMatrix):
    copyCurrentBoard = currentBoard
    for i in range(len(numberMatrix)):
        for j in range(len(numberMatrix[i])):
            if numberMatrix[i][j] == '!':
                copyCurrentBoard[i][j] = '*'
    return copyCurrentBoard


def gameOver(currentBoard, numberMatrix):
    winningBoard = revealWinningBoard(numberMatrix)

    for i in range(len(numberMatrix)):
        for j in range(len(numberMatrix[i])):
            if winningBoard[i][j] != currentBoard[i][j]:
                return False
    return True
