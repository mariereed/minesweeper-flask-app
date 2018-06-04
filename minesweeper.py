import random


def create_true_false_matrix(height, width, mine_count):
    """ creates a {width}x{height} matrix with {mine_count} true randomly placed, the rest false """

    # use a list comprehension to initialize a 2d array of "false"
    matrix = [[False for x in range(width)] for y in range(height)]

    while mine_count > 0:
        # generate a random height and width
        rand_height = random.randint(0, height-1)
        rand_width  = random.randint(0, width-1 )

        # verify not already a mine, place and decrease counter
        if  matrix[rand_height][rand_width] is not True:
            matrix[rand_height][rand_width] = True
            mine_count -= 1
    return matrix


def is_valid_tile(matrix, x, y):
    """ validates that x and y are within grid """
    if  x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
        return True
    return False


def change_if_valid(matrix, x, y):
    """ validates that x and y are within grid and not a bomb """
    if  is_valid_tile(matrix, x, y) and matrix[x][y] != '!':
        matrix[x][y] += 1
        return True
    return False


def reveal_if_valid(answer_matrix, current_board, x, y):
    """ checks that x,y is a valid tile, not a bomb, not yet selected and reveals the tile """
    if  is_valid_tile(current_board, x, y) and answer_matrix[x][y] != '!' and current_board[x][y] == '?':
        if answer_matrix[x][y] == 0:
            current_board[x][y] = ' '
            reveal_neighbors(answer_matrix, current_board, x, y)
        else:
            current_board[x][y] = answer_matrix[x][y]
        return True
    return False


def number_fill(matrix):
    """ generates bomb neighbor counters for each tile """

    # fetch matrix of zeros
    new_matrix = create_new_zero_matrix(matrix)

    # increase counter for neighbors of bombs
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is True:
                new_matrix[i][j] = '!'
                change_if_valid(new_matrix, i  , j-1)
                change_if_valid(new_matrix, i  , j+1)
                change_if_valid(new_matrix, i+1, j  )
                change_if_valid(new_matrix, i+1, j-1)
                change_if_valid(new_matrix, i+1, j+1)
                change_if_valid(new_matrix, i-1, j  )
                change_if_valid(new_matrix, i-1, j-1)
                change_if_valid(new_matrix, i-1, j+1)

    return new_matrix


def create_new_zero_matrix(matrix):
    """ creates a matrix of zeros """
    return [[0 for x in y] for y in matrix]


def create_new_blank_matrix(matrix):
    """ generates '?' matrix, this is the matrix visible to the user """
    return [['?' for x in y] for y in matrix]


def reveal_click(x, y, answer_matrix, current_board):
    """ processes the user input to reveal a tile """

    if  is_valid_tile(answer_matrix, x, y):
        if answer_matrix[x][y] == '!':
            return False, reveal_end_board(current_board, answer_matrix)
        elif answer_matrix[x][y] == 0:
            current_board[x][y]  = ' '
            reveal_neighbors(answer_matrix, current_board, x, y)
        else:
            current_board[x][y] = answer_matrix[x][y]
        return True, current_board
    else:
        return False, current_board


def reveal_neighbors(answer_matrix, current_board, x, y):
    """ selects the neighbors of a selection for revealing """
    reveal_if_valid(answer_matrix, current_board, x  , y-1)
    reveal_if_valid(answer_matrix, current_board, x  , y+1)
    reveal_if_valid(answer_matrix, current_board, x+1, y  )
    reveal_if_valid(answer_matrix, current_board, x+1, y-1)
    reveal_if_valid(answer_matrix, current_board, x+1, y+1)
    reveal_if_valid(answer_matrix, current_board, x-1, y  )
    reveal_if_valid(answer_matrix, current_board, x-1, y-1)
    reveal_if_valid(answer_matrix, current_board, x-1, y+1)


def reveal_winning_board(matrix):
    """ provides the winning board with same formatting as the current_board """
    with_blanks_board    = [[' ' if x == 0 else x for x in y] for y in matrix]
    with_questions_board = [['?' if x == '!' else x for x in y] for y in with_blanks_board]
    return with_questions_board


def reveal_end_board(current_board, answer_matrix):
    """ provides the current_board with all mines revealed """
    copy_current_board = current_board
    for i in range(len(answer_matrix)):
        for j in range(len(answer_matrix[i])):
            if answer_matrix[i][j] == '!':
                copy_current_board[i][j] = '*'
    return copy_current_board


def game_over(current_board, answer_matrix):
    """ determines whether game is won or not """
    winning_board = reveal_winning_board(answer_matrix)

    for i in range(len(answer_matrix)):
        for j in range(len(answer_matrix[i])):
            if winning_board[i][j] != current_board[i][j]:
                return False
    return True
