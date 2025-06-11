import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
    # 1. Kill this asteroid
        self.kill()

    # 2. If it was already the smallest size, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

    # 3. Compute split parameters
    # a random angle between 20° and 50°
        angle = random.uniform(20, 50)
    # two new velocity vectors, rotated off the original
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2
    # new, smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # 4. Spawn two new asteroids at this position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2
