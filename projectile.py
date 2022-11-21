from obj import *
import pygame
import variables

class Projectile(Obj):

    def __init__(self, pos, vel, damage, radius=10) -> None:
        super().__init__(pos)

        self.vel = vel
        self.damage = damage
        self.radius = radius

    def update(self, keys, dt, playerPos):
        self.pos += dt * self.vel

        if self.pos.x < playerPos.x - variables.WIDTH // 2 or self.pos.x > playerPos.x + variables.WIDTH // 2:
            return True

        if self.pos.y < playerPos.y - variables.HEIGHT // 2 or self.pos.y > playerPos.y + variables.HEIGHT // 2:
            return True

        return False

    def display(self, screen, playerPos):
        pygame.draw.circle(screen, (255, 0, 0), (self.pos.x - playerPos.x + variables.WIDTH // 2, self.pos.y - playerPos.y + variables.HEIGHT//2), self.radius)
