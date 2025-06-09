import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # New clock object for FPS limiting
    
    # 1. Create our groups
    updatables = pygame.sprite.Group()
    drawables  = pygame.sprite.Group()
    
    # 2. Tell Player to auto-add itself to both groups
    Player.containers = (updatables, drawables)

    # 3. Instantiate after setting containers
    Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # 4. Update everything in one call
        updatables.update(dt)

        screen.fill((0, 0, 0))
       
         # 5. Draw each sprite
        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()
        
if __name__ == "__main__":
    main()

