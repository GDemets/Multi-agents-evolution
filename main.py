import pygame
from Environment import *

background_colour = (255,255,255)
(width, height) = (850, 850)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Multi-agents evolution')
screen.fill(background_colour)
pygame.display.flip()
running = True

env = Environment(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)
    env.step()
    env.drawEnvironment(screen)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()