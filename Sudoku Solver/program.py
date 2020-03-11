######################################
# Main file for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################


from GUI import *


def main():
    hard_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 3, 6, 0, 0, 0, 0, 0],
                   [0, 7, 0, 0, 9, 0, 2, 0, 0],
                   [0, 5, 0, 0, 0, 7, 0, 0, 0],
                   [0, 0, 0, 0, 4, 5, 7, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 3, 0],
                   [0, 0, 1, 0, 0, 0, 0, 6, 8],
                   [0, 0, 8, 5, 0, 0, 0, 1, 0],
                   [0, 9, 0, 0, 0, 0, 4, 0, 0]]
    grid = Grid.__init__(9, 9, 500, 500)
    grid.draw()
    for i in range(9):
        for j in range(9):
            print(hard_sudoku[i][j], " ", end='')
        print()
    input("Press Enter to continue...")


if __name__ == '__main__':
    main()
