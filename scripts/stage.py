import sys
import pygame
from pygame.locals import QUIT
from player import Player
from enemy import Enemy

def start(window_surface, character, level):
	path = "img\\stage\\stage" + str(character) + str(level) + ".png"
	background = pygame.image.load(path)
	background = pygame.transform.scale(background, (800, 600))
	background.convert()

	window_surface.blit(background, (0, 0))
	floor = pygame.Rect(0, 560, 800, 40)

	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					print(event.pos)

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