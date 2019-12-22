import sys
import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.enemy import Enemy
from scripts.material import Material


def stage00(window_surface, background):
	"""stage 1 for korea fish"""
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

	player = Player(0, 190, 465)
	enemy0 = Enemy(0, 0, 0)
	enemy1 = Enemy(0, 0, 1)
	enemy_group = pygame.sprite.Group()
	enemy_group.add(enemy0)
	enemy_group.add(enemy1)
	material_num = 0
	material = Material(0, 0, material_num)
	window_surface.blit(player.get_surf(), player.get_rect())
	window_surface.blit(material.get_surf(), material.get_rect())

	pygame.display.update()

	while True:
		window_surface.blit(background, (0, 0))
		window_surface.blit(player.get_surf(), player.get_rect())
		window_surface.blit(material.get_surf(), material.get_rect())

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					print(player.get_player_rect().x, player.get_player_rect().y)
				elif event.key == K_UP:
					player.jump()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					print(event.pos)
		pressed_keys = pygame.key.get_pressed()
		player.move_left_right(pressed_keys)
		player.gravity(floor_list)
		enemy0.update(floor_list, player.get_rect())
		enemy1.update(floor_list, player.get_rect())

def start(window_surface, character, level):
	"""
	Determine which stage to run.

	arg:
		window_surface: the window_surface to draw scene
		character: whose stage to generate
		level: which level of this character's game
	"""
	#path = "img\\material\\material_location\\stage1_mateial_location.png"
	path = "img\\stage\\stage" + str(character) + str(level) + "_all.png"
	background = pygame.image.load(path)
	background = pygame.transform.scale(background, (800, 600))
	background.convert()

	window_surface.blit(background, (0, 0))

	if character == 0:
		if level == 0:
			stage00(window_surface, background)

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

	def run(self):
		"""Run the 'Stage' object"""
		self.success = start(self.window_surface, self.character, self.level)

	def get_result(self):
		"""
		Return the result of this stage

		return value:
			True for success
			False for fail
		"""
		return self.success