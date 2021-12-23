import pygame
import time
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from pygame.constants import QUIT

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        
pygame.init()

player = Player()
player.rect.x = 0
player.rect.y = 0

screen = pygame.display.set_mode((1350, 700))

pygame.display.set_caption("VJ's Game")
running = True

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

centerX, centerY = player.rect.center

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    screen.blit(player.surf, (100,100))
    centerX, centerY = player.rect.center

    pygame.display.flip()