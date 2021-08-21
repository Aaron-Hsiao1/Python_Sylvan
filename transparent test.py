import pygame

pygame.init()

X = 570
Y = 900
screen_width = 1000
screen_height = 1000
Width = 30
Height = 30
Speed = 8
looping = True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("blank")

while looping:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # def blit_alpha(target, source, opacity):
    #     x = 100
    #     y = 100
    #     temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    #     temp.blit(target, (-x, -y))
    #     temp.blit(source, (100, 100))
    #     temp.set_alpha(50)        
    #     target.blit(temp, (l00,100))



    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Y -= Speed
    if keys[pygame.K_DOWN]:
        Y += Speed
    if keys[pygame.K_LEFT]:
        X -= Speed
    if keys[pygame.K_RIGHT]:
        X += Speed

    screen.fill((0, 0, 0))  
    pygame.draw.rect(screen, (0,255,0), (X, Y, Width, Height))
    s = pygame.Surface((500,500))  # the size of your rect
    s.set_alpha(150)                # alpha level
    s.fill((255,255,255))           # this fills the entire surface
    screen.blit(s, (250,250))    # (0,0) are the top-left coordinates  
    pygame.display.update()