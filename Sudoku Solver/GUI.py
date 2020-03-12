######################################
# GUI Class for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################


import pygame
from settings import (ROWS, COLS, WIDTH, HEIGHT, WHITE, BLACK, GRID_POS,
                      NUM_OF_TILES, SIZE_OF_SQUARE, GRID_SIZE, CELL_SIZE,
                      SELECTION_COLOR, THIN, THICK, SELECTION_WIDTH, FONT_SIZE)
from functions import solve_board
import _thread


class Grid():

    def __init__(self, grid):
        """Init function for Grid class, taking settings from settings.py"""
        pygame.init()
        self.grid = grid
        self.rows = ROWS
        self.cols = COLS
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.mousePos = None
        self.selected = None

    def run(self):
        """Runs the pygame"""
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        """Checks for events until QUIT is received"""
        for event in pygame.event.get():
            # Quit game event
            if event.type == pygame.QUIT:
                self.running = False
            # Mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = self.mouseOnGrid()
                print(self.selected)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                _thread.start_new_thread(solve_board, (self.grid,))

    def update(self):
        self.mousePos = pygame.mouse.get_pos()

    def draw(self):
        """Draws the updates of the board on screen"""
        self.window.fill(WHITE)
        self.drawGrid()
        # Draw selection over grid if there is a selection
        if self.selected:
            self.drawSelection()
        self.fillWithNums()
        pygame.display.update()

    def drawGrid(self):
        """Draws the sudoku grid on top of the drawn white screen"""
        # Grid's rectangle:
        rect = (GRID_POS[0], GRID_POS[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.window, BLACK, rect, 3)
        for i in range(1, NUM_OF_TILES):  # Exclude the edges of the grid
            # Determine width
            width = THIN
            if i % SIZE_OF_SQUARE == 0:
                # Every 3 tiles, make it a bold line
                width = THICK

            # Vertical lines
            line_x = (GRID_POS[0] + GRID_SIZE / NUM_OF_TILES * i)
            # Starting position for the line
            start_pos = (line_x, GRID_POS[1])
            # Ending position for the line
            end_pos = (line_x, GRID_SIZE + GRID_POS[1])
            pygame.draw.line(self.window, BLACK, start_pos, end_pos, width)

            # Horizontal lines
            line_y = (GRID_POS[1] + GRID_SIZE / NUM_OF_TILES * i)
            # Starting position for the line
            start_pos = (GRID_POS[0], line_y)
            # Ending position for the line
            end_pos = (GRID_POS[0] + GRID_SIZE, line_y)
            pygame.draw.line(self.window, BLACK, start_pos, end_pos, width)

    def mouseOnGrid(self):
        # Compare mouse (x,y) with grid bounds
        if (self.mousePos[0] < GRID_POS[0] or
            self.mousePos[0] > (GRID_POS[0] + GRID_SIZE) or
            self.mousePos[1] < GRID_POS[1] or
                self.mousePos[1] > (GRID_POS[1] + GRID_SIZE)):
            return None
        # Return tile position: (0 - 8, 0 - 8)
        return (int((self.mousePos[0] - GRID_POS[0]) / CELL_SIZE),
                int((self.mousePos[1] - GRID_POS[1]) / CELL_SIZE))

    def drawSelection(self):
        # Draws a line over the selected tile
        rect_x = self.selected[0] * CELL_SIZE + GRID_POS[0]
        rect_y = self.selected[1] * CELL_SIZE + GRID_POS[1]
        rect = (rect_x, rect_y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.window, SELECTION_COLOR, rect, SELECTION_WIDTH)
        # No return

    def fillWithNums(self):
        """ Fills the grid with the numbers in the grid array """
        for i in range(ROWS):
            for j in range(COLS):
                if self.grid[i][j] != 0:
                    self.displayNum(self.grid[i][j], j, i)

    def displayNum(self, num, x, y):
        font = pygame.font.SysFont('comicsansms', FONT_SIZE)
        text_surf = font.render(str(num), True, BLACK)
        text_rect = text_surf.get_rect()
        # Center the text inside the box
        text_x = GRID_POS[0] + (CELL_SIZE * x) + (CELL_SIZE / 2)
        text_y = GRID_POS[1] + (CELL_SIZE * y) + (CELL_SIZE / 2)
        text_rect.center = (text_x, text_y)
        # Display the number
        self.window.blit(text_surf, text_rect)
