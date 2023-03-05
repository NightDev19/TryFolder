"""
Idea : Made Analog Clock Using Pygame

Creator : Sherwin Jefferson Tajan

This Project And Open Source If Anyone Want To Use It 
Make Sure That You'll Have The Permission Permission To The Creator (Me Sherwin Jefferson Tajan)
Thank You!
"""

import pygame , math
from datetime import datetime

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

Digital_Height = 100 
Width = 500
Height = Width + Digital_Height
Clock_Width = Width
Clock_Height = 500
Margin_Height = Margin_Width = 5

Clock_Radius = (Width - Margin_Width)/2
Hour_Hand = Clock_Radius/2
Minute_Hand = Clock_Radius*7/10
Second_Hand = Clock_Radius*8/10
Text_Radius = Clock_Radius*9/10

Tick_Radius = 2
Tick_Length = Hour_Stroke = 5
Minute_Stroke = Second_Stroke = Clock_Stroke = 2

Center_Width = Center_Height  = 10 
Hours = 12
Minutes = Seconds = 60

Size = (Width,Height)

def Center_Point(center , radius , theta):
    return(center[0]+ radius *math.cos(theta)),(center[1] + radius * math.sin(theta))
def Line_Angle(screen,center,radius,theta,color,width):
    point = Center_Point(center,radius,theta)
    pygame.draw.line(screen,color,center,point,width)
def Get_Angle(unit,total):
    return 2 * math.pi * unit / total - math.pi / 2

pygame.init()

screen = pygame.display.set_mode(Size)
pygame.display.set_caption("Analog Clock")
Hour_Font = pygame.font.SysFont('Calibri',25,True,False)
Digital_Font = pygame.font.SysFont('Calibri',32,False,False)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)

    now = datetime.now()

    x , y = Clock_Width / 2 ,Clock_Height / 2
    center = (x,y)

    """ Draw Clock"""
    pygame.draw.circle(
        screen,
        BLACK,
        center , Clock_Width / 2 - Margin_Width / 2,
        Clock_Stroke
    )

    """ Clock Mount """
    pygame.draw.circle(
        screen,
        BLACK,
        center,Clock_Width / 2 - Margin_Width / 2,
        Clock_Stroke
    )

    """ Draw Clock Hands """

    hour_theta = Get_Angle(now.hour + 1.0 * now.minute / Minutes ,Hours)
    minute_theta = Get_Angle(now.minute , Minutes)
    second_theta = Get_Angle(now.second ,Seconds)

    for(radius , theta , color , stroke ) in (
        (Hour_Hand , hour_theta , BLACK , Hour_Stroke),
        (Minute_Hand, minute_theta , BLACK , Minute_Stroke),
        (Second_Hand , second_theta , RED , Second_Stroke)
    ): Line_Angle (screen , center , radius , theta , color ,stroke)

    """ Hour Marking (Text) """
    for hour in range(1,Hours + 1) :
        theta = Get_Angle(hour , Hours)
        text = Hour_Font.render(str(hour) , True,BLACK)
        screen.blit(text,Center_Point(center , Text_Radius , theta))
    
    """ Minute Marking (Lines) """
    for minute in range(0,Minutes):
        theta = Get_Angle(minute , Minutes)
        p1 = Center_Point(center , Clock_Radius - Tick_Length,theta)
        p2 = Center_Point(center , Clock_Radius,theta)
        pygame.draw.line(screen , BLACK , p1 , p2 , Tick_Radius)
    

    """ Draw Digital Clock """
    digital_text = now.strftime("%H:%M:%S")
    text = Digital_Font.render(digital_text,True,BLACK)
    screen.blit(
        text,[
        Width / 2 - Digital_Font.size(digital_text)[0]/2,
        Height - Digital_Height / 2 - Digital_Font.size(digital_text)[1] / 2
        ]
    )
    pygame.display.flip()
    clock.tick(60)

pygame.quit()