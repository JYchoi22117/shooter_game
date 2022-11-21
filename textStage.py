from stage import *
from textComponent import *
import variables
import pygame

class TextStage(Stage):
    """Any stage only with text"""

    def __init__(self, text_components=[]):
        super().__init__()
        self.text_components = text_components
        self.buttons = [i for i in self.text_components if i.button]
        self.selected = None

        self.input_cooldown = 3

    def update(self, keys, dt):
        if len(self.buttons) != 0 and self.input_cooldown == 0:
            if keys[pygame.K_DOWN]:
                if self.selected == None:
                    self.selected = 0
                    self.buttons[0].active = True
                else:
                    self.buttons[self.selected].active = False
                    self.selected += 1
                    self.selected %= len(self.buttons)
                    self.buttons[self.selected].active = True

                self.input_cooldown = 3

            if keys[pygame.K_UP]:
                if self.selected == None:
                    self.selected = 0
                    self.buttons[0].active = True
                else:
                    self.buttons[self.selected].active = False
                    self.selected -= 1
                    self.selected %= len(self.buttons)
                    self.buttons[self.selected].active = True

                self.input_cooldown = 3

            if keys[pygame.K_RETURN]:
                if self.selected != None:
                    return [self.buttons[self.selected].effect, None]

        self.input_cooldown = max(self.input_cooldown - 1, 0)
        return ["", None]
    
    def display(self, screen):
        screen.fill(variables.BLACK)
        for text_component in self.text_components:
            text_component.display(screen)

    def init(self, meta_data):

        pass