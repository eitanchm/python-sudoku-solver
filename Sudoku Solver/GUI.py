######################################
# GUI Class for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################

import pygame


class Grid:

	def __init__(self, rows, cols, width, height):
		self.rows = rows
		self.cols = cols
		self.width = width
		self.height = height
		pygame.init()


	def draw(self):
		pygame.display.set_mode((self.width, self.height))
		
