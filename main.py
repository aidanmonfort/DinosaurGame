import random

import pygame

from Dino import *
from Backround import *
from Blocks import *
from Obstacle import *

grav = -.2
level = 1
scr = 0
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
            obst.append(Obstacle(screen, level, i * pygame.Surface.get_width(screen)/1.5,
                         pygame.Surface.get_height(screen) * (5/6), 'rock.png'))
        else:
            obst.append(Obstacle(screen, level, (i * pygame.Surface.get_width(screen)/1.5),
                         pygame.Surface.get_height(screen) * (5/6), 'cactus.png'))

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
    end = font.render("You lost, Final Score was " + str(scr), True, (116, 42, 133), None)
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
    for i in range(len(obst))[::-1]:
        obst[i].update()
        if obst[i].x < -10:
            obst.remove(obst[i])
            scr += 1

    checkCollisions()
    screen.fill((0,0,0))
    back.draw(screen)
    dinosaur.draw(screen)
    screen.blit(score, scoreRect)
    score = font.render("Score: " + str(scr), True, (116, 42, 133), None)
    for i in range(len(obst)):
        obst[i].draw(screen)

    if len(obst) == 0:
        dinosaur.grav = grav
        spawnObstacles()


    pygame.display.flip()
    clock.tick(60)

while lost:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    drawLostScreen()
    pygame.display.flip()

