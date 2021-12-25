import pygame
import random

from colors import WHITE

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_dimensions, spawn_point):
        super().__init__()

        # Could be replaced with image drawing
        self.width, self.height = (50, 50)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()
        self.ground_collide = False
    
        self.screen_width, self.screen_height = screen_dimensions
        self.move_offset = 10

        self.isJump = False
        self.jumpCount = 10

        self.spawn_point = spawn_point

        if not spawn_point:
            self.rect.x, self.rect.y = (0, 0)
        else:
            self.rect.x, self.rect.y = spawn_point[0], (spawn_point[1] - self.rect.height)


    def check_boundary(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if (self.rect.x + self.width) > self.screen_width:
            self.rect.x = (self.screen_width - self.width)
        if self.rect.y < 0:
            self.rect.y = 0

    def update(self):
        self.check_boundary()

        # no gravity if we are hitting the ground
        if not self.ground_collide and self.isJump:
            self.rect.y += 3.2
        
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

