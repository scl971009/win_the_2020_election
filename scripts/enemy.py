import sys
import pygame
from pygame.locals import *

initial_pos_list = [[]]

class Enemy(pygame.sprite.Sprite):
	def __init__(self, character, level, number):
		"""
		arg:
			character: player number (0 for korea fish)
			level: which level's enemy (start from 0)
			number: which enemy of this level (start from 0)
		"""
		#todo: change character image to the right character (current: black)
		super(Enemy, self).__init__()
		self.surf = pygame.Surface((60, 90))
		self.surf.fill((0,0,0))
		self.rect = self.surf.get_rect()
		#self.rect = self.surf.get_rect(topleft = initial_pos_list[character][level][number])
		self.character = character
		self.level = level
		self.number = number

	def update(self, floor_list, player_rect):
		"""
		This function will be called in the main loop. Update enemy's behavior.

		arg:
			floor_list: a list of all floor's rect in this stage
			player_rect: player's current rect
		"""
		#todo : enemy AI (move)