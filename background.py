from obj import *
from vec import *
import pygame
import variables

def get_color(x, y):
    if (x + y)%2 == 0:
        return (38, 120, 25)
    else:
        return (132, 168, 52)

class Background(Obj):

    def __init__(self):
        super().__init__(Vec(0, 0))

        self.pos = Vec(0, 0)

        self.width = variables.WIDTH * 1/2
        self.height = variables.HEIGHT * 1/2

        self.tile_size = 200

        self.tile_length = Vec(4, 3)

    def update(self, keys, dt):
        pass

    def display(self, screen, playerPos):

        # pygame.draw.rect(screen, (38, 120, 25), [self.pos.x - playerPos.x + variables.WIDTH // 2 -0.5 * self.width, self.pos.y - playerPos.y + variables.HEIGHT // 2 - 0.5*self.height, self.width, self.height])
        center = Vec((playerPos.x / self.tile_size + 1/2) // 1, (playerPos.y / self.tile_size + 0.5) // 1)

        # pygame.draw.rect(screen, get_color(center.x, center.y), [center.x * self.tile_size - playerPos.x + variables.WIDTH // 2 - 0.5 * self.tile_size , center.y * self.tile_size - playerPos.y + variables.HEIGHT // 2 - 0.5*self.tile_size, self.tile_size, self.tile_size])

        for i in range(-self.tile_length.x, self.tile_length.x):
            for j in range(-self.tile_length.y, self.tile_length.y):

                pygame.draw.rect(screen, get_color(center.x + i, center.y + j), [(center.x + i) * self.tile_size - playerPos.x + variables.WIDTH // 2 - 0.5 * self.tile_size , (center.y + j) * self.tile_size - playerPos.y + variables.HEIGHT // 2 - 0.5*self.tile_size, self.tile_size, self.tile_size])
