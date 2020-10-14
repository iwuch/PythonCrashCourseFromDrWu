import pygame
import random
# import time

pygame.init()
win_w = 1280
win_h = 720
win = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()

while True:
	clock.tick(60)
	win.fill((255,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()