# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    passfail = pygame.init()
    print(f"Pygame Modules Initialized -- Pass:{passfail[0]} Fail:{passfail[1]}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(COLORS["BLK"])
        pygame.display.flip()
        # tick for 1/60th of a second, convert delta to seconds (ms->s)
        dt = (clock.tick(60)/1000)
        
if __name__ == "__main__":
    main()

