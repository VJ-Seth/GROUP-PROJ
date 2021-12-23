import pygame
import colors
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
from player import Player



pygame.init()

S_WIDTH = 1350
S_HEIGHT = 700
screen = pygame.display.set_mode((1350, 700))

player = Player()
player.rect.x = 0
player.rect.y = 0
        

def draw():
    screen.fill((0,0,0))
    screen.blit(player.surf, (100,100))


def main():
    pygame.display.set_caption("Fighting Game")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
        screen.blit(player.surf, (100,100))

        pygame.display.update()

if __name__ == "__main__":
    main()