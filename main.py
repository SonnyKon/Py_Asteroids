import pygame

debug: bool = True 

pygame.init()

shuttleMaxFlames = pygame.image.load('media/shuttleMaxFlames.png')
shuttleNoFlames = pygame.image.load('media/shuttleNoFlames.png')
shuttleSmallFlames = pygame.image.load('media/shuttleSmallFlames.png')

shuttleMaxFlames = pygame.transform.scale(shuttleMaxFlames, (100, 100))
shuttleNoFlames = pygame.transform.scale(shuttleNoFlames, (100, 100))
shuttleSmallFlames = pygame.transform.scale(shuttleSmallFlames, (100, 100))


screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("My little game") 
clock = pygame.time.Clock()
running = True

print(screen.get_size())

#screen.fill((0,0,0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # gather information for sceen drawing

    screenSize = screen.get_size()
    screencenter = (screenSize[0]/2, screenSize[1]/2)
    shipInitPosition = (screencenter[0]-50, screencenter[1]-50)
    # draw sceen
    screen.fill((255,255,255)) # (0,0,0)
    #pygame.draw.circle(screen, (255,255,255), screenSize, 20)
    screen.blit(shuttleNoFlames, shipInitPosition)

    #print(screen.get_size())
    pygame.display.flip()
    clock.tick(30)



pygame.quit()