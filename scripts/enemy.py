import sys
import pygame
from pygame.locals import QUIT

class Enemy(pygame.sprite.Sprite):
	def __init__(self, character):
		""""""
		#todo: change character image to the right character (current: black)
		super(Player, self).__init__()
		self.surf = pygame.Surface((60, 90))
		self.surf.fill((0,0,0))
		self.rect = self.surf.get_rect()
		self.character = character

	def update(self):
		""""""
		#todo : enemy AI (move)