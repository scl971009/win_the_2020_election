import sys

import pygame  
import os
from pygame.locals import *
initial_pos_list = [[(490, 465), (490, 465), (490, 465), (490, 465), (490, 465)]]
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
	def __init__(self, character):
		"""
		arg:
			character: player number (0 for korea fish)
			[x, y]: initial position
		"""
		#todo: change character image to the right character (current: black)
		super(Player, self).__init__()

		image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_turnLeft.png'))
		self.surf  = pygame.transform.scale(image, (60, 90))

		self.rect = self.surf.get_rect()

		#self.rect = self.surf.get_rect(topleft = (x, y))
		self.character = character
		self.life = 5
		self.stage = 0
		#maybe you will need force and speed as variable... (I'm not sure. It depends on how you implement jump and gravity.)
		#I think you might need to save initail position in case player is attacked by enemys
		self.rect.center = (60/ 2,  90/ 45)
		self.pos = vec(60/ 2,90/ 2)
		
		self.xspeed = 0                                 # 水平速度
		self.yspeed = 0                                 # 垂直速度
		self.aspeed = 0.5                               # 加速度
		self.stand=True
		self.attack=False
		self.last=pygame.time.get_ticks()
		self.invincible=0





		
			




	def stage_start(self):
		self.rect = self.surf.get_rect(topleft = initial_pos_list[self.character][self.stage])

	def stage_clear(self):
		self.stage = self.stage + 1
		self.life = 5



					
					
			
					                
                



	def update(self,floor_list, enemy_group):

		
		'''for ifloor in floor_list:

			diff_min = 100000

			if ifloor.left <= self.rect.center[0] and ifloor.right >= self.rect.center[0]:
				diff = ifloor.top - self.rect.bottom
				if diff >= 0 and diff_min > diff:
					diff_min = diff'''

		if len(floor_list)==5:
			if  pygame.Rect.colliderect(self.rect, floor_list[0]):
				a=(self.rect.bottom-floor_list[0].top)
				if 0<=self.rect.bottom-floor_list[0].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[1]):
				a=(self.rect.bottom-floor_list[1].top)
				if 0<=self.rect.bottom-floor_list[1].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[2]):
				a=(self.rect.bottom-floor_list[2].top)
				if 0<=self.rect.bottom-floor_list[2].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[3]):
				a=(self.rect.bottom-floor_list[3].top)
				if 0<=self.rect.bottom-floor_list[3].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[4]):
				a=(self.rect.bottom-floor_list[4].top)
				if 0<=self.rect.bottom-floor_list[4].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			else:
						self.yspeed = -11.5
						self.stand=False
		elif len(floor_list)==6:
			if  pygame.Rect.colliderect(self.rect, floor_list[0]):
				a=(self.rect.bottom-floor_list[0].top)
				if 0<=self.rect.bottom-floor_list[0].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[1]):
				a=(self.rect.bottom-floor_list[1].top)
				if 0<=self.rect.bottom-floor_list[1].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[2]):
				a=(self.rect.bottom-floor_list[2].top)
				if 0<=self.rect.bottom-floor_list[2].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[3]):
				a=(self.rect.bottom-floor_list[3].top)
				if 0<=self.rect.bottom-floor_list[3].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)
			elif  pygame.Rect.colliderect(self.rect, floor_list[4]):
				a=(self.rect.bottom-floor_list[4].top)
				if 0<=self.rect.bottom-floor_list[4].top<15:
						self.stand=True
						self.rect.move_ip(0,-a)

			elif  pygame.Rect.colliderect(self.rect, floor_list[5]):
				a=(self.rect.bottom-floor_list[5].top)
				if 0<=self.rect.bottom-floor_list[5].top<15:
						self.stand=True
			else:
						self.yspeed = -11.5
						self.stand=False


		for enemy in enemy_group:
			if 20>abs(self.rect.bottom-enemy.rect.top)>10 and pygame.Rect.colliderect(self.rect, enemy) :
					self.attack=True
					self.jump()
					self.invincible=30
			if pygame.Rect.colliderect(self.rect, enemy) and self.invincible<=0:
				if 0<=abs(self.rect.bottom-enemy.rect.bottom)<=20:				
					self.life -= 1
					self.invincible=200
			if self.invincible>0:
					self.coll()

	def coll (self):
			k= pygame.time.get_ticks()

			b= pygame.time.get_ticks()+1

			if self.invincible>150:
					self.invincible+=(k-b)
					image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_hurt.png'))
					self.surf  = pygame.transform.scale(image, (60, 90))
			elif self.invincible>30:
					self.invincible+=(k-b)
					image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_very_strong.png'))
					self.surf  = pygame.transform.scale(image, (60, 90))
			else :
					self.invincible+=(k-b)
					image = pygame.image.load(os.path.join("img", "main", 'role_KoreaFish.png'))
					self.surf  = pygame.transform.scale(image, (60, 90))
				

				
				

	def move_left_right(self, pressed_keys):
		""""""

		#todo: move when left, right is pressed (remember to set bounds)
		if pressed_keys[K_LEFT] and self.rect[0]>0  :
			self.rect.move_ip(-5, 0)
			image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_turnLeft.png'))
			self.surf  = pygame.transform.scale(image, (60, 90))
		if pressed_keys[K_RIGHT] and self.rect[0]<750  :	
			self.rect.move_ip(5, 0)
			image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_turnRight.png'))
			self.surf  = pygame.transform.scale(image, (60, 90))
		if pressed_keys[K_UP] :
			self.stand=False
			self.jump()	
		if (not pressed_keys[K_UP]) and self.stand==False  :
			self.yspeed = -11.5
			self.grav()
		if pressed_keys[K_UP] and pressed_keys[K_RIGHT]:
			image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_right_jump.png'))
			self.surf  = pygame.transform.scale(image, (60, 90))
		if pressed_keys[K_UP] and pressed_keys[K_LEFT]:
			image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_left_jump.png'))
			self.surf  = pygame.transform.scale(image, (60, 90))



	def jump(self):

                #todo: jump when K_UP is pressed (should not just simply plus y position)
		if self.attack==False:
			self.yspeed = -15
		else :
			self.yspeed =-150
			self.attack =False
		self.jumping()
	def jumping(self):
		self.rect.move_ip(self.xspeed,self.yspeed)        
		self.yspeed = self.yspeed + self.aspeed
	def grav(self):
		self.fall=True
		if self.rect[1]<465  :
			self.rect.move_ip(self.xspeed,-self.yspeed)        
			self.yspeed = -(self.yspeed + self.aspeed)



	
	def get_rect(self):
		return self.rect

	def get_surf(self):
		return self.surf

	def get_life(self):
		return self.life
