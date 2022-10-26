import pygame 
from stage import *
from textStage import *
from textComponent import *

class IntroStage(TextStage):
    """Intro Screen"""

    def __init__(self):
        text_components = []
        text_components.append(TextComponent( "(Name of Game)", (640, 240), 60 ))
        text_components.append(TextComponent( "PLAY", (640, 360), 40, True, "menu" ))
        text_components.append(TextComponent( "SETTINGS", (640, 480), 40, True, "setting" ))

        super().__init__(text_components)
