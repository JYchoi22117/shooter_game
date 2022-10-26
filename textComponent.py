import pygame
import variables

class TextComponent:
    """TextComponent used in textStage.py"""    
    def __init__(self, content, position, size, button=False, effect="", active=False):
        self.content = content
        self.position = position
        self.size = size
        self.button = button
        self.active = active
        self.effect = effect

    def display(self, screen):
        if self.active:
            font = pygame.font.SysFont('ubuntu', self.size, bold=pygame.font.Font.bold)
        else:
            font = pygame.font.SysFont('ubuntu', self.size)

        text = font.render(self.content, True, variables.WHITE)
        text_rect = text.get_rect(center=self.position)

        screen.blit(text, text_rect)