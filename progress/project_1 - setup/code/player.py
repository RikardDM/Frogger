import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

    
    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            elif self.event.key == pygame.K_RIGHT:
                print("right")
            elif self.event.key == pygame.K_UP:
                print("up")
            elif self.event.key == pygame.K_DOWN:
                print("down")
            



 