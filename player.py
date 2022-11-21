from obj import *
from vec import *
from projectile import *
import pygame
import variables

class Player(Obj):

    def __init__(self, pos) -> None:
        super().__init__(pos)

        self.width = 40
        self.height = 100

        self.vel = 100
        self.bullet_vel = 1000

        self.bullet_cooldown = 5

        self.hp = 100

    def update(self, keys, dt):
        if keys[pygame.K_w]:
            self.pos -= Vec(0, 1) * self.vel * dt
        if keys[pygame.K_s]:
            self.pos += Vec(0, 1) * self.vel * dt
        if keys[pygame.K_d]:
            self.pos += Vec(1, 0) * self.vel * dt
        if keys[pygame.K_a]:
            self.pos -= Vec(1, 0) * self.vel * dt

        if keys[pygame.K_SPACE] and self.bullet_cooldown == 0:
            mouse_position = pygame.mouse.get_pos()
            mouse_position = Vec(mouse_position[0], mouse_position[1])

            rel_position = mouse_position - Vec(variables.WIDTH // 2, variables.HEIGHT // 2)
            self.bullet_cooldown = 5

            return Projectile(self.pos, rel_position.normalized() * self.bullet_vel, 50)

        self.bullet_cooldown = max(self.bullet_cooldown - 1, 0)

        if self.hp <= 0:
            pygame.quit()

        # pygame.mouse.get_pos()

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [variables.WIDTH // 2 - 0.5 * self.width, variables.HEIGHT // 2 - 0.5*self.height, self.width, self.height])
        pygame.draw.rect(screen, (0, 255, 0), [variables.WIDTH // 2 - 0.5*self.width, variables.HEIGHT // 2 + 0.5*self.height + 10, self.width * self.hp / 100, self.height * 1 / 10])


    def collsion(self, enemies):

        for enemy in enemies:
            if ( self.pos.x - 0.5*(self.width + enemy.width) < enemy.pos.x <self.pos.x + 0.5*(self.width + enemy.width) ) and ( self.pos.y - 0.5*(self.height + enemy.height) < enemy.pos.y < self.pos.y + 0.5*(self.height + enemy.height)):
                self.hp -= enemy.damage
                enemies.remove(enemy)

        return True

        

            