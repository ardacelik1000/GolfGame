import math 
import sys 
import pygame 

class Ball:
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
        self.speed = 0 
        self.angle = 0 

    def update(self): 
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.x += self.speed * math.sin(math.radians(self.angle))
        
    def deneme(self):
        print(f'Speed is {self.speed}, Angle is {self.angle}')
