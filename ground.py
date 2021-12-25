import pygame
from colors import RED


class Ground(pygame.sprite.Sprite):
    
    def __init__(self, image_path, dimensions):
        super().__init__()

        self.screen_width, self.screen_height = dimensions

        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = (0, self.screen_height - self.rect.height)


