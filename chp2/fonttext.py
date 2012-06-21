import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('fonts')

fpsClock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
#                               String          AA    Color  BG
textSurfaceObj = fontObj.render('Hello World! \n Extremely long text', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    textRectObj.bottom = (textRectObj.bottom + 5) % 300

    for event in pygame.event.get():
        print textRectObj.bottom
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(35) 
