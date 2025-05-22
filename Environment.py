from Creature import *

class Environment:
    def __init__(self,screen):
        self.width, self.height = 400, 400
        self.agents=[Creature(),Creature()]

    def step(self):
        for agent in self.agents:
            agent.move()

    def drawEnvironment(self,screen):
        pygame.draw.rect(screen, "green",(25,25,800,800))
        for agent in self.agents:
            agent.draw(screen)