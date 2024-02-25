import math 
import sys 
import pygame 

class Ball:
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
        self.xSpeed = 0
        self.ySpeed = 0
        self.angle = 0 
        self.radius = 15

    def update(self): 
        self.x += self.xSpeed * math.cos(math.radians(self.angle))
        self.y += self.ySpeed * math.sin(math.radians(self.angle))
 

    
