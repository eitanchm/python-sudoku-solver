########################################
# Functions file for the Sudoku solver #
#      Credit: Eitan Chmelevsky        #
########################################


from settings import NUM_OF_TILES, SIZE_OF_SQUARE


def solve_board(board):
    """Gets an unsolved board and tries to solve it,
       then returns the result."""
    if find_next_empty(board) != -1:
        print('Solving...')
        solve_tile(board, find_next_empty(board))
    else:
        print('Board already solved')


def solve_tile(board, tile_index):
    """Returns all the possible solutions for a tile location"""
    row_index = int(tile_index / NUM_OF_TILES)
    col_index = tile_index % NUM_OF_TILES
    possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Checks to see if there is an empty tile
    if find_next_empty(board) == -1:
        return True
    else:
        for i in possible_nums:  # check every possible number from 1 to 9
            # check if i doesn't exist in current row, col, or square
            if i not in (get_row(board, tile_index) +
                         get_col(board, tile_index) +
                         get_square(board, tile_index)):
                # test the next possible solution
                board[row_index][col_index] = i
                # if it's not a correct solution
                if solve_tile(board, find_next_empty(board)) is not True:
                    board[row_index][col_index] = 0  # reset tile's value
                else:
                    return True  # Returns true when the board is full


def get_row(board, tile_index):
    """Gets the board and a tile index, returns its entire row in an array"""
    row_index = int(tile_index / NUM_OF_TILES)
    row = []
    # Goes through all the elements in the row and appends them to the array
    for i in board[row_index]:
        if i != 0:
            row.append(i)
    return row


def get_col(board, tile_index):
    """Gets the board and a tile index, returns its entire row in an array"""
    col_index = tile_index % NUM_OF_TILES
    col = []
    # Goes through all the elements in the collumn and appends them
    for i in range(0, NUM_OF_TILES):
        if board[i][col_index] != 0:
            col.append(board[i][col_index])  # Appends all the Column's numbers
    return col


def get_square(board, tile_index):
    """Gets the board and a tile index and returns its 3x3 square's contents"""
    row_index = int(tile_index / NUM_OF_TILES)
    col_index = tile_index % NUM_OF_TILES
    square_row = row_index
    square_col = col_index
    square = []
    # Finds where to start on the 3x3 square
    if row_index % SIZE_OF_SQUARE == 1:
        square_row = row_index - 1
    elif row_index % SIZE_OF_SQUARE == 2:
        square_row = row_index - 2
    if col_index % SIZE_OF_SQUARE == 1:
        square_col = col_index - 1
    elif col_index % SIZE_OF_SQUARE == 2:
        square_col = col_index - 2
    # Goes through all the tiles in the 3x3 square
    for i in range(0, NUM_OF_TILES):
        cur_row = square_row + int(i / SIZE_OF_SQUARE)
        cur_col = square_col + (i % SIZE_OF_SQUARE)
        if board[cur_row][cur_col] != 0:
            square.append(board[square_row + int(i / SIZE_OF_SQUARE)]
                          [square_col + (i % SIZE_OF_SQUARE)])

    return square


def is_solved(board):
    """Checks the board for empty tiles, to see if it's solved"""
    solved = True
    for i in board:
        for j in i:
            if j == 0:
                solved = False
    return solved


def find_next_empty(board):
    """Returns the first empty tile it finds"""
    empty_index = -1
    for i in range(0, len(board) * len(board)):
        row_index = int(i / NUM_OF_TILES)
        col_index = i % NUM_OF_TILES
        if board[row_index][col_index] == 0:
            empty_index = i
            break
    return empty_index
