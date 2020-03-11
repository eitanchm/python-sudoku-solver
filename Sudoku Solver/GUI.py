######################################
# GUI Class for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################


import pygame
from pygame import *
from functions import *


class Grid():

	def __init__(self, rows, cols):
		pygame.init()
		self.rows = rows
		self.cols = cols
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		self.running = True
	
	def run(self):
		while self.running:
			self.events()
			self.update()
			self.draw()
		pygame.quit()
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
	
	def update(self):
		pass

	def draw(self):
		self.window.fill(WHITE)
		pygame.display.set_caption("Sudoku Solver")
		pygame.display.flip()