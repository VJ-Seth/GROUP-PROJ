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

        self.canJump = True
        self.startMass = 1
        self.startVelocity = 5
        self.mass = self.startMass
        self.velocity = self.startVelocity

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

    def jump(self):
        if self.canJump:
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
            F =(1 / 2) * self.mass * (self.velocity ** 2)
            
            # change in the y co-ordinate
            self.rect.y -= F
            
            # decreasing velocity while going up and become negative while coming down
            self.velocity -= 1
            
            # object reached its maximum height
            if self.velocity < 0:
                
                # negative sign is added to counter negative velocity
                self.mass = -1
    
            # objected reaches its original state
            if self.velocity == -6:
    
                # making is jump equal to false 
                self.canJump = False

                # setting original values to v and m
                self.velocity = 5
                self.mass = 1
        
        # creates time delay of 10ms
        pygame.time.delay(10)
   
        
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

