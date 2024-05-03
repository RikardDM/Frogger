import settings 
import pygame, sys

pygame.init()

scren = pygame.display.set_mode(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type() == pygame.QUIT:
            pygame.quit()
            sys.exit()


dt = clock.tick(60) / 1000

pygame.display.update()


