import pygame
import random
import math

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    # Player dimentions on start. Centered and to the bottom
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
# Player dimentions on start. Centered and to the bottom
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# ready state, cant see the bullet. Fire, bullet is moving
bullet_state = "ready"


# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#show the score

def showScore(x, y):
    score = font.render("Score:" + " " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

# draw an image of player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX - bulletX), 2)) + (math.pow((enemyY - bulletY), 2)))
    if distance < 27:
        return True
    else:
        return False


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

    playerY += playerY_change

    # confining the spaceship to the width of the screen
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # confining the enemy to the width of the screen
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # calling player image on top of the screen image
    player(playerX, playerY)

    #SHOW SCORE
    showScore(textX,textY)

    # updating the screen to display icons and screen
    pygame.display.update()
