import pygame,random
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Balloon Game')

def show_text(msg,X,Y,col):
    fontobj=pygame.font.SysFont('comicsans',25)
    msgobj=fontobj.render(msg,False,col)
    screen.blit(msgobj,(X,Y))



class Balloon():
    radius=25
    def __init__(self):
        self.letter=random.randint(97,122)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.x=random.randint(0,500)
        self.y=525

    def move(self):
        self.y-=3

    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)
        show_text(chr(self.letter),self.x-10,self.y-10,'white')
        show_text(str(score),10,10,'white')

b1=Balloon()
b2=Balloon()
balloons=[b1,b2]
score=0
gameover=False

while True:
    screen.fill('black')

    
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
            
        if event.type==KEYDOWN:
            
            for b in balloons:
                if chr(event.key)==chr(b.letter):
                    balloons.remove(b)
                    score+=1
 
            balloon=Balloon()
            balloons.append(balloon)



    if gameover==True:
        screen.fill('black')
        show_text('GAME OVER',150,250,'white')

    
        
         
                    
##if len(balloons)<1:
##        balloon=Balloon()
##        balloons.append(balloon)
            
##    if gameover==True:
##        screen.fill('black')
##        show_text('GAME OVER',100,250,'white')
                

    for balloon in balloons:
        balloon.draw()
        if gameover==False:
            balloon.move()

            if balloon.y<=25:
                gameover=True

            
    pygame.display.update()
