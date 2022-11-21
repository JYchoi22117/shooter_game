"""
main.py
"""
from curses import meta
import pygame
import variables
import stageManager
import introStage
import gameStage

### INITIALIZATION
pygame.init()
screen = pygame.display.set_mode([variables.WIDTH, variables.HEIGHT])
run = True
dt = 1 / 30

clock = pygame.time.Clock()

stage_manager = stageManager.StageManager()
stage_manager.append(introStage.IntroStage(), "intro")
stage_manager.append(gameStage.GameStage(), "game")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    effect, meta_data = stage_manager.active.update(keys, dt)
    stage_manager.active.display(screen)

    if effect != "":
        stage_manager.active = stage_manager.get_stage_by_name(effect)
        stage_manager.active.init(meta_data)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()

