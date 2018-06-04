import random


def createBeginnerTrueFalseMatrix(height, width, mineCount):
    """ creates a 8x8 matrix with 10 true, 54 false randomly placed """

    # use a list comprehension to initialize a 2d array of "false"
    matrix = [[False for x in range(width)] for y in range(height)]

    while mineCount > 0:
        # generate a random height and width
        randHeight = random.randint(0, height-1)
        randWidth  = random.randint(0, width-1 )

        # verify not already a mine, place and decrease counter
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


def revealIfValid(answerMatrix, currentBoard, x, y):
    """ checks that x,y is a valid tile, not a bomb, not yet selected and reveals the tile """
    if isValidTile(currentBoard, x, y) and answerMatrix[x][y] != '!' and currentBoard[x][y] == '?':
        if answerMatrix[x][y] == 0:
            currentBoard[x][y] = ' '
            revealNeighbors(answerMatrix, currentBoard, x, y)
        else:
            currentBoard[x][y] = answerMatrix[x][y]
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

    return newMatrix


def createNewZeroMatrix(matrix):
    """ creates a matrix of zeros """
    return [[0 for x in y] for y in matrix]


def createNewBlankMatrix(matrix):
    """ generates '?' matrix, this is the matrix visible to the user """
    return [['?' for x in y] for y in matrix]


def revealClick(x, y, answerMatrix, currentBoard):
    """ processes the user input to reveal a tile """

    if isValidTile(answerMatrix, x, y):
        if answerMatrix[x][y] == '!':
            return False, revealEndBoard(currentBoard, answerMatrix)
        elif answerMatrix[x][y] == 0:
            currentBoard[x][y]  = ' '
            revealNeighbors(answerMatrix, currentBoard, x, y)
        else:
            currentBoard[x][y] = answerMatrix[x][y]
        return True, currentBoard
    else:
        return False, currentBoard


def revealNeighbors(answerMatrix, currentBoard, x, y):
    """ selects the neighbors of a selection for revealing """
    revealIfValid(answerMatrix, currentBoard, x  , y-1)
    revealIfValid(answerMatrix, currentBoard, x  , y+1)
    revealIfValid(answerMatrix, currentBoard, x+1, y  )
    revealIfValid(answerMatrix, currentBoard, x+1, y-1)
    revealIfValid(answerMatrix, currentBoard, x+1, y+1)
    revealIfValid(answerMatrix, currentBoard, x-1, y  )
    revealIfValid(answerMatrix, currentBoard, x-1, y-1)
    revealIfValid(answerMatrix, currentBoard, x-1, y+1)


def revealWinningBoard(matrix):
    """ provides the winningBoard with same formatting as the currentBoard """
    withBlanksBoard    = [[' ' if x == 0 else x for x in y] for y in matrix]
    withQuestionsBoard = [['?' if x == '!' else x for x in y] for y in withBlanksBoard]
    return withQuestionsBoard


def revealEndBoard(currentBoard, answerMatrix):
    """ provides the currentBoard with all mines revealed """
    copyCurrentBoard = currentBoard
    for i in range(len(answerMatrix)):
        for j in range(len(answerMatrix[i])):
            if answerMatrix[i][j] == '!':
                copyCurrentBoard[i][j] = '*'
    return copyCurrentBoard


def gameOver(currentBoard, answerMatrix):
    """ determines whether game is won or not """
    winningBoard = revealWinningBoard(answerMatrix)

    for i in range(len(answerMatrix)):
        for j in range(len(answerMatrix[i])):
            if winningBoard[i][j] != currentBoard[i][j]:
                return False
    return True
