########################################
# Functions file for the Sudoku solver #
#      Credit: Eitan Chmelevsky        #
########################################


NUM_OF_TILES = 9


def solve_board(board):
    for i in board:
        solve_tile(board, i)


def solve_tile(board, tile):
    row = tile / NUM_OF_TILES
    col = tile % NUM_OF_TILES
    if board[row][col] == 0:
        


def check_row(board, tile):
    row = tile / NUM_OF_TILES
    for i in board:



def check_col(board, tile):


