import sys
import pygame
from pygame.locals import *

from scripts.intelude import Intelude
from scripts.stage import Stage

def start(window_surface, background):
	"""
	main scene

	arg:
		background: background image after scaling and convert

	Return value:
		"start": start button pressed
		"setting": setting button pressed
		"instruction": instruction button pressed
	"""
	window_surface.blit(background, (0, 0))

	start = pygame.Rect(310, 385, 170, 100)
	setting = pygame.Rect(120, 385, 170, 100)
	instruction = pygame.Rect(500, 385, 170, 100)

	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if start.collidepoint(event.pos):
						return "start"
					elif setting.collidepoint(event.pos):
						print("don't press setting")
					elif instruction.collidepoint(event.pos):
						return "instruction"

def rule(window_surface):
	"""show instruction page"""
	background = pygame.image.load("img\\else\\rule_HowToPlay.png")
	background = pygame.transform.scale(background, (800, 600))
	background.convert()

	window_surface.blit(background, (0, 0))

	#back btn

	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

def choose_player(window_surface, background):
	"""
	choose character scene

	arg:
		background: background image after scaling and convert

	Return Value:
		0: korea fish is chosen
	"""
	window_surface.blit(background, (0, 0))
	
	korea_fish = pygame.Rect(320, 180, 180, 330)

	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if korea_fish.collidepoint(event.pos):
						return 0

def main():
	"""the main function"""
	pygame.init()
	window_surface = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('2020爭霸戰')

	background = pygame.image.load("img\\main\\start.png")
	background = pygame.transform.scale(background, (800, 600))
	background.convert()
	choose_char = pygame.image.load("img\\main\\choose_role.png")
	choose_char = pygame.transform.scale(choose_char, (800, 600))
	choose_char.convert()

	while True:

		button_main = start(window_surface, background)

		if button_main == "start":
			char = choose_player(window_surface, choose_char)
			for i in range(5):
				story = Intelude(window_surface, char, i, 0)
				story.run()
				stage = Stage(window_surface, char, i)
				stage.run()
				result = stage.get_result()
				if not result:
					#fail
					break
		elif button_main == "instruction":
			rule(window_surface)

if __name__ == '__main__':
	main()