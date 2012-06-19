# http://inventwithpython.com/pygame/chapter2.html

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode( (400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE=(255,255,255)
catImg = pygame.image.load('resources/cat.png')
catx = 10
caty = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx >= 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty >= 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx <= 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty <= 10:
            direction = 'right'
    
    DISPLAYSURF.blit(catImg, (catx, caty))
    old_direction = direction

    for event in pygame.event.get():
        print direction
        if event.type == KEYDOWN:
            direction = 'down'
        elif event.type == KEYUP:
            direction = old_direction
        
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)



