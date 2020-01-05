import sys
import pygame
import os
import random
from pygame.locals import *

initial_pos_list = [[[(50, 465), (300, 315)],
					 [(50, 465), (120,30), (340,170)],
					 [(50, 465), (120,30), (340,170), (340,170), (340,170)],
					 [(50, 465), (120,30), (340,170)],
					 [(50, 465), (120,30), (340,170), (340,170)]
					 ]]  # stage1 initiail_pos
behavior_list = [[[4, 3],
				  [1, 1, 1],
				  [0, 2, 1, 0, 1],
				  [1, 2, 2],
				  [2, 1, 2, 0]
				  ]]

def get_floor(sprite, floor_list):
	floor_target = Rect(0,0,0,0)
	diff_min = 100000
	for ifloor in floor_list:			
		sprite.rect.centery
		if ifloor.left <= sprite.rect.centerx and ifloor.right >= sprite.rect.centerx:
			diff = ifloor.top - sprite.rect.bottom
			if diff >= 0 and diff_min > diff:
				diff_min = diff
				floor_target = ifloor

	return floor_target

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
		# image = pygame.image.load(os.path.join("img", "material", "level_" + str(level + 1), str(number) + ".png"))
		self.image_R = pygame.image.load(os.path.join("img", "enemy", "Level_" + str(level + 1), str(number) + "_R" + ".png"))
		self.image_L = pygame.image.load(os.path.join("img", "enemy", "Level_" + str(level + 1), str(number) + "_L" + ".png"))
		self.image_H = pygame.image.load(os.path.join("img", "enemy", "Level_" + str(level + 1), str(number) + "_hurt" + ".png"))


		self.surf = pygame.transform.scale(self.image_R, (80, 90))  # new_add

		# self.surf = pygame.Surface((60, 90))  # square_test
		# self.surf.fill((255,0,0))    # red_square

		self.rect = self.surf.get_rect(topleft = initial_pos_list[character][level][number])
		self.character = character
		self.level = level
		self.number = number

		self.b_move_right = True
		self.behavior = behavior_list[character][level][number]
		self.b_stop = False
		self.stop_time = 0

		self.jump_time = 300
		self.jump_step_total = 0

	def is_out_of_range(self, move_x, floor):
		if self.rect.left + move_x < floor.left:
			return True
		elif self.rect.right + move_x > floor.right:
			return True

		return False

	def get_floor(self, floor_list):
		floor_target = Rect(0,0,0,0)
		diff_min = 100000
		for ifloor in floor_list:			
			self.rect.centery
			if ifloor.left <= self.rect.centerx and ifloor.right >= self.rect.centerx:
				diff = ifloor.top - self.rect.bottom
				if diff >= 0 and diff_min > diff:
					diff_min = diff
					floor_target = ifloor

		return floor_target
	def is_play_in_same_floor(self, floor_list, player):
		if get_floor(self, floor_list) == get_floor(player, floor_list):
			return True
		else:
			return False

	def jump(self, jump_step_total, move_step):		
		if self.jump_step_total == 0:
			if  self.jump_time == 300:
				self.jump_step_total =jump_step_total
		else:
			self.jump_step_total-=move_step
			self.rect.move_ip(0, -move_step)	

	def gravity(self,move_step,floor):
		if self.rect.bottom + move_step < floor.top:
			self.rect.move_ip(0, move_step)
		else:
			dist=floor.top-self.rect.bottom
			self.rect.move_ip(0, dist)		 

	def behavior1(self,move_step,floor):
		if self.b_move_right:
			if self.is_out_of_range(move_step, floor):
				#dist = floor.right - self.rect.right
				#self.rect.move_ip(dist, 0)
				self.b_move_right = False   # change direction
			else:
				self.surf = pygame.transform.scale(self.image_R, (80, 90))  
				self.rect.move_ip(move_step, 0)
		else:
			if self.is_out_of_range(-move_step, floor):
				#dist = floor.left - self.rect.left
				#self.rect.move_ip(dist, 0)
				self.b_move_right = True	# rechange
			else:
				self.surf = pygame.transform.scale(self.image_L, (80, 90))  
				self.rect.move_ip(-move_step, 0)

	def update(self, floor_list, player):
		"""
		This function will be called in the main loop. Update enemy's behavior.
		arg:
			floor_list: a list of all floor's rect in this stage
			player_rect: player's current rect
		"""
		# todo : enemy AI (move)
		player_rect =player.rect
		if self.stop_time == 0:
			if pygame.sprite.collide_rect(self, player) and self.rect.centery > player.rect.centery:
				self.stop_time = 100   # enter this fun up to 100 times, then stop.
				self.b_stop = True
				self.surf = pygame.transform.scale(self.image_H, (80, 90))  
			else:
				self.b_stop = False				
				self.surf = pygame.transform.scale(self.image_R, (80, 90))  
		else:
			self.stop_time -= 1




		floor = self.get_floor(floor_list)
		player_x = player_rect.centerx
		player_y = player_rect.centery
		move_step = 3

		down_step = 5
		jump_step = down_step*2

		self.gravity(down_step,floor)

		if self.b_stop:
			return 

		if self.behavior == 0:       # random move
			local = random.randint(floor.left, floor.right)
			if local > self.rect.centerx:
				self.surf = pygame.transform.scale(self.image_R, (80, 90))  
				self.rect.move_ip(+move_step, 0)   # move_ip = move to right a unit
			elif local < self.rect.centerx:
				self.surf = pygame.transform.scale(self.image_L, (80, 90))  
				self.rect.move_ip(-move_step, 0)

		elif self.behavior == 1:      # the rightest to the leftest			
			self.behavior1(move_step,floor)
		elif self.behavior == 2:     # close to player
			if self.is_play_in_same_floor(floor_list, player):
				if self.rect.centerx < player_x:
					if not self.is_out_of_range(move_step,floor):
						self.surf = pygame.transform.scale(self.image_R, (80, 90)) 
						self.rect.move_ip(move_step, 0)
				else:
					if not self.is_out_of_range(-move_step,floor):
						self.surf = pygame.transform.scale(self.image_L, (80, 90)) 
						self.rect.move_ip(-move_step, 0)
			else:
				self.behavior1(move_step,floor)
		elif self.behavior == 3:   # jump 
			if self.jump_time == 0:
				self.jump_time = 300
			else:				
				self.jump(180*2, jump_step)
				self.jump_time -= 1

			floor1 = floor_list[0]
			self.behavior1(move_step,floor1)

		elif self.behavior == 4:  # jump and close to player
			if self.jump_time == 0:
				self.jump_time = 300
			else:				
				self.jump(180*2, jump_step)
				self.jump_time -= 1

			floor1 = floor_list[0]
			if self.is_play_in_same_floor(floor_list, player):
				if self.rect.centerx < player_x:
					if not self.is_out_of_range(move_step,floor1):
						self.surf = pygame.transform.scale(self.image_R, (80, 90)) 
						self.rect.move_ip(move_step, 0)
				else:
					if not self.is_out_of_range(-move_step,floor1):
						self.surf = pygame.transform.scale(self.image_L, (80, 90)) 
						self.rect.move_ip(-move_step, 0)
			else:
				self.behavior1(move_step,floor1)
				

	def get_surf(self):
		return self.surf

	def get_rect(self):
		return self.rect
