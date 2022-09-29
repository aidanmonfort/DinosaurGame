import pygame

class Obstacle:
    x = 0
    xVel = 0
    y = 0
    img = pygame.Surface

    def __init__(self, screen, level, x, y, file):
        self.xVel = -2 + (level * -.5)
        self.x = x
        self.y = y
        self.img = pygame.image.load(file)
        self.img = pygame.transform.scale(self.img, ((pygame.Surface.get_width(screen) * .1),
                                               (pygame.Surface.get_height(screen) * .1)))

    def update(self):
        self.x += self.xVel

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def getCollisionRectangle(self):
        return pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.img) - 3,
                                                          pygame.Surface.get_height(self.img) - 10)

    def drawCollisionRectangle(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, pygame.Surface.get_width(self.img) - 3,
                                                         pygame.Surface.get_height(self.img) - 10), 2)
