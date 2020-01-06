import sys
import pygame  
import os
from pygame.locals import *
initial_pos_list = [[(190, 465), (190, 465), (190, 465), (190, 465), (190, 465)]]
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

		image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_turnRight.png'))
		self.surf  = pygame.transform.scale(image, (60, 90))

		self.rect = self.surf.get_rect()

		#self.rect = self.surf.get_rect(topleft = (x, y))
		self.character = character
		self.life = 5
		self.stage = 0
		#maybe you will need force and speed as variable... (I'm not sure. It depends on how you implement jump and gravity.)
		#I think you might need to save initail position in case player is attacked by enemys
		self.rect.center = (60/ 2,  90/ 2)
		self.pos = vec(60/ 2,90/ 2)
		
		self.xspeed = 0                                 # 水平速度
		self.yspeed = 0                                 # 垂直速度
		self.aspeed = 0.5                               # 加速度
		self.stand=True
		self.fall=False



		
			




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

		if  pygame.Rect.collidelistall(self.rect, floor_list):
					self.stand=True


		else:
					self.yspeed = -11.5
					self.stand=False

				

				

					




                     
		
		diff_min=100000
		for enemy in enemy_group:
			if pygame.Rect.colliderect(self.rect, enemy)and self.rect.centery > enemy.rect.centery:
				
					print('coll')
					self.life -= 1
					self.stage_start()
					self.coll()



					


			
		'''alpha=self.rect[0]-ifloor.left
			beta=self.rect[1]-ifloor.top
			print(alpha,beta)
			if pygame.Rect.colliderect(self.rect, ifloor) :

				self.stand=True
			else:

				self.stand==False'''
				
		'''for ifloor in floor_list:                 
			if pygame.Rect.colliderect(self.rect, ifloor) :

				self.stand=True
			else:

				self.stand==False  
			print(self.rect[0]-ifloor.left)'''
			
		'''
		for ifloor in floor_list:			

			if ifloor.left <= self.rect.left and ifloor.right >= self.rect.right:
                                
				diff = ifloor.top - self.rect.bottom
				diff2= ifloor.bottom - self.rect.top

				if diff >= 0  and diff_min > diff :
					self.stand=False

				else:
					self.stand=True'''






		"""
		This function will be called in the main loop. Simulate collision with floor and enemy and gravity.
		hint: How to deal with enemy_group: pygame.sprite.spritecollideany

		arg:
			floot_list: the list of all floor (rect) in this stage.
			enemy_group: all enemy's data
		"""

		"""換個方法寫self.acc = vec(0, PLAYER_GRAV )
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		if keys[pygame.K_RIGHT]:
			self.acc.x = PLAYER_ACC

        # 获得加速度
		self.acc.x += self.vel.x * PLAYER_FRICTION
        # 速度与加速度
		self.vel += self.acc
        # 如果速度小于0.1，则速度为0（比如这样设置，不然速度永远无法0）
		if abs(self.vel.x) < 0.1:
			self.vel.x = 0
		self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
		if self.pos.x > WIDTH:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = WIDTH
# 有初始的加速度 - 玩家没有在平台上就会掉落
		
		#floor part

		#if not colliding any floor:
			#move down (not constant velocity)

		#enemy part

		#if collides with enemy:
			#if attacks enemy:
				#simulate collision with enemy (maybe move up after collision)
			#else (attacked by enemy):
				#lose 1 life and sent back to the initial position
		pass"""
	def coll(self):
		image = pygame.image.load(os.path.join("img", "main", 'KoreaFish_hurt.png'))
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
		self.yspeed = -15
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
