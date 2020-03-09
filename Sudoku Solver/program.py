######################################
# Main file for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################


from functions import *


def main():
    board = [[0, 4, 0, 8, 0, 5, 2, 0, 0],
             [0, 2, 0, 0, 4, 0, 0, 5, 0],
             [5, 0, 0, 0, 0, 0, 0, 0, 4],
             [0, 9, 0, 0, 0, 3, 1, 2, 0],
             [1, 0, 6, 0, 7, 8, 0, 0, 3],
             [3, 7, 0, 9, 0, 4, 0, 8, 0],
             [0, 0, 0, 0, 0, 6, 7, 0, 0],
             [0, 0, 8, 3, 5, 9, 0, 1, 0],
             [0, 1, 9, 0, 0, 7, 6, 0, 0]]
    print(solve_board(board))
    input("Press Enter to continue...")


if __name__ == '__main__':
    main()
