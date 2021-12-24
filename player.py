import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, screen_dimensions, screen, starting_pos):
        super(Player, self).__init__()

        self.width, self.height = (50, 50)
        self.surf = pygame.Surface((self.width, self.height))
        self.screen = screen
        self.screen_width, self.screen_height = screen_dimensions

        self.move_offset = 10

        if not starting_pos:
            self.x, self.y = (0, 0)
        else:
            self.x, self.y = starting_pos


    def update(self):
        if self.x < 0:
            self.x = 0
        if (self.x + self.width) > self.screen_width:
            self.x = (self.screen_width - self.width)
        if self.y < 0:
            self.y = 0
        if (self.y + self.height) > self.screen_height:
            self.y = (self.screen_height - self.height)
        

    def draw(self):
        self.surf.fill((255,255,255))
        self.screen.blit(self.surf, (self.x, self.y))
        

    def move(self, move_index):
        """
            0 - left
            1 - up
            2 - right
            3 - down
        """

        if move_index == 0:
            self.x -= self.move_offset
        elif move_index == 1:
            self.y -= self.move_offset
        elif move_index == 2:
            self.x += self.move_offset
        elif move_index == 3:
            self.y += self.move_offset
        else:
            return -1