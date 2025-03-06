# settings.py (Game settings)
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -10
PLAYER_SPEED = 5

# player.py (Handles player logic)
import pygame
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 500, 40, 40)
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False
        
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        
        self.check_collision(platforms)

    def check_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True
                return
        self.on_ground = False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
