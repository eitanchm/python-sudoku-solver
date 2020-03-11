######################################
# GUI Class for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################


import pygame
from pygame import *
from functions import *


class Grid():

	def __init__(self, rows, cols, width, height):
		self.rows = rows
		self.cols = cols
		self.width = width
		self.height = height
		pygame.init()
		self.running = True
	
	def run(self):
		while self.running:
			self.events()
			self.update()
			self.draw()
		pygame.quit()

	def draw(self):
		font = pygame.font.SysFont("comicsans", 40)
		white = [255, 255, 255]
		screen = pygame.display.set_mode((self.width, self.height))
		screen.fill(white);
		pygame.display.set_caption("Sudoku Solver")
		pygame.display.flip()
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False