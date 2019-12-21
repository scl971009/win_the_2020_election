import sys
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self, character, x, y):
		"""
		arg:
			character: player number (0 for korea fish)
			[x, y]: initial position
		"""
		#todo: change character image to the right character (current: black)
		super(Player, self).__init__()
		self.surf = pygame.Surface((60, 90))
		self.surf.fill((0,0,0))
		self.rect = self.surf.get_rect(topleft = (x, y))
		self.character = character
		self.life = 5
		#maybe you will need force and speed as variable... (I'm not sure. It depends on how you implement jump and gravity.)

	def gravity(self, floor_list):
		"""
		This function will be called in the main loop. Simulate gravity when no keys are pressed.

		arg:
			floot_list: the list of all floor (rect) in this stage.
		"""
		#if not colliding any floor:
			#move down (not constant velocity)
		#else:
			#handle collide
		pass

	def move_left_right(self, pressed_keys):
		""""""
		#todo: move when left, right is pressed (remember to set bounds)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)

	def jump(self):
		""""""
		#todo: jump when K_UP is pressed (should not just simply plus y position)
		print('jump')

	def get_player_rect(self):
		return self.rect

	def get_player_surf(self):
		return self.surf