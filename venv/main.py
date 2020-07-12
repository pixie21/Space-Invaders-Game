import pygame

#Intialize pygame
pygame.init()

#creating first screen
#opens a new screen
screen = pygame.display.set_mode((800,600))

#Title and Logo for scree
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Players
playerImg = pygame.image.load('space-invaders.png')
# Player dimentions on start. Centered and to the bottom
playerX = 370
playerY = 480

#draw an image of player on the screen
def player():
    screen.blit(playerImg,(playerX,playerY))

#makes sure the screen remains open while a event is running
running = True
while running:
    # Screen color
    screen.fill((51, 0, 51))

    for event in pygame.event.get():
        # enabling the close button on the screen
        if event.type == pygame.QUIT:
            running = False


    #calling player image on top of the screen image
    player()
    #updating the screen to display icons and screen
    pygame.display.update()
