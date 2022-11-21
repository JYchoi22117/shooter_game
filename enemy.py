from obj import *
from vec import *
import variables
import pygame

class Enemy(Obj):

    def __init__(self, pos) -> None:
        super().__init__(pos)

        self.width = 40
        self.height = 100

        self.aim = Vec(0, 0)
        self.vel = 100

        self.hp = 100
        self.damage = 30

    def update(self, keys, dt):

        velocity = (self.aim - self.pos).normalized()*self.vel
        self.pos += dt * velocity

        if self.hp <= 0:
            return True

        return False

    def display(self, screen, playerPos):
        pygame.draw.rect(screen, (0, 0, 255), [self.pos.x - playerPos.x + variables.WIDTH // 2 - 0.5*self.width, self.pos.y - playerPos.y + variables.HEIGHT // 2 - 0.5*self.height, self.width, self.height])

        pygame.draw.rect(screen, (0, 255, 0), [self.pos.x - playerPos.x + variables.WIDTH // 2 - 0.5*self.width, self.pos.y - playerPos.y + variables.HEIGHT // 2 + 0.5*self.height + 10, self.width * self.hp / 100, self.height * 1 / 10])

        # A Little bit of update
        self.aim = playerPos

    def collsion(self, projectiles):

        for proj in projectiles:
            if ( self.pos.x - 0.5*self.width < proj.pos.x <self.pos.x + 0.5*self.width ) and ( self.pos.y - 0.5*self.height < proj.pos.y < self.pos.y + 0.5*self.height):
                self.hp -= proj.damage
                projectiles.remove(proj)

        return True

        
