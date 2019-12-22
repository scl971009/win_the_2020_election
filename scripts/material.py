import sys
import pygame
from pygame.locals import *

initial_pos_list = [[[(715, 495), (160, 345), (375, 210), (10, 495), (620, 80)]]]

class Material(pygame.sprite.Sprite):
	def __init__(self, character, level, number):
		"""
		arg:
			character: player number (0 for korea fish)
			level: which level's material (start from 0)
			number: which material of this level (start from 0)
		"""
		#todo: change character image to the right character (current: black)
		super(Material, self).__init__()
		self.surf = pygame.Surface((60, 60))
		self.surf.fill((255,0,0))
		#self.rect = self.surf.get_rect()
		self.rect = self.surf.get_rect(topleft = initial_pos_list[character][level][number])
		self.character = character
		self.level = level
		self.number = number

	def get_rect(self):
		return self.rect

	def get_surf(self):
		return self.surf