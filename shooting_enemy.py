from enemy import *
import pygame

class ShootingEnemy(Enemy):

    def __init__(self, pos) -> None:
        super().__init__(pos)

    def update(self, keys, dt):

        velocity = (self.aim - self.pos).normalized()*self.vel
        self.pos += dt * velocity

        if self.hp <= 0:
            return True

        return False
