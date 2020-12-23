
#spleef hitball
#hitballs get bigger

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("meow")

A = random.randrange(0, 1140)
B = -30
C = random.randrange(0, 1140)
D = -90
E = random.randrange(0, 1140)
F = -30
# G = random.randrange(0, 1140, 30)
# H = random.randrange(0, 1140, 30)
# I = random.randrange(0, 1140, 30)
# J = random.randrange(0, 1140, 30)
# K = random.randrange(0, 1140, 30)
# L = random.randrange(0, 1140, 30)
# M = random.randrange(0, 1140, 30)
# N = random.randrange(0, 1140, 30)
green = (0,255,0) 
blue =  (0,0,255) 
red =  (255,0,0) 







# text = font.render('Hits', True,(0,100,100) , (255,0 ,0))
Bottom = 0
Bottom2 = 0
X = 570
Y = 1170
Width = 30
Height = 30
Speed = 8
matthew_exists = True
WHY = 1.0

def LOSE():
    screen.fill((0,0,0))
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render('YOU LOSE! Score: ' + str(Bottom2), 1, green)
    screen.blit(text, (400,50))
    pygame.time.delay(1000)
    pygame.quit()

def if_hit(playerX:int, playerY:int, dodgeballX:int, dodgeballY:int, Bottom:int, Bottom2:int) -> (None):
    if playerX >= dodgeballX and playerX <= dodgeballX+30 and playerY <= dodgeballY and playerY >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Bottom2 +=1

    
    if playerX+30 >= dodgeballX and playerX+30 <= dodgeballX+30 and playerY <= dodgeballY and playerY >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Bottom2 +=1


    if playerX >= dodgeballX and playerX <= dodgeballX+30 and playerY-30 <= dodgeballY and playerY-30 >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Bottom2 +=1


    if playerX+30 >= dodgeballX and playerX+30 <= dodgeballX+30 and playerY-30 <= dodgeballY and playerY-30 >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Bottom2 +=1


    
    if dodgeballY >= 1200:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Bottom +=1

    
    
    return dodgeballX, dodgeballY, Bottom, Bottom2, WHY

def Speedy(WHY:float) -> (None):
    WHY += 0.2


while matthew_exists:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    A,B,Bottom,Bottom2 = if_hit(X,Y,A,B, Bottom, Bottom2, )
    C,D,Bottom,Bottom2,  = if_hit(X,Y,C,D, Bottom, Bottom2, )
    E,F,Bottom,Bottom2,  = if_hit(X,Y,E,F, Bottom, Bottom2, )


    # if X >=A and X <= A+30 and Y <= B and Y >= B-30:
    #     A = random.randrange(0, 1140, 30)
    #     B =(-30)
    
    # if X+30 >=A and X+30 <= A+30 and Y <= B and Y >= B-30:
    #     A = random.randrange(0, 1140, 30)
    #     B =(-30)

    # if X >=A and X <= A+30 and Y-30 <= B and Y-30 >= B-30:
    #     A = random.randrange(0, 1140, 30)
    #     B =(-30)

    # if X+30 >=A and X+3
    # 0 <= A+30 and Y-30 <= B and Y-30 >= B-30:
    #     A = random.randrange(0, 1140, 30)
    #     B =(-30)
    
    B += WHY
    D += WHY
    F += WHY


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and 599 <= Y:
        Y -= Speed
    if keys[pygame.K_DOWN] and Y <= 1200 - Speed - Height:
        Y += Speed
    if keys[pygame.K_LEFT] and X >= Speed:
        X -= Speed
    if keys[pygame.K_RIGHT] and X <= 1200 - Speed - Width:
        X += Speed

    screen.fill((0, 0, 0))    

    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render('Score: ' + str(Bottom2), 1, green)
    screen.blit(text, (400,50))

    text2 = font.render('Misses: ' + str(Bottom), 1, green)
    screen.blit(text2, (400,100))



    pygame.draw.rect(screen, (255,255,255), (0, 570, 1200, Height))
    pygame.draw.rect(screen, (0,255,0), (X, Y, Width, Height))
    pygame.draw.rect(screen, (255,0,0), (int(A), int(B), Width, Height))
    pygame.draw.rect(screen, (0,225,255), (int(C), int(D), Width, Height))
    pygame.draw.rect(screen, (255,0, 98), (int(E), int(F), Width, Height))
    # pygame.draw.rect(screen, (255,247,0), (G, H, Width, Height))
    # pygame.draw.rect(screen, (255,0, 255), (I, J, Width, Height))
    # pygame.draw.rect(screen, (0,255,0), (K, L, Width, Height))
    # pygame.draw.rect(screen, (0,255,0), (M, N, Width, Height))

    pygame.display.update()
    
    if Bottom == 3:
        LOSE()



