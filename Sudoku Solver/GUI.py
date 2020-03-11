######################################
# GUI Class for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################

from pygame import *
from functions import *


class Grid:

	def __init__(self, rows, cols, width, height):
		self.rows = rows
		self.cols = cols
		self.width = width
		self.height = height
		pygame.init()


	def draw(self):
		font = pygame.font.SysFont("comicsans", 40)
		pygame.display.set_mode((self.width, self.height))
