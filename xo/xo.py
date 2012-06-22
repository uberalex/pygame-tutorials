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

# start with O player
currentPlayer = 0 

def setPiece(number):
    global board # make sure we use the correct board!
    if(board[number-1] == None):
        board[number-1] = currentPlayer
        return True
    else:
        return False

#TODO: GOT HERE
#if a row sums to zero or three, then someone won
def addtriple(triple):
    try:
        return sum(triple) in (0,3)
    except TypeError:
        return False

def checkWin():
    global board #get the board
    
    return ( (True in [addtriple(board[i::3]) for i in range(0,3)]) or # columns are [colid::3]
    (True in [addtriple(board[i:i+3]) for i in range(0,9,3)]) or # rows are [start:start+2]
    #diagonals
    (True in [addtriple(board[::4])]) or
    (True in [addtriple(board[2:8:2])]) )


def endTurn():
    global currentPlayer # make sure we use the global variable
    if checkWin():
        print ('O','X')[currentPlayer], 'Wins!'
    else:
        currentPlayer = 1 if currentPlayer == 0 else 0

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

def drawNum(count, x, y):
    textSurfaceObj = fontObj.render(count, True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def drawPieces():
    for count in range(len(board)):
        y = 100 + ((count) % 3) * 100 
        x = 100 + ((count) / 3) * 100 
        piece = board[count]
        if piece == 1:
            drawX(x, y) 
        elif piece == 0:
            drawO(x, y)
        else:
            drawNum(str( count + 1 ), x, y)

def drawPrompt(player):
    if player == 1:
        textSurfaceObj = fontObj.render('X Player\'s Go', True, RED, WHITE)

    elif player == 0:
        textSurfaceObj = fontObj.render('O Player\'s Go', True, BLUE, WHITE)

    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 25)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

while True: # main game loop
        drawBox()
        drawPieces()
        drawPrompt(currentPlayer)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pressed = pygame.key.name(event.key)
                try:
                    #no board position 10 and can't pass
                    if pressed == '0':
                        raise ValueError
                    if setPiece( int(pressed) ):
                        endTurn() 
                except ValueError:
                    pass 
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
