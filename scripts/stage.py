import sys
import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.enemy import Enemy


def stage00(window_surface, background):
	"""stage 1 for korea fish"""
	floor = pygame.Rect(0, 560, 800, 40)
	block1 = pygame.Rect(95, 140, 130, 20)
	block2 = pygame.Rect(570, 140, 135, 20)
	block3 = pygame.Rect(195, 270, 390, 20)
	block4 = pygame.Rect(150, 405, 500, 25)
	player = Player(0, 190, 470)
	enemy0 = Enemy(0, 0, 0)
	enemy1 = Enemy(0, 0, 1)
	enemy_group = pygame.sprite.Group()
	enemy_group.add(enemy0)
	enemy_group.add(enemy1)
	window_surface.blit(player.surf, (190, 470))

	pygame.display.update()

	while True:
		window_surface.blit(background, (0, 0))
		window_surface.blit(player.get_player_surf(), player.get_player_rect())

		pygame.display.update()
		if not floor.top == player.get_player_rect().bottom:
			print('on floor')
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pressed_keys = pygame.key.get_pressed()
		player.update(pressed_keys)

def start(window_surface, character, level):
	"""
	Determine which stage to run.

	arg:
		window_surface: the window_surface to draw scene
		character: whose stage to generate
		level: which level of this character's game
	"""
	path = "img\\stage\\stage" + str(character) + str(level) + ".png"
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