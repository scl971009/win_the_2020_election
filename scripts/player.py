import sys

import pygame  
import os
from pygame.locals import *
initial_pos_list = [[(590, 465), (590, 465), (590, 465), (590, 465), (590, 465)]]
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
		self.image_R = pygame.image.load(os.path.join("img","main", 'KoreaFish_turnRight.png'))
		self.image_L = pygame.image.load(os.path.join("img","main", 'KoreaFish_turnLeft.png'))
		self.image_H = pygame.image.load(os.path.join("img","main", 'KoreaFish_hurt.png'))
		self.image_jumpR = pygame.image.load(os.path.join("img","main", 'KoreaFish_Right_jump.png'))
		self.image_jumpL = pygame.image.load(os.path.join("img","main", 'KoreaFish_left_jump.png'))
		self.image_invR = pygame.image.load(os.path.join("img","main", 'KoreaFish_R_strong.png'))
		self.image_invL = pygame.image.load(os.path.join("img","main", 'KoreaFish_L_strong.png'))
		self.image_invjumpR = pygame.image.load(os.path.join("img","main", 'KoreaFish_Rjump_strong.png'))
		self.image_invjumpL = pygame.image.load(os.path.join("img","main", 'KoreaFish_Ljump_strong.png'))
		self.image_normal = pygame.image.load(os.path.join("img","main", 'role_KoreaFish.png'))
		self.image_invnormal = pygame.image.load(os.path.join("img","main", 'KoreaFish_very_strong.png'))

		self.surf  = pygame.transform.scale(self.image_L, (60, 90))
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
		self.h=0
	def stage_start(self):
		self.rect = self.surf.get_rect(topleft = initial_pos_list[self.character][self.stage])
		self.h=0
	def stage_clear(self):
		self.surf  = pygame.transform.scale(self.image_L, (60, 90))
		self.stage = self.stage + 1
		self.life = 5
	def update(self,floor_list, enemy_group):
		if self.stand==True:
			self.h=0
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
					self.surf  = pygame.transform.scale(self.image_H, (60, 90))
			elif self.invincible>30:
					self.invincible+=(k-b)
					self.surf  = pygame.transform.scale(self.image_invnormal, (60, 90))
			elif self.invincible>0:
					self.invincible+=(k-b)
					self.surf  = pygame.transform.scale(self.image_normal, (60, 90))
				

				
				

	def move_left_right(self, pressed_keys):

		#todo: move when left, right is pressed (remember to set bounds)
		if pressed_keys[K_LEFT] and self.rect[0]>0  :
			self.rect.move_ip(-5, 0)
			self.surf  = pygame.transform.scale(self.image_L, (60, 90))
		if pressed_keys[K_RIGHT] and self.rect[0]<750  :	
			self.rect.move_ip(5, 0)
			self.surf  = pygame.transform.scale(self.image_R, (60, 90))
		if pressed_keys[K_UP] and self.h<=20:
			self.stand=False
			self.h+=1
			self.jump()
		if( (not pressed_keys[K_UP]) and self.stand==False)or self.h>20  :
			self.yspeed = -11.5
			self.grav()
		if pressed_keys[K_UP] and pressed_keys[K_RIGHT]:
			self.surf  = pygame.transform.scale(self.image_jumpR, (60, 90))
		if pressed_keys[K_UP] and pressed_keys[K_LEFT]:
			self.surf  = pygame.transform.scale(self.image_jumpL, (60, 90))



	def jump(self):

                #todo: jump when K_UP is pressed (should not just simply plus y position
		if self.h<15:
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
