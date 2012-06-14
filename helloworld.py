#this is the first example of the python game library tutorial.
import sys, pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')
while True: # main event loop
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update() 
