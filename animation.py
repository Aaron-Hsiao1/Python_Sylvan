import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('NewPiskel/sprite_00.png'), pygame.image.load('NewPiskel/sprite_01.png'), pygame.image.load('NewPiskel/sprite_02.png'), pygame.image.load('NewPiskel/sprite_03.png'), pygame.image.load('NewPiskel/sprite_04.png'), pygame.image.load('NewPiskel/sprite_05.png')]
walkLeft = [pygame.image.load('NewPiskel/sprite_00.png'), pygame.image.load('NewPiskel/sprite_01.png'), pygame.image.load('NewPiskel/sprite_02.png'), pygame.image.load('NewPiskel/sprite_03.png'), pygame.image.load('NewPiskel/sprite_04.png'), pygame.image.load('NewPiskel/sprite_05.png')]
#bg = pygame.image.load('snakes/sprite_background00.png')
char = pygame.image.load('NewPiskel/sprite_00.png')

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

isMoving = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    #win.blit(bg, (0,0))  
    if walkCount + 1 >= 18:
        walkCount = 0
        
    if isMoving:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        isMoving = True

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        isMoving = True
        
    else: 
        isMoving = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            isMoving = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    win.fill((0,0,0))
    redrawGameWindow() 
    
    
pygame.quit()