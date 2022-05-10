import pygame
import random
import numpy as np
from box import Box
from grid import Grid

pygame.init()

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
#Window Size
SIZE = 400

screen = pygame.display.set_mode((SIZE,SIZE))

#Creating the boxes
boxes = []
for i in np.arange(0,SIZE,SIZE/4):
    for j in np.arange(0,SIZE,SIZE/4):
        box = Box(i,j,random.randint(1,4))
        boxes.append(box)
#Creating the Grid
grid = Grid(SIZE,2)


running = True
while running:
    
    screen.fill(WHITE)
    grid.draw(screen,BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for box in boxes:
        box.draw(screen,BLACK,SIZE)
    
    pygame.display.flip()
