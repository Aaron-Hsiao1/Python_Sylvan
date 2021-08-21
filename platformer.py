#NOTES  
 
#main menu
 
# menu_loop = True
# escape_loop = False

# game_loop:
#   while menu_loop:
#       menu code

#   if key pressed:
#       menu_loop = False

#   game code
#   if key pressed:
#       escape_loop = True  
#   while escape_loop:
#       pause code
#   while y > 1280:
#       end screen menu
#       if key pressed:
#           menu_loop = True



#add camera following person around - lollipop ninja
#add random platorms - spike dungeon
#smooth character jumping - lollipop ninja

import pygame
import mixer
import random
pygame.init()
pygame.mixer.init() 
#pygame.mixer.pre_init(44100, 16, 2, 4096)  

screenWidth = 1920
screenHeight = 1080

pygame.mixer.music.load('Sounds/jump2.mp3')
pygame.mixer.music.set_volume(0.1)
screen = pygame.display.set_mode((screenWidth,screenHeight), pygame.FULLSCREEN)
pygame.display.toggle_fullscreen()

gameRunning = False
masterLoop = True
gameMenu = True
gamePause = False
pygame.display.set_caption("Jump!")

walkRight = [pygame.image.load('NewPiskel/sprite_00.png'), pygame.image.load('NewPiskel/sprite_01.png'), pygame.image.load('NewPiskel/sprite_02.png'), pygame.image.load('NewPiskel/sprite_03.png'), pygame.image.load('NewPiskel/sprite_04.png'), pygame.image.load('NewPiskel/sprite_05.png')]
walkLeft = [pygame.image.load('NewPiskel/sprite_00.png'), pygame.image.load('NewPiskel/sprite_01.png'), pygame.image.load('NewPiskel/sprite_02.png'), pygame.image.load('NewPiskel/sprite_03.png'), pygame.image.load('NewPiskel/sprite_04.png'), pygame.image.load('NewPiskel/sprite_05.png')]
#bg = pygame.image.load('snakes/sprite_background00.png')
char = pygame.image.load('NewPiskel/sprite_00.png')

background = pygame.image.load('Background/bluesky.png')

startMenu = pygame.image.load('Background/start.png')
 
score = 0

canJump = 0

velocity = 0

numJumps = 10

debug = False
debugtimer = 0
candebug = True

left = False
right = False   
walkCount = 0

platformmin = 100
platformmax = 200

platformymin = -200
platformymax = 200

platform_1_x = random.randint(10,400)
platform_1_y = random.randint(500,1080)
platform_1_width = 200
platform_1_height = 20

platform_2_x = random.randint(platformmin,platformmax) + platform_1_x
platform_2_y = random.randint(platformymin,platformymax) + platform_1_y
platform_2_width = 200
platform_2_height = 20

platform_3_x = random.randint(platformmin,platformmax) + platform_2_x
platform_3_y = random.randint(platformymin,platformymax) + platform_2_y
platform_3_width = 200
platform_3_height = 20

platform_4_x = random.randint(platformmin,platformmax) + platform_3_x
platform_4_y = random.randint(platformymin,platformymax) + platform_3_y
platform_4_width = 200
platform_4_height = 20

platform_5_x = random.randint(platformmin,platformmax) + platform_4_x
platform_5_y = random.randint(500,1080)
platform_5_width = 200
platform_5_height = 20

platform_6_x = random.randint(platformmin,platformmax) + platform_5_x
platform_6_y = random.randint(platformymin,platformymax) + platform_5_y
platform_6_width = 200 
platform_6_height = 20


platform_7_x = random.randint(platformmin,platformmax) + platform_6_x
platform_7_y = random.randint(platformymin,platformymax) + platform_6_y
platform_7_width = 200
platform_7_height = 20

platform_8_x = random.randint(platformmin,platformmax) + platform_7_x
platform_8_y = random.randint (platformymin,platformymax) + platform_7_y
platform_8_width = 200
platform_8_height = 20

platform_9_x = random.randint(platformmin,platformmax) + platform_8_x
platform_9_y = random.randint(platformymin,platformymax) + platform_8_y
platform_9_width = 200
platform_9_height = 20
playerX = platform_1_x 
playerY = platform_1_y -25
player_width = 10
player_height = 10

ableToJump = True
abletojumpvar = True
jumpSec = 0
globalTimer = 0
timer = False
#def if_hit(playerX:int, playerY:int, dodgeballX:int, dodgeballY:int, Bottom:int, Bottom2:int) -> (None):
    #if playerX >= dodgeballX and playerX <= dodgeballX+30 and playerY <= dodgeballY and playerY >= dodgeballY-30:
        #dodgeballX = random.randrange(0, 1140, 30)
        #dodgeballY = random.randrange(-120, -60, 1)
        #Bottom2 +=1


def abovePlatform():
    global platform_1_x
    global platform_2_x
    global platform_3_x
    global platform_4_y
    global platform_5_y
    global platform_6_y
    global platform_7_y
    global platform_8_y
    global platform_9_y

    global platform_1_width
    global platform_2_width
    global platform_3_width
    global platform_4_width
    global platform_5_width
    global platform_6_width
    global platform_7_width
    global platform_8_width
    global platform_9_width
    global playerX
    global playerY
    if playerX >= platform_1_x -10 and playerX <= platform_1_x + platform_1_width and playerY + player_height >= platform_1_y and playerY + player_height <= platform_1_y + 5:    
        return True 
    elif playerX >= platform_2_x - 10 and playerX <= platform_2_x + platform_2_width and playerY + player_height >= platform_2_y and playerY + player_height <= platform_2_y + 5: 
        return True
    elif playerX >= platform_3_x - 10 and playerX <= platform_3_x + platform_3_width and playerY + player_height >= platform_3_y and playerY + player_height <= platform_3_y + 5:
        return True
    elif playerX >= platform_4_x - 10 and playerX <= platform_4_x + platform_4_width and playerY + player_height >= platform_4_y and playerY + player_height <= platform_4_y + 5:
        return True
    elif playerX >= platform_5_x - 10 and playerX <= platform_5_x + platform_5_width and playerY + player_height >= platform_5_y and playerY + player_height <= platform_5_y + 5:
        return True
    elif playerX >= platform_6_x - 10 and playerX <= platform_6_x + platform_6_width and playerY + player_height >= platform_6_y and playerY + player_height <= platform_6_y + 5:
        return True
    elif playerX >= platform_7_x - 10 and playerX <= platform_7_x + platform_7_width and playerY + player_height >= platform_7_y and playerY + player_height <= platform_7_y + 5:
        return True
    elif playerX >= platform_8_x - 10 and playerX <= platform_8_x + platform_8_width and playerY + player_height >= platform_8_y and playerY + player_height <= platform_8_y + 5:
        return True
    elif playerX >= platform_9_x - 10 and playerX <= platform_9_x + platform_9_width and playerY + player_height >= platform_9_y - 7 and playerY + player_height <= platform_9_y + 5:
        return True
    else: 
        return False
    
def ifHitTop():
    global playerX
    global playerY
    global player_height
    global platform_1_y
    global platform_2_y
    global platform_3_y
    global platform_4_y
    global platform_5_y
    if playerY + player_height >= platform_1_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_2_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_3_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_4_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_5_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_6_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_7_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_8_y and abovePlatform() == True:
        return True
    elif playerY + player_height >= platform_9_y and abovePlatform() == True:
        return True
    else:
        return False
def ifHitRight():
    global playerX
    global player_width
    if playerX + player_width >= 1920:             
        return True
    else:
        return False
def ifHitLeft():
    global playerX
    if playerX >= 0:
        return True
    else:
        return False

def tpOutofPlatform():
    global platform_1_height
    global platform_2_height
    global platform_3_height
    global platform_4_height
    global platform_5_height
    global platform_6_height
    global platform_7_height
    global platform_8_height
    global platform_9_height
    global platform_1_width
    global platform_2_width
    global platform_3_width
    global platform_4_width
    global platform_6_width
    global platform_7_width
    global platform_8_width
    global platform_9_width
    global platform_1_x
    global platform_2_x
    global platform_3_x
    global platform_4_x
    global platform_5_x
    global platform_6_x
    global platform_7_x
    global platform_8_x
    global platform_9_x
    global platform_1_y
    global platform_2_y
    global platform_3_y
    global platform_4_y
    global platform_5_y
    global platform_6_y
    global platform_7_y 
    global platform_8_y
    global platform_9_y
    global playerY
    global playerX
    global player_height
    global velocity
    #if playerX >= platform_1_x and playerX <= platform_1_x + platform_1_width:
    if (abovePlatform() == True and playerX >= platform_1_x and playerX <= platform_1_x + platform_1_width) or (playerX >= platform_1_x and playerX <= platform_1_x + platform_1_width and playerY > platform_1_height and velocity == 0):
        playerY = platform_1_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_2_x and playerX <= platform_2_x + platform_2_width) or (playerX >= platform_2_x and playerX <= platform_2_x + platform_2_width and playerY > platform_2_height and velocity == 0):
        playerY = platform_2_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_3_x and playerX <= platform_3_x + platform_3_width) or (playerX >= platform_3_x and playerX <= platform_3_x + platform_3_width and playerY > platform_3_height and velocity == 0):
        playerY = platform_3_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_4_x and playerX <= platform_4_x + platform_4_width) or (playerX >= platform_4_x and playerX <= platform_4_x + platform_4_width and playerY > platform_4_height and velocity == 0):
        playerY = platform_4_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_5_x and playerX <= platform_5_x + platform_5_width) or (playerX >= platform_5_x and playerX <= platform_5_x + platform_5_width and playerY > platform_5_height and velocity == 0):
        playerY = platform_5_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_6_x and playerX <= platform_6_x + platform_6_width) or (playerX >= platform_6_x and playerX <= platform_6_x + platform_6_width and playerY > platform_6_height and velocity == 0):
        playerY = platform_6_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_7_x and playerX <= platform_7_x + platform_7_width) or (playerX >= platform_7_x and playerX <= platform_7_x + platform_7_width and playerY > platform_7_height and velocity == 0):
        playerY = platform_7_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_8_x and playerX <= platform_8_x + platform_8_width) or (playerX >= platform_8_x and playerX <= platform_8_x + platform_8_width and playerY > platform_8_height and velocity == 0):
        playerY = platform_8_y - player_height - 1
        velocity = 0
    if (abovePlatform() == True and playerX >= platform_9_x and playerX <= platform_9_x + platform_9_width) or (playerX >= platform_9_x and playerX <= platform_9_x + platform_9_width and playerY > platform_9_height and velocity == 0):
        playerY = platform_9_y - player_height - 1
        velocity = 0
    #playerY = platform_2_y - player_height - 13
    print("e")

def ifinPlatform():
    global playerY
    global playerX
    global player_width
    global player_height
    global platform_1_height
    global platform_1_y
    
    if playerY + player_height > platform_1_y and playerY + player_height < platform_1_y + platform_1_height:
        if abovePlatform() == True and playerX >= platform_1_x and playerX <= platform_1_x + platform_1_width:
            tpOutofPlatform()
    if playerY + player_height > platform_2_y and playerY + player_height < platform_2_y + platform_2_height:
        if abovePlatform() == True and playerX >= platform_2_x and playerX <= platform_2_x + platform_2_width:
            tpOutofPlatform()
    if playerY + player_height > platform_3_y and playerY + player_height < platform_3_y + platform_3_height:
        if abovePlatform() == True and playerX >= platform_3_x and playerX <= platform_3_x + platform_3_width:
            tpOutofPlatform()
    if playerY + player_height > platform_4_y and playerY + player_height < platform_4_y + platform_4_height:
        if abovePlatform() == True and playerX >= platform_4_x and playerX <= platform_4_x + platform_4_width:
            tpOutofPlatform()
    if playerY + player_height > platform_5_y and playerY + player_height < platform_5_y + platform_5_height:
        if abovePlatform() == True and playerX >= platform_5_x and playerX <= platform_5_x + platform_5_width:
            tpOutofPlatform()
    if playerY + player_height > platform_6_y and playerY + player_height < platform_6_y + platform_6_height:
        if abovePlatform() == True and playerX >= platform_6_x and playerX <= platform_6_x + platform_6_width:
            tpOutofPlatform()
    if playerY + player_height > platform_7_y and playerY + player_height < platform_7_y + platform_7_height:
        if abovePlatform() == True and playerX >= platform_7_x and playerX <= platform_7_x + platform_7_width:
            tpOutofPlatform()
    if playerY + player_height > platform_8_y and playerY + player_height < platform_8_y + platform_8_height:
        if abovePlatform() == True and playerX >= platform_8_x and playerX <= platform_8_x + platform_8_width:
            tpOutofPlatform()
    if playerY + player_height > platform_9_y and playerY + player_height < platform_9_y + platform_9_height:
        if abovePlatform() == True and playerX >= platform_9_x and playerX <= platform_9_x + platform_9_width:
            tpOutofPlatform()





def changeYVelocity():
    global velocity
    global playerY
    global canJump
    global numJumps
    #print(numJumps)
    #print("e")
    if controls[pygame.K_SPACE] and numJumps > 0: #and ifHitTop() == True:
        playerY -= 10
        velocity = -10
        pygame.mixer.music.play()
        canJump = 1
        numJumps -= 1
    elif not abovePlatform() and velocity != 6:
        velocity += 1 
    if abovePlatform():
        velocity = 0
        canJump = 0
        numJumps = 10
        #print("b")
    
    playerY += velocity




def resetglobaltimer():
    global globalTimer
    globalTimer = 0

def addglobaltimer():
    global globalTimer
    globalTimer += 5
def redrawGameWindow(): 
    global walkCount
    global playerX
    global playerY

    #win.blit(bg, (0,0))  
    if walkCount + 1 >= 18:
        walkCount = 0
        
    if isMoving:  
        screen.blit(walkLeft[0], (playerX,playerY))
        #walkCount += 1                          
    else:
        screen.blit(char, (playerX, playerY))
        walkCount = 0
        
    #pygame.display.update() 

def directions():

    global globalTimer
    global velocity
    global playerY
    #ifhit directoins
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render((str(ifHitTop())+" ifhittop"),1,((255,255,200)))
    screen.blit(text, (1700,700)) 
    
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render((str(ifHitLeft()) + " ifhitleft"),1,((255,255,255)))
    screen.blit(text, (700,500)) 

    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render((str(ifHitRight()) + " ifhitright"),1,((255,255,255)))
    screen.blit(text, (700,300)) 
    #velocity
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render((str(velocity)+" changeyvelocity"),1,((255,255,200)))
    screen.blit(text, (700,900)) 
    #printing variables to screen
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render(str(playerX) + '  ' + str(playerY),1,((255,255,255)))
    screen.blit(text, (300,300))
    #respawn
    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render("Press X to Respawn",1,((0,0,0)))
    screen.blit(text, (1000,1000))


def checkglobaltimer():
    global timer
    global globalTimer
    if globalTimer >= 200:
        timer = False
        resetglobaltimer()  
    if globalTimer <= 200 and timer == True:
        addglobaltimer()




def platformRespawn():
    global platform_1_x
    global platform_1_width
    global platform_2_x
    global platform_2_width
    global platform_3_x
    global platform_3_width
    global platform_4_x
    global platform_4_width 
    global platform_5_x
    global platform_5_width
    global platform_6_x
    global platform_6_width
    global platform_7_x
    global platform_7_width
    global platform_8_x
    global platform_8_width
    global platform_9_x

    #left to right
    if platform_1_x + platform_1_width < 0:
        platform_1_x = random.randint(1620,1920)
    if platform_2_x + platform_2_width < 0:
        platform_2_x = random.randint(1320,1620)
    if platform_3_x + platform_3_width < 0:
        platform_3_x = platform_2_x + random.randint(1020,1320)
    if platform_4_x + platform_4_width < 0:
        platform_4_x = platform_3_x + random.randint(720,1020)
    if platform_5_x + platform_5_width < 0:
        platform_5_x = platform_4_x + random.randint(0,720)
    if platform_6_x + platform_6_width < 0:
        platform_6_x = platform_5_x + random.randint(0,720)
    if platform_7_x + platform_7_width < 0:
        platform_7_x = platform_6_x + random.randint(0,720)
    if platform_8_x + platform_8_width < 0:
        platform_8_x = platform_7_x + random.randint(0,720)
    if platform_9_x + platform_9_width < 0:
        platform_9_x = platform_8_x + random.randint(0,720)
    #right to left
    if platform_1_x + platform_1_width > 1920:
        platform_1_x = random.randint(0,720)
    if platform_2_x + platform_2_width > 1920:
        platform_2_x = random.randint(720, 1020)
    if platform_3_x + platform_3_width > 1920:
        platform_3_x = random.randint(1020,1320)
    if platform_4_x + platform_4_width > 1920:
        platform_4_x = random.randint(1320,1620)
    if platform_5_x + platform_5_width > 1920:  
        platform_5_x = random.randint(1620,1920)
    if platform_6_x + platform_6_width > 1920:  
        platform_6_x = random.randint(1620,1920)
    if platform_7_x + platform_7_width > 1920:  
        platform_7_x = random.randint(1620,1920)
    if platform_8_x + platform_8_width > 1920:  
        platform_8_x = random.randint(1620,1920)
    if platform_9_x + platform_9_width > 1920:  
        platform_9_x = random.randint(1620,1920)


def movePlatformRight():
    global platform_1_x
    global platform_2_x
    global platform_3_x
    global platform_4_x
    global platform_5_x
    global platform_6_x
    global platform_7_x
    global platform_8_x
    global platform_9_x
    platform_1_x += 1
    platform_2_x += 1
    platform_3_x += 1
    platform_4_x += 1
    platform_5_x += 1
    platform_6_x += 1
    platform_7_x += 1
    platform_8_x += 1
    platform_9_x += 1
def movePlatformRight():
    global platform_1_x
    global platform_2_x
    global platform_3_x
    global platform_4_x
    global platform_5_x
    global platform_6_x
    global platform_7_x
    global platform_8_x
    global platform_9_x
    platform_1_x += 1
    platform_2_x += 1
    platform_3_x += 1
    platform_4_x += 1
    platform_5_x += 1
    platform_6_x += 1
    platform_7_x += 1
    platform_8_x += 1
    platform_9_x += 1
def playerPlatform():
    global platform_1_x
    global platform_2_x
    global platform_3_x
    global platform_4_x
    global platform_5_x
    global platform_6_x
    global platform_7_x
    global platform_8_x
    global platform_9_x
    platformRight = min(platform_1_x, platform_2_x, platform_3_x, platform_4_x, platform_5_x, platform_6_x, platform_7_x, platform_8_x, platform_9_x)
    return platformRight 


def debugscreen():
    global debug
    font = pygame.font.SysFont('comicsans', 25, False, False)
    text = font.render("Player Y - " + str((playerY + player_height)),1,(100,100,100))
    screen.blit(text, (10,25)) 
    
    font = pygame.font.SysFont('comicsans', 25, False, False)
    text = font.render("Player X - " + str((playerX)),1,(100,100,100))
    screen.blit(text, (10,40))
    
    font = pygame.font.SysFont('comicsans', 25, False, False)
    text = font.render("Velocity - " + str((velocity)),1,(100,100,100))
    screen.blit(text, (10,55)) 
def resetdebugtimer():
    global debugtimer
    debugtimer = 0
def adddebugtimer():     
    global candebug
    global debugtimer
    if debugtimer >= 0 and debugtimer <= 1000:
        candebug = False    
        debugtimer += 10
    #print(debugtimer)
def checkdebugtimer():
    global debugtimer
    global candebug
    if debugtimer >= 1000 and debugtimer <= 2000:
        candebug = True
    #print(debugtimer)
    #print(candebug)
while masterLoop:
    while gameRunning:
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if playerY >= 1080:
            gameRunning = False
        if controls[pygame.K_ESCAPE]:
            gamePause = True
            gameRunning = False
        
        screen.blit(background, (0,0))
        controls = pygame.key.get_pressed()
        ifinPlatform()
        if controls[pygame.K_f]:
            pygame.display.toggle_fullscreen()

        
        changeYVelocity()
        #print (canJump)
        checkglobaltimer()

        print(score)

        #movePlatformZone()
        platformRespawn()

        adddebugtimer()

        if controls[pygame.K_q] and debugtimer >= 100:
            resetdebugtimer()
            debug = not debug
            adddebugtimer()

        if debug == True:
            debugscreen()

        if controls[pygame.K_a]:
            platform_1_x +=5
            platform_2_x +=5
            platform_3_x +=5
            platform_4_x +=5
            platform_5_x +=5
            platform_6_x +=5
            platform_7_x +=5
            platform_8_x +=5
            platform_9_x +=5    
            isMoving = True
            score -= 1
        elif controls[pygame.K_d]:
            platform_1_x -=5
            platform_2_x -=5
            platform_3_x -=5
            platform_4_x -=5
            platform_5_x -=5
            platform_6_x -=5
            platform_7_x -=5
            platform_8_x -=5
            platform_9_x -=5
            isMoving = True
            score += 1
        else:
            isMoving = False
            walkCount = 0

        
        #pygame.draw.rect(screen, (255,255,255), (playerX, playerY, player_width, player_height))

        # font = pygame.font.SysFont('comicsans', 25, False, False)
        # text = font.render(str((platform_1_y)),1,(100,100,100))
        # screen.blit(text, (10,40))
        # font = pygame.font.SysFont('comicsans', 100, False, False)
        # text = font.render(str((platform_2_y)),1,(200,200,200))
        # screen.blit(text, (1500,900))
        # font = pygame.font.SysFont('comicsans', 100, False, False)
        # text = font.render(str((platform_3_y)),1,(200,200,200))
        # screen.blit(text, (1500,500))  

        
        redrawGameWindow()


    
        # directions()


        font = pygame.font.SysFont('comicsans', 25, False, False)
        text = font.render("Score = " + (str(score)),10,(100,100,100))
        screen.blit(text, (10,10))
        
        
        #platform1
        pygame.draw.rect(screen, (255,0,0), (platform_1_x,platform_1_y, platform_1_width, platform_1_height))
        #pygame.draw.rect(screen, (255,255,255), (0,900, 900,10))
        #platform2
        pygame.draw.rect(screen, (255,128,0), (platform_2_x ,platform_2_y, platform_2_width, platform_2_height))
        #platform3
        pygame.draw.rect(screen, (255,255,51), (platform_3_x ,platform_3_y, platform_3_width, platform_3_height))
        #platform4
        pygame.draw.rect(screen, (0,255,0), (platform_4_x ,platform_4_y, platform_4_width, platform_4_height))
        #platform5  
        pygame.draw.rect(screen, (0,0,255), (platform_5_x ,platform_5_y, platform_5_width, platform_5_height))
        #platform6
        pygame.draw.rect(screen, (155,155,155), (platform_6_x ,platform_6_y, platform_6_width, platform_6_height))
        #platform7
        pygame.draw.rect(screen, (0,0,0), (platform_7_x ,platform_7_y, platform_7_width, platform_7_height))
        #platofrm8
        pygame.draw.rect(screen, (155,155,155), (platform_8_x ,platform_8_y, platform_8_width, platform_8_height))
        #platform9
        pygame.draw.rect(screen, (155,155,155), (platform_9_x ,platform_9_y, platform_9_width, platform_9_height))


        pygame.display.update()

    while gameMenu:
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
        screen.fill((0,0,0))
        controls = pygame.key.get_pressed()
        # font = pygame.font.SysFont('comicsans', 100, False, False)
        # text = font.render(str(("Press X to Start")),1,(255,255,255))
        screen.blit(startMenu,(0,0))
        # screen.blit(text, (screenWidth/2-285, screenHeight/2-30))
        if controls[pygame.K_x]:
            gameMenu = False
            gameRunning = True
        if controls[pygame.K_q]:
            pygame.quit()
        
        pygame.display.update()   

    while gamePause:
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        controls = pygame.key.get_pressed()
        if controls[pygame.K_x]:
            gameRunning = True
            gamePause = False
        if controls[pygame.K_q]:
            gameMenu = True
            gameRunning = False
            gamePause = False

        
        screen.blit(background,(0,0))
        pygame.draw.rect(screen, (255,0,0), (platform_1_x,platform_1_y, platform_1_width, platform_1_height))
        pygame.draw.rect(screen, (255,128,0), (platform_2_x ,platform_2_y, platform_2_width, platform_2_height))
        pygame.draw.rect(screen, (255,255,51), (platform_3_x ,platform_3_y, platform_3_width, platform_3_height))
        pygame.draw.rect(screen, (0,255,0), (platform_4_x ,platform_4_y, platform_4_width, platform_4_height)) 
        pygame.draw.rect(screen, (0,0,255), (platform_5_x ,platform_5_y, platform_5_width, platform_5_height))
        pygame.draw.rect(screen, (155,155,155), (platform_6_x ,platform_6_y, platform_6_width, platform_6_height))
        pygame.draw.rect(screen, (0,0,0), (platform_7_x ,platform_7_y, platform_7_width, platform_7_height))
        pygame.draw.rect(screen, (155,155,155), (platform_8_x ,platform_8_y, platform_8_width, platform_8_height))
        pygame.draw.rect(screen, (155,155,155), (platform_9_x ,platform_9_y, platform_9_width, platform_9_height))
        pygame.draw.rect(screen,(255,255,255),(playerX, playerY, player_width, player_height))
        s = pygame.Surface((1920,1080))  # the size of your rect
        s.set_alpha(150)                # alpha level
        s.fill((255,255,255))           # this fills the entire surface
        screen.blit(s, (0,0))    # (0,0) are the top-left coordinates  
        font = pygame.font.SysFont('comicsans', 100, False, False)
        text = font.render(str(("Press X to Continue")),1,(0,0,0))
        screen.blit(text, (screenWidth/2-350, screenHeight/2-30))
        font = pygame.font.SysFont('comicsans', 100, False, False)
        text = font.render(str(("Press Q to return to menu")),1,(0,0,0))
        screen.blit(text, (screenWidth/2-450, screenHeight/2+50))
        pygame.display.update()

    while playerY >= 1080:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        controls = pygame.key.get_pressed() 
        pygame.time.delay(5)
        screen.fill((0,0,0))
        font = pygame.font.SysFont('comicsans', 100, False, False)
        text = font.render(str(("Press X to Respawn")),1,(255,255,255))
        screen.blit(text, (screenWidth/2-350, screenHeight/2-30))  
        
        font = pygame.font.SysFont('comicsans', 100, False, False)
        text = font.render("Score = " + (str(score)),1,(255,255,255))
        screen.blit(text, (screenWidth/2-175, screenHeight/2-200))
        
        if controls[pygame.K_x]:
            playerY = 0
            score = 0
            gameRunning = True
        pygame.display.update()
    pygame.display.update()
    