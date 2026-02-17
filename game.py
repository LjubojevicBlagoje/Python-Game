import pygame
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Initialise a window 
gameDisplay = pygame.display.set_mode((display_width, display_height)) 

pygame.display.set_caption('Racing game') # Set window title

clock = pygame.time.Clock() # fps

carRaw = pygame.image.load('racecar.png')
# Flip the car image upside down
carImg = flipped_surface = pygame.transform.flip(carRaw, False, True)

def car(x,y):
    gameDisplay.blit(carImg,(x,y)) # Display the car at x,y

x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

# Event handling loop
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    gameDisplay.fill(white) # Set background
    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


