from obj import *
import pygame
import variables
import math

class Clock(Obj):

    def __init__(self, pos, radius) -> None:
        super().__init__(pos)

        self.phase = 0
        self.radius = radius
        self.speed = 1    

    def update(self, keys, dt):
        self.phase = (self.phase + self.speed * dt) % (2 * math.pi)


    def display(self, screen, playerPos):
        pygame.draw.line(screen, (255, 255, 255), (self.pos.x - playerPos.x + variables.WIDTH // 2, self.pos.y - playerPos.y + variables.HEIGHT // 2), (self.pos.x - playerPos.x + variables.WIDTH // 2 + self.radius * math.cos(self.phase), self.pos.y - playerPos.y + variables.HEIGHT // 2 + self.radius * math.sin(self.phase)), width=5)
