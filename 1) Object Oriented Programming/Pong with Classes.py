import pygame,random,time
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Pong with Classes')

def show_text(msg,X,Y,col):
    fontobj=pygame.font.SysFont('comicsans',25)
    msgobj=fontobj.render(msg,False,col)
    screen.blit(msgobj,(X,Y))


class Paddle:
    def __init__(self,x,color):
        self.x=x
        self.y=500/2-100
        self.color=color
        self.height=200
        self.width=20
        self.paddle_state='stop'
        self.score=0
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)
        show_text(str(self.score),self.x,10,'white')
    def movement(self):
        if self.paddle_state=='up':
            self.y-=3
        elif self.paddle_state=='down':
            self.y+=3

    def stop(self):
        self.paddle_state='stop'

    def increase_score(self):
        self.score+=1


class Circle:
    def __init__(self):
        self.color = 'white'
        self.radius=25
        self.reset()
        self.speedx=5
        self.speedy=3


    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y),self.radius, 0)

    def movement(self):
        if self.up==True:
            self.y-=self.speedy
        elif self.up==False:
            self.y+=self.speedy

        if self.right==True:
            self.x+=self.speedx
        elif self.right==False:
            self.x-=self.speedx

    def boundary_check(self):
        if self.y<=self.radius:
            self.up=False
        if self.y>=500-self.radius:
            self.up=True

        if self.x<=self.radius:
            self.reset()
            paddle_2.increase_score()


        if self.x >= 500 - self.radius:
            self.reset()
            paddle_1.increase_score()

    def collision_check(self):
        if self.x<=75 and paddle_1.y<self.y<paddle_1.y+200:
            self.right=True
        if self.x>=425 and paddle_2.y<self.y<paddle_2.y+200:
            self.right=False

    def reset(self):
        direction=[True,False]
        self.x = 250
        self.y = 250
        time.sleep(1)
        self.up = random.choice(direction)
        self.right = random.choice(direction)





paddle_1=Paddle(30,'red')
paddle_2=Paddle(450,'blue')
ball=Circle()

gameover=False


while True:
    screen.fill('black')
    if gameover==False:
        #movement logic
        paddle_1.movement()
        paddle_2.movement()
        ball.movement()
        ball.boundary_check()

        #draw logic
        paddle_1.draw()
        paddle_2.draw()
        ball.draw()

        #collision logic
        ball.collision_check()

        #scoring logic
        if paddle_1.score==10:
            winner=1
            gameover=True

        if paddle_2.score==10:
            winner=2
            gameover=True
    else:
        show_text(f'player {winner} wins', 150, 250, 'white')

    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        if event.type==KEYDOWN: #key event logic

            if event.key==K_w:
                paddle_1.paddle_state='up'
            if event.key==K_s:
                paddle_1.paddle_state = 'down'

            if event.key==K_UP:
                paddle_2.paddle_state='up'
            if event.key==K_DOWN:
                paddle_2.paddle_state='down'

        if event.type==KEYUP: #key event logic

            if event.key==K_w:
                paddle_1.stop()
            if event.key==K_s:
                paddle_1.stop()

            if event.key==K_UP:
                paddle_2.stop()
            if event.key==K_DOWN:
                paddle_2.stop()

    pygame.display.update()