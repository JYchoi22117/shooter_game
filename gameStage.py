from stage import *
from player import *
from background import *
from enemy import *
from clock import *

from vec import *

import random
import math

class GameStage(Stage):
    def __init__(self):
        super().__init__()
        self.player = Player(Vec(0, 0))
        self.background = Background()

        self.clocks = []

        self.projectiles = []
        self.enemies = []

        self.clocks.append(Clock(Vec(300, 0), 200))

    def update(self, keys, dt):
        self.player.collsion(self.enemies)
        creations = self.player.update(keys, dt)
        self.background.update(keys, dt)

        if creations != None:
            self.projectiles.append(creations)

        for projectile in self.projectiles:
            if projectile.update(keys, dt, self.player.pos):
                self.projectiles.remove(projectile)

        if random.random() < dt:
            R = random.random() * 300 + 600
            theta = random.random() * math.pi * 2

            self.enemies.append( Enemy(Vec(R * math.cos(theta) + self.player.pos.x, R * math.sin(theta) + self.player.pos.y)) )

        for enemy in self.enemies:
            enemy.collsion(self.projectiles)
            if enemy.update(keys, dt):
                self.enemies.remove(enemy)

        for clock in self.clocks:
            clock.update(keys, dt)

        return "", None

    def display(self, screen):
        screen.fill(variables.BLACK)
        self.background.display(screen, self.player.pos)
        self.player.display(screen)

        for projectile in self.projectiles:
            projectile.display(screen, self.player.pos)

        for enemy in self.enemies:
            enemy.display(screen, self.player.pos)

        for clock in self.clocks:
            clock.display(screen, self.player.pos)

    def init(self, meta_data):
        pass

