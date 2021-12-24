import pygame
import random

from colors import WHITE

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_dimensions, starting_pos):
        super().__init__()

        # Could be replaced with image drawing
        self.width, self.height = (50, 50)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)

        
        self.rect = self.image.get_rect()
    
        self.screen_width, self.screen_height = screen_dimensions
        self.move_offset = 10

        if not starting_pos:
            self.rect.x, self.rect.y = (0, 0)
        else:
            self.rect.x, self.rect.y = starting_pos


    def check_boundary(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if (self.rect.x + self.width) > self.screen_width:
            self.rect.x = (self.screen_width - self.width)
        if self.rect.y < 0:
            self.rect.y = 0
        if (self.rect.y + self.height) > self.screen_height:
            self.rect.y = (self.screen_height - self.height)

    def update(self):
        self.check_boundary()
        
    def move(self, move_index):
        """
            0 - left
            1 - up
            2 - right
            3 - down
        """

        if move_index == 0:
            self.rect.x -= self.move_offset
        # elif move_index == 1:
        #     self.rect.y -= self.move_offset
        elif move_index == 2:
            self.rect.x += self.move_offset
        # elif move_index == 3:
        #     self.rect.y += self.move_offset
        else:
            return -1

