import sys
import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.enemy import Enemy


def stage00(window_surface):
	floor = pygame.Rect(0, 560, 800, 40)
	block1 = pygame.Rect(95, 140, 130, 20)
	block2 = pygame.Rect(570, 140, 135, 20)
	block3 = pygame.Rect(195, 270, 390, 20)
	block4 = pygame.Rect(150, 405, 500, 25)
	player = Player(0)
	enemy0 = Enemy(0, 0, 0)
	enemy1 = Enemy(0, 0, 1)
	window_surface.blit(player.surf, (190, 470))

	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					print("space pressed")
				else:
					pressed_keys = pygame.key.get_pressed()
					player.update(pressed_keys)

def start(window_surface, character, level):
	path = "img\\stage\\stage" + str(character) + str(level) + ".png"
	background = pygame.image.load(path)
	background = pygame.transform.scale(background, (800, 600))
	background.convert()

	window_surface.blit(background, (0, 0))

	if character == 0:
		if level == 0:
			stage00(window_surface)

class Stage():
	def __init__(self, window_surface, character, level):
		""""""
		self.window_surface = window_surface
		self.character = character
		self.level = level
		self.success = False

	def run(self):
		self.success = start(self.window_surface, self.character, self.level)

	def get_result(self):
		return self.success