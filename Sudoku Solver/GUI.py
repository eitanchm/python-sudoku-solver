######################################
# GUI Class for Python Sudoku solver #
#      Credit: Eitan Chmelevsky      #
######################################


import pygame
from pygame import *
from functions import *


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
		pass