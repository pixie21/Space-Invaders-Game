import pygame
import random

# Intialize pygame
pygame.init()

# creating first screen
# opens a new screen
screen = pygame.display.set_mode((800, 600))

# creates background
background = pygame.image.load('background.png')

# Title and Logo for scree
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player/Spaceship
playerImg = pygame.image.load('space-invaders.png')
# Player dimentions on start. Centered and to the bottom
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Player/Enemy
enemyImg = pygame.image.load('enemy.png')
# Player dimentions on start. Centered and to the bottom
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
# Player dimentions on start. Centered and to the bottom
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# ready state, cant see the bullet. Fire, bullet is moving
bullet_state = "ready"


# draw an image of player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# makes sure the screen remains open while a event is running
running = True
while running:
    # Screen color
    screen.fill((51, 0, 51))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # enabling the close button on the screen
        if event.type == pygame.QUIT:
            running = False

        # check key stroke to determine direction and decrease/increase value
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            # if event.key == pygame.K_UP:
            #     playerY_change = -5
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # makes sure the spaceship stops moving when the key stops pressing
                playerX_change = 0
                playerY_change = 0

    # update the player coordinates
    playerX += playerX_change
    playerY += playerY_change
    enemyX += enemyX_change

    # confining the spaceship to the width of the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # confining the enemy to the width of the screen
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # calling player image on top of the screen image
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # updating the screen to display icons and screen
    pygame.display.update()
