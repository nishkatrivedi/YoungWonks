import pygame
import random,time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Pygame with Classes')

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
white=(255,255,255)

disappear=False
count=-1
col=white
def show_text(msg,X,Y,col):
    fontobj=pygame.font.SysFont('comicsans',25)
    msgobj=fontobj.render(msg,False,col)
    screen.blit(msgobj,(X,Y))
    
'''class Circle:
    def __init__(self):
        self.radius=random.randint(1,100)
        self.x=random.randint(1,500)
        self.y=random.randint(1,500)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
circles=[]        

for i in range(0,10,1):
    circle=Circle()
    circles.append(circle)

circles=[Circle() for i in range(10)]

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
            
    for i in range(len(circles)):
       
        circles[i].draw()
        
    pygame.display.update()'''


'''position=[100,300,450]
colors=[red,green]
circles=[]

class Circle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.color=random.choice(colors)
        self.speed=random.randint(1,5)
        self.key=chr(random.randint(97,122))
        self.hidden=False
        self.right=True
        self.left=False
        
    def get_key(self):
        return self.key
    def key_matches(self,letter):
        
        return letter==self.key
    def draw(self):
        if self.hidden==False:
            pygame.draw.circle(screen,self.color,(self.x,self.y),25,0)
            show_text(self.key,self.x-10,self.y-10,col)
            
    def move(self):
        if self.hidden==False:
            ##time.sleep(1)
            if self.right==True and self.left==False:
                self.x=self.x+self.speed
               # print('moving right')
                if self.x>476:
                    self.right=False
                    self.left=True
            elif self.left==True and self.right==False:
                self.x=self.x-self.speed
                #print('moving left')
                if self.x<24:
                    self.right=True
                    self.left=False
    def hide(self):
        self.hidden=True
    def toggle_visibility(self):
        if self.hidden==False:
            self.hide()
        else:
            self.hidden=False'''
    
            

'''for i in range(30):
    circle=Circle()
    circles.append(circle)'''
'''c1=Circle(50,100)
circles.append(c1)
c2=Circle(100,100)
circles.append(c2)'''
'''
hidden=False

for y in range(50,251,100):
    for x in range(25,476,50):
        c=Circle(x,y)
        circles.append(c)


##circles=[Circle(25,50)]     
while True:
    screen.fill(black)
    
    
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
      
        if event.type==KEYDOWN:
            for i in range(len(circles)):
                #print(chr(event.key),'==',circles[i].key, chr(event.key)==circles[i].key)
            
                if circles[i].key_matches(chr(event.key)):
                    circles[i].toggle_visibility()
                
                    
                        
        
    for c in circles:
        c.move()
    
    for c in circles:
        c.draw()
    
        ##print('circle')
        
        
    pygame.display.update()'''
'''
total_laps=5
class Circle:
    def __init__(self,y):
        self.lap=1
        self.speed=random.randint(10,15)
        self.right=True
        self.x=25
        self.y=y
        self.trigger=False
        self.color=yellow
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),25,0)
        show_text(str(self.lap),self.x-25,self.y-25,black)
        
    def move(self):
        global finished
        if self.lap<=total_laps:
            if self.right==True:
                self.x=self.x+self.speed
            else:
                self.x=self.x-self.speed
                
            if self.x<25:
                    self.right=True
                    self.lap+=1
                    if self.lap>total_laps:
                        self.x=25
                        finished+=1
                        if finished==1:
                            self.color=red
                            print('1st',circles.index(self))
                        elif finished==2:
                            self.color=blue
                            print('2nd',circles.index(self))
                        elif finished==3:
                            self.color=green
                            print('3rd',circles.index(self))
                        
            if self.x>475:
                self.right=False

            
        
            
            
        
         
    
        
start=False
circles=[]
finished=0
for y in range(25,500,50):

    circle=Circle(y)
    circles.append(circle)


while True:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                print('space pressed')
                start=True
                    
    for circle in circles:
        circle.draw()
        if start==True:
            circle.move()
                    
        
    pygame.display.update()'''
    
'''circles[m].x+=1
        if circles[m].x>525:
            circles[m].x=-25'''        

'''circles=[]
class Circle:
    radius=20
    def __init__(self):
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.x=random.randint(0,500)
        self.y=random.randint(0,500)
        pass

    def expand(self):
        self.radius+=2
    def shrink(self):
        self.radius-=2
    def check_pos(self,pos):
        mx,my=pos
        cx=self.x
        cy=self.y
        return cx - self.radius < mx < cx + self.radius and cy - self.radius < my < cy + self.radius

for i in range(0,10,1):
    c=Circle()
    circles.append(c)

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()

        if event.type==KEYDOWN:
            if event.key==K_UP:
                Circle.radius+=2
                    
            elif event.key==K_DOWN:
                Circle.radius-=2
        if event.type==MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()==(True,False,False):
                for circle in circles:
                    if circle.check_pos(event.pos):
                       circle.expand()
            elif pygame.mouse.get_pressed()==(False,False,True):
                for circle in circles:
                    if circle.check_pos(event.pos):
                        circle.shrink()

    for i in range(0,10,1):
        pygame.draw.circle(screen,circles[i].color,(circles[i].x,circles[i].y,),circles[i].radius,0)
    pygame.display.update()'''



'''colors=[red,blue]
circles=[]

class Circle:
    radius=20
    def __init__(self):
        self.x=random.randint(self.radius,500-self.radius)
        self.y=random.randint(self.radius,500-self.radius)
        self.color=random.choice(colors)
        self.speedx=0
        self.speedy=0
        self.set_direction()
    def set_direction(self):
        if self.color==red:
            self.speedy=1
            self.speedx=0
        if self.color==blue:
            self.speedy=0
            self.speedx=1

    def movement(self):
        if self.speedy==1 and self.speedx==0:
            if y_up==True and y_down==False:
                self.y-=self.speedy
            if y_down==True and y_up==False:
                self.y+=self.speedy
        if self.speedx==1 and self.speedy==0:
            if x_right==True and x_left==False:
                self.x+=self.speedx
            if x_left==True and x_right==False:
                self.x-=self.speedx

    def check_click(self,position):
        mx,my=position
        if self.x-self.radius<=mx<=self.x+self.radius:
            if self.y - self.radius <= my <= self.y + self.radius:
                return True
        return False
    def toggle_color(self):
        if self.color==blue:
            self.color=red
        elif self.color==red:
            self.color=blue
        self.set_direction()
    def movement_2(self):
        self.y+=self.speedy
        self.x+=self.speedx
        self.boundary_check()
    def boundary_check(self):
        if self.x>=480:
            self.speedx=-1
        if self.x<=20:
            self.speedx=1
        if self.y>=480:
            self.speedy=-1
        if self.y<=20:
            self.speedy=1

    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)

for i in range(0,20,1):
    c=Circle()
    circles.append(c)


while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
        if event.type==MOUSEBUTTONDOWN:
            for circle in circles:
                if circle.check_click(event.pos):
                    circle.toggle_color()

    for i in circles:
        i.draw()
        i.movement_2()


    pygame.display.update()'''






























