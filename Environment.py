from Creature import *
from Plant import *

class Environment:
    def __init__(self,screen):
        self.width, self.height = 400, 400
        self.agents=[Creature(),Creature()]
        self.plants=[]
        for i in range(25):
            self.plants.append(Plant())

    def step(self):
        for agent in self.agents:
            agent.move()

    def drawEnvironment(self,screen):
        pygame.draw.rect(screen, "green",(25,25,800,800))

        for agent in self.agents:
            agent.draw(screen)

        for plant in self.plants:
            plant.draw(screen)