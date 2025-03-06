# player.py (Handles player logic)
import pygame
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 500, 40, 40)
        self.vel_y = 0
        self.on_ground = False
        self.image = pygame.Surface((40, 40))
        self.image.fill(PLAYER_COLOR)

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
        screen.blit(self.image, self.rect.topleft)
