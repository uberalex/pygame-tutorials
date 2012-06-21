import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
RED = (178, 34, 34)
BLUE = (34, 34, 178)
BLACK = (34,34,34)

DISPLAYSURF = pygame.display.set_mode( (400, 400), 0, 32)
pygame.display.set_caption('X & O')

# game logic
board = [None] * 9

currentplayer = 0 

def setPiece(number):

    board[number-1] = currentplayer

# Rendering
fontObj = pygame.font.Font('freesansbold.ttf', 32)

def drawBox():
   DISPLAYSURF.fill(WHITE)
   pygame.draw.line(DISPLAYSURF, BLACK, (50,150), (350,150), 4)
   pygame.draw.line(DISPLAYSURF, BLACK, (50,250), (350,250), 4)
   pygame.draw.line(DISPLAYSURF, BLACK, (250,50), (250,350), 4)
   pygame.draw.line(DISPLAYSURF, BLACK, (150,50), (150,350), 4)

def drawX(x, y):
    pygame.draw.line(DISPLAYSURF, RED, (x, y), (x+25, y+25), 4)
    pygame.draw.line(DISPLAYSURF, RED, (x, y), (x+25, y-25), 4)
    pygame.draw.line(DISPLAYSURF, RED, (x, y), (x-25, y+25), 4)
    pygame.draw.line(DISPLAYSURF, RED, (x, y), (x-25, y-25), 4)
    
def drawO(x, y):
    pygame.draw.ellipse(DISPLAYSURF, BLUE, (x-25, y-25 ,50, 50), 4)

def drawPieces():
    for count in range(len(board)):
        x = 100 + ((count+1) % 3) * 100 
        y = 100 + ((count) / 3) * 100 
        piece = board[count]
        if piece == 1:
            drawX(x, y) 
        elif piece == 0:
            drawO(x, y)

def drawPrompt(player):
    if player == 1:
        textSurfaceObj = fontObj.render('X Player\'s Go', True, RED, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 25)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    elif player == 0:
        textSurfaceObj = fontObj.render('O Player\'s Go', True, BLUE, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 25)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

while True:

        drawBox()
        drawPieces()
        drawPrompt('o')
        for event in pygame.event.get():
            if event.type == :
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
