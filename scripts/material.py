import sys
import os
import pygame
from pygame.locals import *

initial_pos_list = [[[(715, 495), (160, 345), (375, 210), (10, 495), (620, 80)], 
				     [(180, 330), (465, 200), (600, 65), (115, 60)],
				     [(690, 495), (510, 335), (220, 195), (120, 60)],
				     [(330, 350), (690, 85), (230, 220), (65, 65), (690, 495)],
				     [(330, 55), (560, 340), (100, 205), (560, 200), (25, 495), (740, 495), (375, 55)]]]

class Material(pygame.sprite.Sprite):
	def __init__(self, character, level, number):
		"""
		arg:
			character: player number (0 for korea fish)
			level: which level's material (start from 0)
			number: which material of this level (start from 0)
		"""
		super(Material, self).__init__()
		# image = pygame.image.load("img\\material\\level_" + str(level + 1) + "\\" + str(number) + ".png")
		image = pygame.image.load(os.path.join("img", "material", "level_" + str(level + 1) ,  str(number) + ".png"))
		self.surf = pygame.transform.scale(image, (60, 60))
		self.rect = self.surf.get_rect(topleft = initial_pos_list[character][level][number])
		self.character = character
		self.level = level
		self.number = number

	def get_rect(self):
		"""return material's rect"""
		return self.rect

	def get_surf(self):
		"""return material's surf"""
		return self.surf