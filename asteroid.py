from constants import *
from circleshape import CircleShape
import pygame # type: ignore

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, COLORS["WHT"], self.position, ASTEROID_LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)