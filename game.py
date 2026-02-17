import pygame
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

# Initialise a window (w = 800 h = 600)
gameDisplay = pygame.display.set_mode((display_width, display_height)) 

pygame.display.set_caption('Racing game') # Set window title

clock = pygame.time.Clock() # fps

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()


