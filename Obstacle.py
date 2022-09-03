import pygame

class Obstacle:
    x = 0
    xVel = 0
    y = 0

    def __init__(self, screen, level, x, y):
        self.xVel = -2 + (level * -.5)
        self.x = x
        self.y = y

    def update(self):
        self.x += self.xVel

