import pygame, sys, random, os, string
from pygame.locals import *

class Ball():
    def __init__(self,pos1,pos2,radius,width=0):
        self.pos1=pos1
        self.pos2=pos2
        self.radius=radius
        self.width=width
        self.pos = pos1,pos2

    def draw_circle(self):
        my_ball=pygame.draw.circle(screen,RED,(self.pos1,self.pos2),self.radius,self.width)

        return my_ball

    def move(self,x,y):
        self.x=x
        self.y=y
        self.pos2+=y
        self.pos1+=x
        pygame.display.update()
        screen.fill(BLACK)


class Bauncer():
    def __init__ (self,pos1,pos2,height,width,color,key1,key2):
        self.pos1=pos1
        self.pos2=pos2
        self.height=height
        self.width=width
        self.color=color
        self.pos=pos1,pos2
        self.key1=key1
        self.key2=key2

    def draw_rect(self):
        my_bouncer=pygame.draw.rect(screen,self.color,(self.pos1,self.pos2,self.height,self.width))

        return my_bouncer

    def move(self,):
        move_map = {self.key1: (-1, 0),
            self.key2: (1, 0)}
        if pygame.key.get_pressed():
            if self.pos1>=0 and self.pos1<=size[0]-self.height:
                if pygame.key.get_pressed()[self.key1]:
                    self.pos1+=move_map[self.key1][0]
                    self.pos2+=0
                if pygame.key.get_pressed()[self.key2]:
                    self.pos1+=move_map[self.key2][0]
                    self.pos2+=0
            elif self.pos1<0:
                if pygame.key.get_pressed()[self.key1]:
                    self.pos1==0
                    self.pos2+=0
                if pygame.key.get_pressed()[self.key2]:
                    self.pos1+=move_map[self.key2][0]
                    self.pos2+=0
            elif self.pos1>size[0]-self.height:
                if pygame.key.get_pressed()[self.key1]:
                    self.pos1+=move_map[self.key1][0]
                    self.pos2+=0
                if pygame.key.get_pressed()[self.key2]:
                    self.pos1==540
                    self.pos2+=0
            screen.fill(BLACK)



RED = (255,   0,   0)
YELLOW= (255, 255, 0)
BLACK = (0,0,0)
BLUE = (  0,   0, 255)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
os.environ['SDL_VIDEO_CENTERED']='-100'
size=(640,800)
screen = pygame.display.set_mode(size)
screen.fill(BLACK)

bouncer=Bauncer(0,770,100,20,YELLOW,K_LEFT,K_RIGHT)
bouncer2=Bauncer(0,10,100,20,BLUE,K_z,K_x)

ball=Ball(10,40,10,0)
ball.move(1,1)
pygame.display.set_caption('TENNIS GAME')
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
sound=pygame.mixer.Sound("ton.wav")
bnc1=pygame.mixer.Sound("bounce.wav")
bnc2=pygame.mixer.Sound("boun.wav")
win=pygame.mixer.Sound("Quee.wav")
win.set_volume(0.4)
count=pygame.mixer.Sound("count.wav")
myfont=pygame.font.SysFont('Arial',20)
myfont1=pygame.font.SysFont('Arial',40)
myfont2=pygame.font.SysFont('Arial',30)
goals_team1=0
goals_team2=0
bounces=3
label0=myfont2.render("This is a tennis game between",1,GREEN)
label7=myfont2.render("BLUE TEAM VS. YELLOW TEAM",1,GREEN)
label8=myfont2.render("The first team scoring 10 goals wins",1,GREEN)
label9=myfont.render("Press any key to start....",1,GREEN)
screen.blit(label0,(55,200))
screen.blit(label7,(55,300))
screen.blit(label8,(55,400))
screen.blit(label9,(55,500))
pygame.display.update()
res=0

while res==0:
    for event in pygame.event.get():
        if event.type==KEYDOWN or event.type==MOUSEBUTTONDOWN:
            count.play()
            res=1
        elif event.type == QUIT or (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            sys.exit()
        else:
            continue
pygame.time.wait(7000)
bounce_count=0

while True and goals_team1<10 and goals_team2<10:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            sys.exit()
    if 630>=ball.pos1>=10 and 40<=ball.pos2<=760 and ball.x>0 and ball.y>0:
        ball.move(1,1)
        bouncer2.move()
        bouncer.move()
    elif 630>=ball.pos1>=10 and ball.pos2==761 and ball.x>0 and ball.y>0and ball.pos1 in range(
                    bouncer.pos1-int(0.1*bouncer.height),bouncer.pos1+int(1.1*bouncer.height)):
        bnc1.play()
        ball.move(1,-1)
        bouncer.move()
        bouncer2.move()
        if bounces>0:
            bounces-=1
    elif 630>=ball.pos1>=10 and ball.pos2==761 and ball.x>0 and ball.y>0and not ball.pos1 in range(
                    bouncer.pos1-int(0.1*bouncer.height),bouncer.pos1+int(1.1*bouncer.height)):
        ball.move(1,1)
        bouncer.move()
        bouncer2.move()
    elif ball.pos2>761 and ball.x>0 and ball.y>0 and ball.pos1 in range(
                bouncer.pos1-int(0.2*bouncer.height),bouncer.pos1+int(0.5*bouncer.height))and bounce_count==0:
        bounce_count+=1
        ball.move(-2,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)
    elif ball.pos2>761 and ball.x>0 and ball.y>0 and ball.pos1 in range(
                bouncer.pos1+int(0.5*bouncer.height),bouncer.pos1+int(1.2*bouncer.height))and bounce_count==0:
        bounce_count+=1
        ball.move(2,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)
    elif ball.pos2>761 and ball.x>0 and ball.y>0 and bounce_count!=0:
        ball.move(2,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)
    elif ball.pos2>761 and ball.x<0 and ball.y>0 and bounce_count!=0:
        ball.move(-2,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)


    elif ball.pos2>761 and ball.x>0 and ball.y>0and not ball.pos1 in range(
                    bouncer.pos1-int(0.2*bouncer.height),bouncer.pos1+int(1.2*bouncer.height))and bounce_count==0:
        ball.move(1,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)
    elif 630>=ball.pos1>=10 and 40<=ball.pos2<=760 and ball.x>0 and ball.y<0:
        ball.move(1,-1)
        bouncer.move()
        bouncer2.move()
    elif ball.pos1>630 and 40<=ball.pos2<=760 and ball.x>0 and ball.y<0:
        ball.move(-1,-1)
        bouncer.move()
        bouncer2.move()
    elif 630>=ball.pos1>=10 and 40<=ball.pos2<=760 and ball.x<0 and ball.y<0:
        ball.move(-1,-1)
        bouncer.move()
        bouncer2.move()
    elif 630>=ball.pos1>=10 and ball.pos2==39 and ball.x<0 and ball.y<0and ball.pos1 in range(
                    bouncer2.pos1-int(0.1*bouncer2.height),bouncer2.pos1+int(1.1*bouncer2.height)):
        bnc2.play()
        ball.move(-1,1)
        bouncer.move()
        bouncer2.move()
        if bounces>0:
            bounces-=1
    elif 630>=ball.pos1>=10 and ball.pos2==39 and ball.x<0 and ball.y<0and not ball.pos1 in range(
                    bouncer2.pos1-int(0.1*bouncer2.height),bouncer2.pos1+int(1.1*bouncer2.height)):
        ball.move(-1,-1)
        bouncer.move()
        bouncer2.move()

    elif ball.pos2<39 and ball.x<0 and ball.y<0 and ball.pos1 in range(
                    bouncer2.pos1+int(0.5*bouncer2.height),bouncer2.pos1+int(1.2*bouncer2.height)) and bounce_count==0:
        bounce_count+=1
        ball.move(2,-1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif ball.pos2<39 and ball.x<0 and ball.y<0 and ball.pos1 in range(
                    bouncer2.pos1-int(0.2*bouncer2.height),bouncer2.pos1+int(0.5*bouncer2.height)) and bounce_count==0:
        bounce_count+=1
        ball.move(-2,-1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif ball.pos2<39 and ball.x<0 and ball.y<0 and bounce_count!=0:
        ball.move(-2,-1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif ball.pos2<39 and ball.x<0 and ball.y<0 and not ball.pos1 in range(
                    bouncer2.pos1-int(0.2*bouncer2.height),bouncer2.pos1+int(1.2*bouncer2.height)) and bounce_count==0:
        ball.move(-1,-1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif 630>=ball.pos1>=10 and 40<=ball.pos2<=760 and ball.x<0 and ball.y>0:
        ball.move(-1,1)
        bouncer.move()
        bouncer2.move()
    elif ball.pos1<10 and 40<=ball.pos2<=760 and ball.x<0 and ball.y>0:
        ball.move(1,1)
        bouncer.move()
        bouncer2.move()
    elif 630>=ball.pos1>=10 and ball.pos2==39 and ball.x>0 and ball.y<0 and ball.pos1 in range(
                    bouncer2.pos1-int(0.1*bouncer2.height),bouncer2.pos1+int(1.1*bouncer2.height)):
        bnc2.play()
        ball.move(1,1)
        bouncer.move()
        bouncer2.move()
        if bounces>0:
            bounces-=1
    elif 630>=ball.pos1>=10 and ball.pos2==39 and ball.x>0 and ball.y<0 and not ball.pos1 in range(
                    bouncer2.pos1-int(0.1*bouncer2.height),bouncer2.pos1+int(1.1*bouncer2.height)):
        ball.move(1,-1)
        bouncer.move()
        bouncer2.move()
    elif ball.pos2<39 and ball.x>0 and ball.y<0 and ball.pos1 in range(
                    bouncer2.pos1-int(0.2*bouncer2.height),bouncer2.pos1+int(0.5*bouncer2.height)) and bounce_count==0:
        ball.move(-2,-1)
        bounce_count+=1
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif ball.pos2<39 and ball.x>0 and ball.y<0 and ball.pos1 in range(
                    bouncer2.pos1+int(0.5*bouncer2.height),bouncer2.pos1+int(1.2*bouncer2.height)) and bounce_count==0:
        ball.move(2,-1)
        bounce_count+=1
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif ball.pos2<39 and ball.x>0 and ball.y<0 and bounce_count!=0:
        ball.move(2,-1)
        bounce_count+=1
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif ball.pos2<39 and ball.x>0 and ball.y<0 and ball.y<0 and not ball.pos1 in range(
                    bouncer2.pos1-int(0.2*bouncer2.height),bouncer2.pos1+int(1.2*bouncer2.height)) and bounce_count==0:
        ball.move(1,-1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==-10:
            goals_team2+=1
            sound.play()
            ball.pos1=40
            ball.pos2=40
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,1)
    elif ball.pos1>630 and 40<=ball.pos2<=760 and ball.x>0 and ball.y>0:
        ball.move(-1,1)
        bouncer.move()
        bouncer2.move()
    elif 630>=ball.pos1>=10 and ball.pos2==761 and ball.x<0 and ball.y>0 and ball.pos1 in range(
                    bouncer.pos1-int(0.1*bouncer.height),bouncer.pos1+int(1.1*bouncer.height)):
        bnc1.play()
        ball.move(-1,-1)
        bouncer.move()
        bouncer2.move()
        if bounces>0:
            bounces-=1
    elif 630>=ball.pos1>=10 and ball.pos2==761 and ball.x<0 and ball.y>0 and not ball.pos1 in range(
                    bouncer.pos1-int(0.1*bouncer.height),bouncer.pos1+int(1.1*bouncer.height))and bounce_count==0:
        ball.move(-1,1)
        bouncer.move()
        bouncer2.move()
    elif ball.pos2>761 and ball.x<0 and ball.y>0 and ball.pos1 in range(
                bouncer.pos1+int(0.5*bouncer.height),bouncer.pos1+int(1.2*bouncer.height)) and bounce_count==0:
        bounce_count+=1
        ball.move(2,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)
    elif ball.pos2>761 and ball.x<0 and ball.y>0 and ball.pos1 in range(
                bouncer.pos1-int(0.2*bouncer.height),bouncer.pos1+int(0.5*bouncer.height)) and bounce_count==0:
        bounce_count+=1
        ball.move(-2,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)
    elif ball.pos2>761 and ball.x<0 and ball.y>0 and not ball.pos1 in range(
                    bouncer.pos1-int(0.2*bouncer.height),bouncer.pos1+int(1.2*bouncer.height))and bounce_count==0:
        ball.move(-1,1)
        bouncer.move()
        bouncer2.move()
        if ball.pos2==810:
            goals_team1+=1
            sound.play()
            ball.pos1=600
            ball.pos2=760
            bounce_count=0
            pygame.time.delay(1000)
            bounces=3
            ball.move(1,-1)
    elif ball.pos1<10 and 40<=ball.pos2<=760 and ball.x<0 and ball.y<0:
        ball.move(1,-1)
        bouncer.move()
        bouncer2.move()
    ball.draw_circle()
    bouncer.draw_rect()
    bouncer2.draw_rect()
    blue_team_result=str("BLUE TEAM    {:>20}".format(str(goals_team1)))
    yellow_team_result=str("YELLOW TEAM{:>19}".format(str(goals_team2)))
    label=myfont.render(blue_team_result,1,GREEN)
    label1=myfont.render(yellow_team_result,1,GREEN)
    label5=myfont2.render("Press Enter for new game or esc to quit",1,GREEN)
    if goals_team1==10:
        screen.blit(label,(200,100))
        screen.blit(label1,(200,260))
        label2=myfont1.render("BLUE TEAM WON THIS GAME",10,GREEN)
        win.play()
        screen.blit(label2,(55,380))
        screen.blit(label5,(60,440))
        pygame.display.update()
        res=0
        while res==0:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)or event.type == QUIT :
                    res=1
                    sys.exit()
                elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                    win.stop()
                    goals_team1=0
                    goals_team2=0
                    res=1
                else:
                    continue
    elif goals_team2==10:
        screen.blit(label,(200,100))
        screen.blit(label1,(200,260))
        label3=myfont1.render("YELLOW TEAM WON THIS GAME",1,GREEN)
        win.play()
        screen.blit(label3,(50,380))
        screen.blit(label5,(60,440))
        pygame.display.update()
        res=0
        while res==0:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)or event.type == QUIT:
                    res=1
                    sys.exit()
                elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                    win.stop()
                    goals_team1=0
                    goals_team2=0
                    res=1
                else:
                    continue
    screen.blit(label,(200,300))
    screen.blit(label1,(200,460))
    pygame.time.delay(bounces)

sys.exit()
pygame.quit()





