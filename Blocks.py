import pygame
from Obstacle import Obstacle

class Cactus(Obstacle):
    cact = pygame.image.load('cactus.png')

    def __init__(self, screen, level, x, y):
        Obstacle.__init__(self, screen, level, x, y)
        self.cact = pygame.transform.scale(self.cact, ((pygame.Surface.get_width(screen) * .1),
                                               (pygame.Surface.get_height(screen) * .1)))

    def draw(self, screen):
        screen.blit(self.cact, (self.x, self.y))

    def getCollisionRectangle(self):
        return pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.cact) - 3,
                                                          pygame.Surface.get_height(self.cact) - 10)

    def drawCollisionRectangle(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.cact) - 3,
                                                         pygame.Surface.get_height(self.cact) - 10), 2)

class Rock(Obstacle):
    rock = pygame.image.load('rock.png')

    def __init__(self, screen, level, x, y):
        Obstacle.__init__(self, screen, level, x, y)
        self.rock = pygame.transform.scale(self.rock, ((pygame.Surface.get_width(screen) * .1),
                                                       (pygame.Surface.get_height(screen) * .1)))

    def draw(self, screen):
        screen.blit(self.rock, (self.x, self.y))

    def getCollisionRectangle(self):
        return pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.rock) - 3,
                                                          pygame.Surface.get_height(self.rock) - 10)

    def drawCollisionRectangle(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.rock) - 3,
                                                         pygame.Surface.get_height(self.rock) - 10), 2)