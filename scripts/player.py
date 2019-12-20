import sys
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self, character):
		""""""
		#todo: change character image to the right character (current: black)
		super(Player, self).__init__()
		self.surf = pygame.Surface((60, 90))
		self.surf.fill((0,0,0))
		self.rect = self.surf.get_rect()
		self.character = character
		self.life = 5

	def update(self, pressed_keys):
		""""""
		#todo: move when up, left, right is pressed
		if pressed_keys[K_UP]:
			print('up pressed')
		if pressed_keys[K_LEFT]:
			print('left pressed')
		if pressed_keys[K_RIGHT]:
			print('right pressed')