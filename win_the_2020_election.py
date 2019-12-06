import sys
import pygame
from pygame.locals import QUIT

def main():
	pygame.init()
	window_surface = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('2020爭霸戰')

	background = pygame.image.load("img\\main\\start.png")
	background = pygame.transform.scale(background, (800, 600))
	background.convert()
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
					#print(event.pos)
					if start.collidepoint(event.pos):
						print("start pressed!")
					elif setting.collidepoint(event.pos):
						print("setting pressed!")
					elif instruction.collidepoint(event.pos):
						print("instruction pressed!")

if __name__ == '__main__':
	main()