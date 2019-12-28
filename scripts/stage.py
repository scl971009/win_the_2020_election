import sys
import os
import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.enemy import Enemy
from scripts.material import Material

def set_life(num):
	# life = pygame.image.load("img\\stage\\" + str(num) + ".png")
	life = pygame.image.load(os.path.join("img", "stage", str(num) + ".png"))

	life = pygame.transform.scale(life, (60, 70))
	return life

def action(character, level, window_surface, player, background, material_amount, floor_list, enemy_group):
	material_num = 0
	material = Material(character, level, material_num)
	while True:
		life = set_life(player.get_life())
		window_surface.blit(background, (0, 0))
		window_surface.blit(life, (450, 545))
		window_surface.blit(player.get_surf(), player.get_rect())
		window_surface.blit(material.get_surf(), material.get_rect())
		for enemy in enemy_group:
			window_surface.blit(enemy.get_surf(), enemy.get_rect())

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					print(player.get_rect().x, player.get_rect().y)
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					print(event.pos)
					
					if player.get_rect().collidepoint(event.pos):
						player.life = player.life - 1
					if material.get_rect().collidepoint(event.pos):
						material_num = material_num + 1
						if material_num == material_amount:
							return True
						material = Material(character, level, material_num)
			
		pressed_keys = pygame.key.get_pressed()
		player.move_left_right(pressed_keys)
		
		for enemy in enemy_group:
			enemy.update(floor_list, player)

		player.update(floor_list, enemy_group)

		if pygame.sprite.collide_rect(player, material):
			material_num = material_num + 1
			if material_num == material_amount:
				return True
			material = Material(character, level, material_num)

		if player.get_life() == 0:
			return False

def stage00(window_surface, background, material_amount, player):
	"""stage 1 for korea fish"""
	player.stage_start()

	floor = pygame.Rect(0, 555, 800, 45)
	block1 = pygame.Rect(95, 140, 130, 20)
	block2 = pygame.Rect(570, 140, 135, 20)
	block3 = pygame.Rect(195, 270, 390, 20)
	block4 = pygame.Rect(150, 405, 500, 25)
	floor_list = []
	floor_list.append(floor)
	floor_list.append(block1)
	floor_list.append(block2)
	floor_list.append(block3)
	floor_list.append(block4)

	enemy0 = Enemy(0, 0, 0)
	enemy1 = Enemy(0, 0, 1)
	enemy_group = pygame.sprite.Group()
	enemy_group.add(enemy0)
	enemy_group.add(enemy1)

	return action(0, 0, window_surface, player, background, material_amount, floor_list, enemy_group)

def stage01(window_surface, background, material_amount, player):
	"""stage 2 for korea fish"""
	player.stage_start()
	
	floor = pygame.Rect(0, 555, 800, 45)
	block1 = pygame.Rect(115, 120, 85, 30)
	block2 = pygame.Rect(520, 125, 60, 25)
	block3 = pygame.Rect(310, 260, 400, 30)
	block4 = pygame.Rect(120, 390, 160, 30)
	floor_list = []
	floor_list.append(floor)
	floor_list.append(block1)
	floor_list.append(block2)
	floor_list.append(block3)
	floor_list.append(block4)
	
	enemy0 = Enemy(0, 1, 0)
	enemy1 = Enemy(0, 1, 1)
	enemy2 = Enemy(0, 1, 2)
	enemy_group = pygame.sprite.Group()
	enemy_group.add(enemy0)
	enemy_group.add(enemy1)
	enemy_group.add(enemy2)
	
	return action(0, 1, window_surface, player, background, material_amount, floor_list, enemy_group)

def stage02(window_surface, background, material_amount, player):
	"""stage 3 for korea fish"""
	player.stage_start()
	
	floor = pygame.Rect(0, 0, 0, 0)
	block1 = pygame.Rect(0, 0, 0, 0)
	block2 = pygame.Rect(0, 0, 0, 0)
	block3 = pygame.Rect(0, 0, 0, 0)
	block4 = pygame.Rect(0, 0, 0, 0)
	block5 = pygame.Rect(0, 0, 0, 0)
	floor_list = []
	floor_list.append(floor)
	floor_list.append(block1)
	floor_list.append(block2)
	floor_list.append(block3)
	floor_list.append(block4)
	floor_list.append(block5)
	
	enemy0 = Enemy(0, 2, 0)
	enemy1 = Enemy(0, 2, 1)
	enemy2 = Enemy(0, 2, 2)
	enemy3 = Enemy(0, 2, 3)
	enemy4 = Enemy(0, 2, 4)
	enemy_group = pygame.sprite.Group()
	enemy_group.add(enemy0)
	enemy_group.add(enemy1)
	enemy_group.add(enemy2)
	enemy_group.add(enemy3)
	enemy_group.add(enemy4)
	
	return action(0, 2, window_surface, player, background, material_amount, floor_list, enemy_group)

def stage03(window_surface, background, material_amount, player):
	"""stage 4 for korea fish"""
	player.stage_start()
	
	floor = pygame.Rect(0, 0, 0, 0)
	block1 = pygame.Rect(0, 0, 0, 0)
	block2 = pygame.Rect(0, 0, 0, 0)
	block3 = pygame.Rect(0, 0, 0, 0)
	block4 = pygame.Rect(0, 0, 0, 0)
	floor_list = []
	floor_list.append(floor)
	floor_list.append(block1)
	floor_list.append(block2)
	floor_list.append(block3)
	floor_list.append(block4)
	
	enemy0 = Enemy(0, 3, 0)
	enemy1 = Enemy(0, 3, 1)
	enemy2 = Enemy(0, 3, 2)
	enemy_group = pygame.sprite.Group()
	enemy_group.add(enemy0)
	enemy_group.add(enemy1)
	enemy_group.add(enemy2)
	
	return action(0, 3, window_surface, player, background, material_amount, floor_list, enemy_group)

def stage04(window_surface, background, material_amount, player):
	"""stage 5 for korea fish"""
	player.stage_start()
	
	floor = pygame.Rect(0, 0, 0, 0)
	block1 = pygame.Rect(0, 0, 0, 0)
	block2 = pygame.Rect(0, 0, 0, 0)
	block3 = pygame.Rect(0, 0, 0, 0)
	block4 = pygame.Rect(0, 0, 0, 0)
	block5 = pygame.Rect(0, 0, 0, 0)
	floor_list = []
	floor_list.append(floor)
	floor_list.append(block1)
	floor_list.append(block2)
	floor_list.append(block3)
	floor_list.append(block4)
	floor_list.append(block5)
	
	enemy0 = Enemy(0, 4, 0)
	enemy1 = Enemy(0, 4, 1)
	enemy2 = Enemy(0, 4, 2)
	enemy3 = Enemy(0, 4, 3)
	enemy_group = pygame.sprite.Group()
	enemy_group.add(enemy0)
	enemy_group.add(enemy1)
	enemy_group.add(enemy2)
	enemy_group.add(enemy3)
	
	return action(0, 4, window_surface, player, background, material_amount, floor_list, enemy_group)
		
def start(window_surface, character, level, player):
	"""
	Determine which stage to run.

	arg:
		window_surface: the window_surface to draw scene
		character: whose stage to generate
		level: which level of this character's game
	"""
	#path = "img\\material\\material_location\\stage" + str(level + 1) + "_mateial_location.png"
	# path = "img\\stage\\stage" + str(character) + str(level) + "_all.png"
	path = os.path.join("img", "stage", "stage" + str(character) + str(level) + "_all.png")
	background = pygame.image.load(path)
	background = pygame.transform.scale(background, (800, 600))
	background.convert()

	if character == 0:
		if level == 0:
			result = stage00(window_surface, background, 5, player)
		elif level == 1:
			result = stage01(window_surface, background, 4, player)
		elif level == 2:
			result = stage03(window_surface, background, 4, player)
		elif level == 3:
			result = stage04(window_surface, background, 5, player)
		elif level == 4:
			result = stage05(window_surface, background, 7, player)
	return result

class Stage():
	def __init__(self, window_surface, character, level):
		"""
		'Stage' is the object of the action game. Simply call 'run()' to generate the whole stage.

		arg:
			window_surface: the window_surface to draw scene
			character: whose stage to generate
			level: which level of this character's game
		"""
		self.window_surface = window_surface
		self.character = character
		self.level = level
		self.success = False

	def run(self, player):
		"""Run the 'Stage' object"""
		self.success = start(self.window_surface, self.character, self.level, player)

	def get_result(self):
		"""
		Return the result of this stage

		return value:
			True for success
			False for fail
		"""
		return self.success