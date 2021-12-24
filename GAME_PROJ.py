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
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

player = Player((S_WIDTH, S_HEIGHT), screen, None)
        

def draw():
    screen.fill((0,0,0))
    player.draw()

def held_key_movement():
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        player.move(0)
    elif pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        player.move(1)
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        player.move(2)
    elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        player.move(3)


def main():
    pygame.display.set_caption("Fighting Game")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        held_key_movement()

        player.update()
        draw()

        pygame.display.update()

if __name__ == "__main__":
    main()