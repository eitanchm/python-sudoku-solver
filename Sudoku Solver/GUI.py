######################################
# GUI Class for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################


import pygame
from settings import (ROWS, COLS, WIDTH, HEIGHT, WHITE, BLACK, GRID_POS,
                      NUM_OF_TILES, SIZE_OF_SQUARE)
# from functions import *


class Grid():

    def __init__(self, grid):
        """Init function for Grid class, taking settings from settings.py"""
        pygame.init()
        self.grid = grid
        self.rows = ROWS
        self.cols = COLS
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

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
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        """Draws the updates of the board on screen"""
        self.window.fill(WHITE)
        self.drawGrid()
        pygame.display.update()

    def drawGrid(self):
        """Draws the sudoku grid on top of the drawn white screen"""
        grid_width = WIDTH - 60  # Grid's right line
        grid_height = HEIGHT - 60  # Grid's down line
        # Grid's rectangle:
        rect = (GRID_POS[0], GRID_POS[1], grid_width, grid_height)
        pygame.draw.rect(self.window, BLACK, rect, 3)
        for i in range(1, NUM_OF_TILES):  # Exclude the edges of the grid
            width = 1
            if i % SIZE_OF_SQUARE == 0:
                # Every 3 tiles, make it a bold line
                width = 3

            # Vertical lines:
            line_x = (GRID_POS[0] + grid_width / NUM_OF_TILES * i)
            # Starting position for the line
            start_pos = (line_x, GRID_POS[1])
            # Ending position for the line
            end_pos = (line_x, grid_height + GRID_POS[1])
            pygame.draw.line(self.window, BLACK, start_pos, end_pos, width)

            # Horizontal lines:
            line_y = (GRID_POS[1] + grid_height / NUM_OF_TILES * i)
            # Starting position for the line
            start_pos = (GRID_POS[0], line_y)
            # Ending position for the line
            end_pos = (GRID_POS[0] + grid_width, line_y)
            pygame.draw.line(self.window, BLACK, start_pos, end_pos, width)
