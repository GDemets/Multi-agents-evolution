import pygame
import random


class Plant:
    def __init__(self):
        self.x=random.randint(25,800)
        self.y=random.randint(25,800)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", (self.x, self.y), 2)
