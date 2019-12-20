import sys
import pygame
from pygame.locals import QUIT

class Enemy(pygame.sprite.Sprite):
	def __init__(self, character, level, number):
		"""
		arg:
			character: player number (0 for korea fish)
			level: which level's enemy (start from 0)
			number: which enemy of this level (start from 0)
		"""
		#todo: change character image to the right character (current: black)
		super(Player, self).__init__()
		self.surf = pygame.Surface((60, 90))
		self.surf.fill((0,0,0))
		self.rect = self.surf.get_rect()
		self.character = character
		self.level = level
		self.number = number

	def update(self):
		""""""
		#todo : enemy AI (move)