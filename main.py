# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player

CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

def main():
    print("Starting asteroids!")
    passfail = pygame.init()
    print(f"Pygame Modules Initialized -- Pass:{passfail[0]} Fail:{passfail[1]}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(CENTER_X, CENTER_Y)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(COLORS["BLK"])
        
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        # tick for 1/60th of a second, convert delta to seconds (ms->s)
        dt = (clock.tick(60)/1000)

if __name__ == "__main__":
    main()

