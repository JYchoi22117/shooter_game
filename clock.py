from obj import *
import pygame
import variables
import math

class Clock(Obj):

    def __init__(self, pos, radius) -> None:
        super().__init__(pos)

        self.phase = 0
        self.radius = radius
        self.speed = 0.25

    def update(self, keys, dt):
        self.phase = (self.phase + self.speed * dt) % (2 * math.pi)

    def collision(self, player, enemies):
        playerRect = pygame.Rect(player.pos.x - player.width*0.5 , player.pos.y - player.width*0.5, player.width, player.height)    
        if playerRect.clipline(self.pos.x, self.pos.y,self.pos.x + self.radius * math.cos(self.phase), self.pos.y + self.radius * math.sin(self.phase)):
            player.hp = 0

        for enemy in enemies:
            enemyRect = pygame.Rect(enemy.pos.x - enemy.width*0.5 , enemy.pos.y - enemy.width*0.5, enemy.width, enemy.height)    
            if enemyRect.clipline(self.pos.x, self.pos.y,self.pos.x + self.radius * math.cos(self.phase), self.pos.y + self.radius * math.sin(self.phase)):
                enemy.hp = 0


    def display(self, screen, playerPos):
        pygame.draw.line(screen, (255, 255, 255), (self.pos.x - playerPos.x + variables.WIDTH // 2, self.pos.y - playerPos.y + variables.HEIGHT // 2), (self.pos.x - playerPos.x + variables.WIDTH // 2 + self.radius * math.cos(self.phase), self.pos.y - playerPos.y + variables.HEIGHT // 2 + self.radius * math.sin(self.phase)), width=5)
