# platform.py (Defines platforms)
import pygame
from settings import *

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill(PLATFORM_COLOR)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# background.py (Handles background rendering)
import pygame
from settings import *

class Background:
    def __init__(self):
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(BACKGROUND_COLOR)
    
    def draw(self, screen):
        screen.blit(self.image, (0, 0))
