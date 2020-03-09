########################################
# Functions file for the Sudoku solver #
#      Credit: Eitan Chmelevsky        #
########################################


NUM_OF_TILES = 9
SIZE_OF_SQUARE = 3


def solve_board(board):
    """Gets an unsolved board and tries to solve it, then returns the result."""
    while is_solved(board) == False:
        for i in range(0, len(board) * len(board)):
	        row_index = int(i / NUM_OF_TILES)
	        col_index = i % NUM_OF_TILES
	        if board[row_index][col_index] == 0:
	    	    board = solve_tile(board, i)
    return board


def solve_tile(board, tile_index):
    """Returns all the possible solutions for a tile location"""
    row_index = int(tile_index / NUM_OF_TILES)
    col_index = tile_index % NUM_OF_TILES
    possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_solutions = []
    """3 arrays to check all impossible solutions for the tile"""
    row = get_row(board, tile_index)
    col = get_col(board, tile_index)
    square = get_square(board, tile_index)
    """removes all impossible solutions for the tile"""
    for i in row:
    	possible_nums[i - 1] = 0
    for i in col:
    	possible_nums[i - 1] = 0
    for i in square:
    	possible_nums[i - 1] = 0
    """builds a new array to represent all possible numbers to put in the tile"""
    for i in possible_nums:
    	if i != 0:
    		possible_solutions.append(i)
    """if there is only 1 possible solution places it"""
    if len(possible_solutions) == 1:
        board[row_index][col_index] = possible_solutions[0]
    return board


def get_row(board, tile_index):
	"""Gets the board and a tile index and returns its entire row in an array"""
	row_index = int(tile_index / NUM_OF_TILES)
	col_index = tile_index % NUM_OF_TILES
	row = []
	"""Goes through all the elements in the row and appends them to the array"""
	for i in board[row_index]:
		if i != 0:
			row.append(i)
	return row


def get_col(board, tile_index):
	"""Gets the board and a tile index and returns its entire row in an array"""
	row_index = int(tile_index / NUM_OF_TILES)
	col_index = tile_index % NUM_OF_TILES
	col = []
	"""Goes through all the elements in the collumn and appends them to the array"""
	for i in range(0, NUM_OF_TILES):
		if board[i][col_index] != 0:
			col.append(board[i][col_index]) #Appends all the Column's numbers
	return col


def get_square(board, tile_index):
	"""Gets the board and a tile index and returns its 3x3 square's contents"""
	row_index = int(tile_index / NUM_OF_TILES)
	col_index = tile_index % NUM_OF_TILES
	square_row = row_index
	square_col = col_index
	square = []
	"""Finds where to start on the 3x3 square"""
	if row_index % SIZE_OF_SQUARE == 1:
		square_row = row_index - 1
	elif row_index % SIZE_OF_SQUARE == 2:
		square_row = row_index - 2
	if col_index % SIZE_OF_SQUARE == 1:
		square_col = col_index - 1
	elif col_index % SIZE_OF_SQUARE == 2:
		square_col = col_index - 2
	"""Goes through all the tiles in the 3x3 square"""
	for i in range(0, NUM_OF_TILES):
		if board[square_row + int(i / SIZE_OF_SQUARE)][square_col + (i % SIZE_OF_SQUARE)] != 0:
			square.append(board[square_row + int(i / SIZE_OF_SQUARE)][square_col + (i % SIZE_OF_SQUARE)])

	return square


def is_solved(board):
	solved = True
	for i in board:
		for j in i:
			if j == 0:
				solved = False
	return solved
