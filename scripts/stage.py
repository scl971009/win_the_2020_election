import sys
import pygame
from pygame.locals import QUIT

def start(self, window_surface, character, level):
	path = "img\\stage\\stage" + str(character) + str(level) + ".png"
	background = pygame.image.load(path)

class Stage():
	def __init__(self, window_surface, character, level):
		""""""
		self.window_surface = window_surface
		self.character = character
		self.level = level
		self.success = False

	def run(self):
		self.success = start(self.window_surface, self.character, self.level)

	def get_result(self):
		return self.success