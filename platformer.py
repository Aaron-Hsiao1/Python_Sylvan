#NOTES
#make player die/respawn


import pygame
pygame.init()

screen = pygame.display.set_mode((1920,1080))

gameRunning = True

pygame.display.set_caption("Jump!")


playerX = 1
playerY = 0



platform_1_x = 1000
platform_1_y = 500
platform_1_width = 100
platform_1_height = 20

platform_2_x = 200
platform_2_y = 500
platform_2_width = 100
platform_2_height = 20

platform_3_x = 400
platform_3_y = 100
platform_3_width = 100
platform_3_height = 20

playerX_width = 10
playerY_height = 10
numJumps = 0
ableToJump = True
gravity = True
stopLoopGravity = False
loopCountGravity = 0
abletojumpvar = True
jumpSec = 0
globalTimer = 0
gravitydirection = 1
timer = False
#def if_hit(playerX:int, playerY:int, dodgeballX:int, dodgeballY:int, Bottom:int, Bottom2:int) -> (None):
    #if playerX >= dodgeballX and playerX <= dodgeballX+30 and playerY <= dodgeballY and playerY >= dodgeballY-30:
        #dodgeballX = random.randrange(0, 1140, 30)
        #dodgeballY = random.randrange(-120, -60, 1)
        #Bottom2 +=1



def abovePlatform(platformx, platformy, platformwidth):
    if playerX >= platformx - 10 and playerX <= platformx + platformwidth and playerY <= platformy and gravitydirection == 1:
        return True
    else:
        return False
def ifHitTop(platformy,platformx, platformwidth):
    global playerX
    global playerY
    if playerY + playerY_height >= platformy and abovePlatform(platformx, platformy, platformwidth) == True and gravitydirection == 1:
        return True
    else:
        return False
def ifHitRight(platformx):
    global playerX
    global playerY
    if playerX >= platformx: 
        return True
    else:
        return False

def Gravity():
    global playerY
    global gravity
    global stopLoopGravity
    global loopCountGravity
    global platform_1_y
    global gravitydirection
    if loopCountGravity <= 200:
        if gravity == True and (ifHitTop(platform_1_y,platform_1_x, platform_1_width) or ifHitTop(platform_2_y, platform_2_x, platform_2_width) or ifHitTop(platform_3_y, platform_3_x, platform_3_width)) == False:
            playerY += gravitydirection



def reverseGravity():
    global gravitydirection
    global globalTimer
    #print("hello")
    gravitydirection = -2


def regularGravity():
    global gravitydirection
    #print("hello")
    gravitydirection = 1

def resetglobaltimer():
    global globalTimer
    globalTimer = 0

def addglobaltimer():
    global globalTimer
    globalTimer += 5

def directions():
    global gravitydirection
    global globalTimer
    #ifhit directoins
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(ifHitTop(platform_1_y, platform_1_x, platform_1_width)),1,((255,255,255)))
    screen.blit(text, (700,500)) 
    
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(ifHitLeft(platform_1_x)),1,((255,255,255)))
    screen.blit(text, (900,500)) 

    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(ifHitRight(platform_1_x)),1,((255,255,255)))
    screen.blit(text, (1100,500)) 
    #printing gravitydirection to screen
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(gravitydirection),1,((205,205,205)))
    screen.blit(text, (500,500)) 
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(globalTimer),1,((105,105,105)))
    screen.blit(text, (500,800))
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(timer),1,((105,105,105)))
    screen.blit(text, (100,800))

def checkglobaltimer():
    global timer
    global globalTimer
    if globalTimer >= 200:
        regularGravity()
        timer = False
        resetglobaltimer()  
    if globalTimer <= 200 and timer == True:
        addglobaltimer()



def movePlatformRight():
    global platform_1_x
    global platform_2_x
    global platform_3_x
    if platform_1_x >= 1919:
        platform_1_x = 0 - platform_1_width
    if platform_2_x >= 1919:
        platform_2_x = 0 - platform_2_width
    if platform_3_x >= 1919:
        platform_3_x = 0 - platform_3_width
    platform_1_x += 1
    platform_2_x += 1
    platform_3_x += 1


def movePlatformZone():
    if playerX >= 1820:
        movePlatformRight()
    if playerX <= 100:
        movePlatformLeft()
def movePlatformLeft():
    global platform_1_x
    global platform_2_x
    global platform_3_x
    if platform_1_x >= 1919:
        platform_1_x = 0 - platform_1_width
    if platform_2_x >= 1919:
        platform_2_x = 0 - platform_2_width
    if platform_3_x >= 1919:
        platform_3_x = 0 - platform_3_width
    platform_1_x -= 1
    platform_2_x -= 1
    platform_3_x -= 1


def platformRespawn():
    global platform_1_x
    global platform_1_width
    global platform_2_x
    global platform_2_width
    global platform_3_x
    global platform_3_width
    #left to right
    if platform_1_x + platform_1_width < 0:
        platform_1_x += platform_1_width + 1920
    if platform_2_x + platform_2_width < 0:
        platform_2_x += platform_2_width + 1920
    if platform_3_x + platform_3_width < 0:
        platform_3_x += platform_3_width + 1920
    #right to left
    if platform_1_x + platform_1_width > 1920:
        platform_1_x += platform_1_width + 1920
    if platform_2_x + platform_2_width > 1920:
        platform_2_x += platform_2_width + 1920
    if platform_3_x + platform_3_width > 1920:
        platform_3_x += platform_3_width + 1920

def movePlatformRight():
    global platform_1_x
    global platform_2_x
    global platform_3_x
    if platform_1_x >= 1919:
        platform_1_x = 0 - platform_1_width
    if platform_2_x >= 1919:
        platform_2_x = 0 - platform_2_width
    if platform_3_x >= 1919:
        platform_3_x = 0 - platform_3_width
    platform_1_x += 1
    platform_2_x += 1
    platform_3_x += 1
while gameRunning:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    if playerY >= 1080:
        gameRunning = False
    controls = pygame.key.get_pressed()

    checkglobaltimer()
    movePlatformZone()
    platformRespawn()

    if controls[pygame.K_SPACE] and playerY >= 0 and (ifHitTop(platform_1_y, platform_1_x, platform_1_width) or ifHitTop(platform_2_y, platform_2_x, platform_2_width) or ifHitTop(platform_3_y, platform_3_x, platform_3_width)) and gravitydirection == 1:
        reverseGravity()
        timer = True
    if controls[pygame.K_a] and playerX >= 1 and ifHitLeft(platform_1_x):
        playerX -= 1
    if controls[pygame.K_d] and playerX <= 1909 and ifHitRight(platform_1_x):
        playerX += 1
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,255,255), (playerX, playerY, playerX_width, playerY_height))
    


   
    directions()

    #gravity
    Gravity()

    #printing variables to screen
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(playerX) + '  ' + str(playerY),1,((255,255,255)))
    screen.blit(text, (300,300))
    
    
    #platform1
    pygame.draw.rect(screen, (155,155,155), (platform_1_x,platform_1_y, platform_1_width, platform_1_height))
    pygame.draw.rect(screen, (255,255,255), (0,900, 900,10))
    #platform2
    pygame.draw.rect(screen, (155,155,155), (platform_2_x ,platform_2_y, platform_2_width, platform_2_height))
    #platform3
    pygame.draw.rect(screen, (155,155,155), (platform_3_x ,platform_3_y, platform_3_width, platform_3_height))
    pygame.display.update()