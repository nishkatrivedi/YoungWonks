import pygame
import random,time
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Pygame with Classes')

def show_text(msg,X,Y,col):
    fontobj=pygame.font.SysFont('comicsans',25)
    msgobj=fontobj.render(msg,False,col)
    screen.blit(msgobj,(X,Y))

level=1
show='menu'
white=(255,255,255)
black=(0,0,0)
while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        if event.type==KEYDOWN:
            if event.key==K_m:
                show='menu'
            if event.key==K_s:
                if show=='menu':
                    show='screen1'
            if event.key==K_t:
                if show=='menu':
                    show='screen2'
            
    if show=='menu':
        show_text('Menu',250,250,white)
    elif show=='screen1':
        show_text('screen1',250,250,white)
    elif show=='screen2':
        show_text('screen2',250,250,white)
                  
    pygame.display.update()
