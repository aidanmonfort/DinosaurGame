import pygame
from pygame.rect import Rect


class Dino:
    y = 0
    x = 90
    yVelo = 2
    grav = -4
    dinoImg = pygame.image.load('dino.png')
    jumping = False


    def __init__(self, grav, screen):
        self.x = pygame.Surface.get_width(screen) * (1/24)
        self.y = pygame.Surface.get_height(screen) * (5/6)
        self.yVelo = 0
        self.grav = grav
        self.jumping = False

    def update(self, screen):
        self.y -= self.yVelo
        self.yVelo += self.grav
        if self.y > pygame.Surface.get_height(screen) * (5/6):
            self.y = pygame.Surface.get_height(screen) * (5/6)
            self.yVelo = 0
            self.jumping = False

    def jump(self):
        if not self.jumping:
            self.yVelo += 7
            self.jumping = True

    def draw(self, screen):
        self.dinoImg = pygame.transform.scale(self.dinoImg, ((pygame.Surface.get_width(screen) * .1),
                                               (pygame.Surface.get_height(screen) * .1)))
        screen.blit(self.dinoImg, (self.x, self.y))

    def getCollisionRect(self):
        return pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.dinoImg) - 3,
                                         pygame.Surface.get_height(self.dinoImg) - 10)

    def drawCollisionRectangle(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.dinoImg) - 3,
                                                         pygame.Surface.get_height(self.dinoImg) - 10), 2)