from settings import *
import pygame, sys
from player import Player

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups 

all_sprites = pygame.sprite.Group()


#sprites 
player = Player((600,400), all_sprites)

# game loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    # draw 
    all_sprites.draw(screen)

    #update 
    all_sprites.update()

   
    input(event)

    # delta time 
    dt = clock.tick(60) / 1000

    pygame.display.update()


