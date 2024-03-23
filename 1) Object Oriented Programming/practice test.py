import pygame
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Pygame with Classes')

x=50
y=100
speed=1

red=(255,0,0)
black=(0,0,0)
while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
            
        pygame.draw.circle(screen,red,(x,y),25,0)
    x=x+speed
    if x>500 or x<25:
        speed=-speed
        
    pygame.display.update()
            
