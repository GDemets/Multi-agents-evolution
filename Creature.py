import random
import math
import pygame

class Creature:
    def __init__(self):
        self.x=random.randint(0,400)
        self.y=random.randint(0,400)
        self.life=100
        self.stamina=100
        self.targetX,self.targetY=self.x,self.y

    def move(self,plants):

        if abs(self.targetX-self.x)<1 and abs(self.targetY-self.y)<1 :
            newTarget=False
            while newTarget==False:
                self.targetX,self.targetY=random.randint(round(self.targetX-50),round(self.x+50)),random.randint(round(self.targetY-50),round(self.y+50))
                if 25 <= self.targetX <= 800 and 25 <= self.targetY <= 800:
                    newTarget=True

        for plant in plants:
            distance = math.sqrt((plant.x-self.x)**2 + (plant.y-self.y)**2)
            if distance<=15:
                self.targetX,self.targetY=plant.x,plant.y
            else:
                continue

        dx = self.targetX - self.x
        dy = self.targetY - self.y
        distance = math.sqrt(dx * dx + dy * dy)

        self.x += (dx / distance) * 1
        self.y += (dy / distance) * 1
        self.stamina-=0.1

    def draw(self,screen):
        pygame.draw.circle(screen, "red", (self.x,self.y), 5)
        pygame.draw.circle(screen, "blue", (self.targetX,self.targetY), 5)



