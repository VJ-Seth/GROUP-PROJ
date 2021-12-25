import pygame

from colors import RED


class Ground(pygame.sprite.Sprite):
    
    def __init__(self, image_path, position):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = position

        self.image.fill(RED)

