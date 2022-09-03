import pygame

class Backround:
    back = pygame.image.load('dinoBackround.png')
    xVelo = 0
    x = 0
    width = 0
    screen = pygame.Surface

    def __init__(self, screen, x):
        self.screen = screen
        self.xVelo = -4
        self.x = x
        self.width = pygame.Surface.get_width(screen)
        self.back = pygame.transform.scale(self.back,
                                           (self.width, pygame.Surface.get_height(screen)))

    def update(self):
        self.x += self.xVelo

    def draw(self, screen):
        screen.blit(self.back, (self.x, 0))
        if self.x < 0:
            newBack = Backround(screen, self.x + self.width)
            newBack.draw(screen)
