import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        # build a unit vector pointing “up” rotated by the player’s rotation,
        # then scale by shoot speed
        direction = pygame.Vector2(0, 1).rotate(rotation)
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        # a filled circle (no border width argument)
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius
        )

    def update(self, dt):
        # move straight in the direction we set
        self.position += self.velocity * dt
