import pygame
import os
from ground import Ground
from player import Player


pygame.init()

S_WIDTH = 1350
S_HEIGHT = 700
CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

all_sprites = pygame.sprite.Group()
player = Player((S_WIDTH, S_HEIGHT), (S_WIDTH//2 - 25, S_HEIGHT//2 - 25))
all_sprites.add(player)

ground = Ground(os.path.join("assets", "ground.png"), (S_WIDTH, S_HEIGHT))
all_sprites.add(ground)
        

def draw():
    screen.fill((0, 0, 0))

    all_sprites.draw(screen)
    pygame.display.update()

def held_key_movement():
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        player.move(0)
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        player.move(2)
    
    if player.canJump == False:
        if pressed_keys[pygame.K_SPACE]:    
            player.canJump = True


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
    
        all_sprites.update()

        held_key_movement()
        draw()

        CLOCK.tick(60)

if __name__ == "__main__":
    main()
