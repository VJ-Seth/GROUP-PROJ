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

ground = Ground(os.path.join("assets", "ground.png"), (S_WIDTH, S_HEIGHT))
all_sprites.add(ground)

player = Player((S_WIDTH, S_HEIGHT), (ground.rect.x, ground.rect.y))
all_sprites.add(player)
        

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
                if event.key == pygame.K_SPACE:
                    if player.isJump == False:  
                        player.isJump = True
                        
        # handle player jumping
        if player.isJump:
            if player.jumpCount >= -10:
                velocity = (player.jumpCount * abs(player.jumpCount)) * 0.5
                if player.rect.y - velocity >= ground.rect.y:
                    player.rect.y = ground.rect.y - player.rect.height
                    player.jumpCount = 10
                    player.isJump = False
                else:
                    player.rect.y -= velocity
                    player.jumpCount -= 1
            else: 
                player.jumpCount = 10
                player.isJump = False


        ground_collision = pygame.sprite.collide_rect(player, ground)
        player.ground_collide = ground_collision
        
    
        all_sprites.update()

        held_key_movement()
        draw()

        CLOCK.tick(60)

if __name__ == "__main__":
    main()
