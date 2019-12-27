import sys
import pygame
import os
from pygame.locals import *

initial_pos_list = [[(190, 465), (190, 465)]]

class Player(pygame.sprite.Sprite):
	def __init__(self, character):
		"""
		arg:
			character: player number (0 for korea fish)
			[x, y]: initial position
		"""
		#todo: change character image to the right character (current: black)
		super(Player, self).__init__()

		image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_turnRight.png'))
		self.surf  = pygame.transform.scale(image, (60, 90))

		self.rect = self.surf.get_rect()
		#self.rect = self.surf.get_rect(topleft = (x, y))
		self.character = character
		self.life = 5
		self.stage = 0
		#maybe you will need force and speed as variable... (I'm not sure. It depends on how you implement jump and gravity.)
		#I think you might need to save initail position in case player is attacked by enemys

	def stage_start(self):
		self.rect = self.surf.get_rect(topleft = initial_pos_list[self.character][self.stage])

	def stage_clear(self):
		self.stage = self.stage + 1

	def update(self, floor_list, enemy_group):
		"""
		This function will be called in the main loop. Simulate collision with floor and enemy.
		hint: How to deal with enemy_group: pygame.sprite.spritecollideany

		arg:
			floot_list: the list of all floor (rect) in this stage.
			enemy_group: all enemy's data
		"""
		#floor part

		#if not colliding any floor:
			#move down (not constant velocity)

		#enemy part

		#if collides with enemy:
			#if attacks enemy:
				#simulate collision with enemy (maybe move up after collision)
			#else (attacked by enemy):
				#lose 1 life and sent back to the initial position
		pass

	def move_left_right(self, pressed_keys):
		""""""
		#todo: move when left, right is pressed (remember to set bounds)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
			image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_turnLeft.png'))
			self.surf  = pygame.transform.scale(image, (60, 90))
		if pressed_keys[K_RIGHT]:	
			self.rect.move_ip(5, 0)
			image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_turnRight.png'))
			self.surf  = pygame.transform.scale(image, (60, 90))
		if pressed_keys[K_UP]:

			self.jump()

	def jump(self):

                #todo: jump when K_UP is pressed (should not just simply plus y position)
		print('jump')
		y=-20
		self.rect.move_ip(0, y)
		image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_right_jump.png'))
		self.surf  = pygame.transform.scale(image, (60, 90))
		if y!=0:
			self.rect.move_ip(20, y) 
			self.rect.move_ip(20, 20) 

   
	def get_rect(self):
		return self.rect

	def get_surf(self):
		return self.surf

	def get_life(self):
		return self.life
