import pygame

class Box:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value

    def draw(self,SCREEN,COLOUR,size):
        pygame.draw.rect(SCREEN,COLOUR,(self.x,self.y,size,size), 1)
        font = pygame.font.SysFont("arial",100)
        text = font.render(str(self.value), True, (0,0,0))
        SCREEN.blit(text,(self.x+25,self.y-10))