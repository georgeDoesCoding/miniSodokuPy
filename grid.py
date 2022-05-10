import pygame

class Grid:
    def __init__(self,SIZE,TOTAL):
        self.SIZE = SIZE
        self.TOTAL = TOTAL
        self.ratio = int(SIZE/TOTAL)

    def draw(self,SCREEN,COLOUR):

        for i in range(self.ratio,self.SIZE,self.ratio):
            pygame.draw.line(SCREEN,COLOUR,(i,0),(i,self.SIZE),3)
            pygame.draw.line(SCREEN,COLOUR,(0,i),(self.SIZE,i),3)
        
        pygame.draw.line(SCREEN,COLOUR,(0,0),(0,self.SIZE),3)
        pygame.draw.line(SCREEN,COLOUR,(0,0),(self.SIZE,0),3)
        pygame.draw.line(SCREEN,COLOUR,(0,self.SIZE),(self.SIZE,self.SIZE),3)
        pygame.draw.line(SCREEN,COLOUR,(self.SIZE,0),(self.SIZE,self.SIZE),3)
        
            
        
        
        
        
