import random

import pygame

from Dino import *
from Backround import *
from Blocks import *

grav = -.2
level = 1
pygame.init()
pygame.display.set_caption("Dinosaur Game")
window = pygame.display.set_mode((550, 550))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
dinosaur = Dino(grav, screen)
back = Backround(screen, 0)
obst = []
running = True
lost = False
font = pygame.font.Font('High Speed.ttf', 25)
score = font.render("Score: " + str(level), True, (116, 42, 133), None)
scoreRect = score.get_rect()
scoreRect.center = (pygame.Surface.get_width(screen)/2, pygame.Surface.get_height(screen)/4)

def checkInput():
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        dinosaur.jump()

def spawnObstacles():
    global obst, level, screen, grav, dinosaur, score
    for i in range(1, 7):
        choice = random.randint(0, 2)
        if choice == 0:
            obst.append(Rock(screen, level, (i * pygame.Surface.get_width(screen)/1.5),
                         pygame.Surface.get_height(screen) * (5/6)))
        else:
            obst.append(Cactus(screen, level, (i * pygame.Surface.get_width(screen)/1.5),
                         pygame.Surface.get_height(screen) * (5/6)))

    level += 1
    grav += -.025

def checkCollisions():
    global obst, dinosaur, running, lost
    for Obstacle in obst:
        if pygame.Rect.colliderect(Obstacle.getCollisionRectangle(), dinosaur.getCollisionRect()):
            running = False
            lost = True

def drawLostScreen():
    global font, level
    screen.fill((0, 0, 0))
    end = font.render("You lost, Final Score was " + str(level-1), True, (116, 42, 133), None)
    endBox = end.get_rect()
    endBox.center = (pygame.Surface.get_width(screen)/2, pygame.Surface.get_height(screen)/2)
    endBack = Backround(screen, 0)
    endBack.draw(screen)
    screen.blit(end, endBox)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    checkInput()
    dinosaur.update(screen)
    back.update()
    for Obstacle in obst:
        Obstacle.update()
        if Obstacle.x < -10:
            obst.remove(Obstacle)

    checkCollisions()
    screen.fill((0,0,0))
    back.draw(screen)
    dinosaur.draw(screen)
    screen.blit(score, scoreRect)
    for Obstacle in obst:
        Obstacle.draw(screen)

    if len(obst) == 0:
        dinosaur.grav = grav
        score = font.render("Score: " + str(level), True, (116, 42, 133), None)
        spawnObstacles()

    pygame.display.flip()
    clock.tick(60)

while lost:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    drawLostScreen()
    pygame.display.flip()

