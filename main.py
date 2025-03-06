# main.py (Entry point of the game)
import pygame
from settings import *
from player import Player
from platform import Platform
from background import Background

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixel Adventure")
    clock = pygame.time.Clock()
    running = True

    background = Background()
    player = Player()
    platforms = [Platform(100, 300, 200, 20), Platform(400, 400, 200, 20), Platform(250, 500, 300, 20)]

    while running:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(platforms)
        
        background.draw(screen)
        player.draw(screen)
        
        for platform in platforms:
            platform.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
