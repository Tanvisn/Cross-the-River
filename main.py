import pygame
import random
import math
import time
import config
from config import  *
pygame.init()
# Creating screen display variable
screen = pygame.display.set_mode((1854,1000))
# Score controlling and exit flags
flag1_pl = True
flag2_pl = False
flag3_pl = False
flag4_pl = False
flag5_pl = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False
# Start text position
start_textX = 850
start_textY = 970
# End text position
end_textX = 850
end_textY = 5
# Title
pygame.display.set_caption("Cross The River")
# score
score_value1 = 0
score_value2 = 0
# Score display coordinates
score_text1X = 10
score_text1Y = 5
score_text2X = 1640
score_text2Y = 5

# player
playerImg = pygame.image.load('yacht2.png')
playerX = 370
playerY = 968
playerX_change = 0
playerY_change = 0

# Score showing function


def show_score1(x,y):
    score = font.render("Score1 :" + str(score_value1), True, (0, 0, 0))
    screen.blit(score, (x, y))

# Score showing function


def show_score2(x,y):
    score = font.render("Score2 :" + str(score_value2), True, (0, 0, 0))
    screen.blit(score, (x, y))

# Player showing function


def player(x, y):
    screen.blit(playerImg, (x, y))
# Obstacle coordinates and their respective blitting functions
fishImg = pygame.image.load( 'fish1.png' )
fishX = 10
fishY = 70
fishX_change = 1


def fish(x, y):
    screen.blit(fishImg, (x, y))


treeImg = pygame.image.load('coconut1.png')
treeX = 100
treeY = 120


def tree(x, y):
    screen.blit(treeImg, (x, y))


tree1Img = pygame.image.load('coconut1.png')
tree1X = 1500
tree1Y = 120


def tree1(x, y):
    screen.blit(tree1Img, (x, y))


tree2Img = pygame.image.load('coconut1.png')
tree2X = 1000
tree2Y = 280


def tree2(x, y):
    screen.blit(tree2Img, (x, y))


tree3Img =pygame.image.load('coconut1.png')
tree3X = 500
tree3Y = 280


def tree3(x, y):
    screen.blit(tree3Img, (x, y))


tree4Img =pygame.image.load('coconut1.png')
tree4X = 1700
tree4Y = 440


def tree4(x, y):
    screen.blit(tree4Img, (x, y))


tree5Img =pygame.image.load('coconut1.png')
tree5X = 900
tree5Y = 440


def tree5(x, y):
    screen.blit(tree5Img, (x, y))


tree6Img =pygame.image.load('coconut1.png')
tree6X = 1234
tree6Y = 600


def tree6(x, y):
    screen.blit(tree6Img, (x, y))


tree7Img =pygame.image.load('coconut1.png')
tree7X = 46
tree7Y = 600


def tree7(x, y):
    screen.blit(tree7Img, (x, y))


tree10Img =pygame.image.load('coconut1.png')
tree10X = 420
tree10Y = 600


def tree10(x, y):
    screen.blit(tree10Img, (x, y))


tree9Img =pygame.image.load('coconut1.png')
tree9X = 1469
tree9Y = 760


def tree9(x, y):
    screen.blit(tree9Img, (x, y))


tree8Img =pygame.image.load('coconut1.png')
tree8X = 672
tree8Y = 760


def tree8(x, y):
    screen.blit(tree8Img, (x, y))


fish1Img = pygame.image.load('dolly-fish.png')
fish1X = 300
fish1Y = 230
fish1X_change = 1.5

def fish1(x, y):
    screen.blit(fish1Img, (x, y))


fish2Img = pygame.image.load('octopus.png')
fish2X = 600
fish2Y = 390
fish2X_change = 1.5


def fish2(x, y):
    screen.blit(fish2Img, (x, y))


fish3Img = pygame.image.load('duck.png')
fish3X = 900
fish3Y = 550
fish3X_change = 1.5


def fish3(x, y):
    screen.blit(fish3Img, (x, y))


fish4Img = pygame.image.load('crocodile.png')
fish4X = 1200
fish4Y = 690
fish4X_change = 1.5


def fish4(x, y):
    screen.blit(fish4Img, (x, y))


fish5Img = pygame.image.load('spa.png')
fish5X = 1500
fish5Y = 850
fish5X_change = 1.5


def fish5(x, y):
    screen.blit(fish5Img, (x, y))
fish_arr = [fish,fish1,fish2,fish3,fish4,fish5]


def isCollision(fishX,fishY,playerX,playerY):
    distance = math.sqrt((math.pow(fishX-playerX,2)) + (math.pow(fishY-playerY,2)))
    if distance < 35:
        return True
    else:
        return False
over_font = pygame.font.Font('freesansbold.ttf',64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (700, 500))


def start(x,y):
    start_text = font.render("Start", True, (0, 0, 0))
    screen.blit(start_text, (x, y))


def end(x,y):
    end_text = font.render("End", True, (0, 0, 0))
    screen.blit(end_text, (x, y))


start11 = pygame.time.get_ticks()
time11 = 0
# Player1 round1
while True:
    # Display scree
    screen.fill(skyBlue)
    # Drawing lines on screen
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    # Calculating time of each loop
    stloop11 = pygame.time.get_ticks()
    time11 += (stloop11 - start11)
    time11 /= 1000
    time11 = round(time11)
    # Exit the code if quit button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    # Moving the obstacles
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 1.5

    elif fishX >= 1790:
            fishX = 0

    fish1X += fish1X_change
    if fish1X <= 0:
            fish1X = 1790

    elif fish1X >= 1790:
            fish1X_change = -1.5

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 1.5

    elif fish2X >= 1790:
            fish2X_change = -1.5
    fish3X += fish3X_change
    if fish3X <= 0:
            fish3X = 1790

    elif fish3X >= 1790:
            fish3X_change = -1.5

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 1.5

    elif fish4X >= 1790:
            fish4X_change = -1.5
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 1.5

    elif fish5X >= 1790:
            fish5X_change = -1.5
    # Incrementing score if a partition is crossed
    if flag1_pl:
        if playerY <= 810:
            score_value1 += 10
            flag1_pl = False
            flag1_mi = True
            flag2_pl = True

    if flag2_pl:
        if playerY <= 650:
            score_value1 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True

    if flag3_pl:
        if playerY <= 490:
            score_value1 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True

    if flag4_pl:
        if playerY <= 330:
            score_value1 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True

    if flag5_pl:
        if playerY <= 170:
            score_value1 += 10
            flag5_pl = False
            flag5_mi = True
    # Storing the results of collision function
    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)
    # Calling the obstacle display functions
    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    # If player collides next round is started and score is decremented by 20
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2   Round 1", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl1 = True

    elif exfl1:
        score_value1 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 1", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl2 = True

    elif exfl2:
        score_value1 -= 20
        break
    elif collision12 or collision13 or collision14 or collision15 or collision16:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 1", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl3 = True

    elif exfl3:
        score_value1 -= 20
        break
    # Even if the player reaches to end new round is started
    elif playerY < 20:
        for i in range (3):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 1", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl4 = True

    elif exfl4:
        break

    pygame.display.update()
# End of Player1 Round1

start_textX = 850
start_textY = 5
end_textX = 850
end_textY = 970
playerX = 370
playerY = 0
flag1_pl = True
flag1_mi = True
flag2_pl = False
flag2_mi = False
flag3_pl = False
flag3_mi = False
flag4_pl = False
flag4_mi = False
flag5_pl = False
flag5_mi = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False

start21 = pygame.time.get_ticks()
time21 = 0
# Player2 round1
while True:
    screen.fill(skyBlue)
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    stloop21 = pygame.time.get_ticks()
    time21 += (stloop21 - start21)
    time21 /= 1000
    time21 = round(time11)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 1.5

    elif fishX >= 1790:
        fishX = 0


    fish1X += fish1X_change
    if fish1X <= 0:
        fish1X = 1790


    elif fish1X >= 1790:
            fish1X_change = -1.5

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 1.5

    elif fish2X >= 1790:
            fish2X_change = -1.5
    fish3X += fish3X_change
    if fish3X <= 0:
        fish3X = 1790


    elif fish3X >= 1790:
            fish3X_change = -1.5

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 1.5

    elif fish4X >= 1790:
            fish4X_change = -1.5
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 1.5

    elif fish5X >= 1790:
            fish5X_change = -1.5

    if flag1_pl:
        if playerY >= 170:
            score_value2 += 10
            flag1_pl = False
            flag1_mi = True
            flag2_pl = True

    if flag2_pl:
        if playerY >= 330:
            score_value2 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True


    if flag3_pl:
        if playerY >= 490:
            score_value2 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True

    if flag4_pl:
        if playerY >= 650:
            score_value2 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True


    if flag5_pl:
        if playerY >= 810:
            score_value2 += 10
            flag5_pl = False
            flag5_mi = True

    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)
    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1   Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl1 = True

    elif exfl1:
        score_value2 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl2 = True

    elif exfl2:
        score_value2 -= 20
        break
    elif collision12 or collision13 or collision14 or collision15 or collision16:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl3 = True

    elif exfl3:
        score_value2 -= 20
        break
    elif playerY > 968:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl4 = True
    elif exfl4:
        break
    pygame.display.update()
# End of Player2 Round1

start_textX = 850
start_textY = 970
end_textX = 850
end_textY = 5
playerX = 370
playerY = 968
flag1_pl = True
flag1_mi = True
flag2_pl = False
flag2_mi = False
flag3_pl = False
flag3_mi = False
flag4_pl = False
flag4_mi = False
flag5_pl = False
flag5_mi = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False
fishX_change = 2
fish1X_change = 2
fish2X_change = 2
fish3X_change = 2
fish4X_change = 2
fish5X_change = 2
start12 = pygame.time.get_ticks()
time12 = 0
# Player1 Round2
while True:
    screen.fill(skyBlue)
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    stloop12 = pygame.time.get_ticks()
    time12 += (stloop12 - start12)
    time12 /= 1000
    time12 = round(time12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 2

    elif fishX >= 1790:
        fishX = 0


    fish1X += fish1X_change
    if fish1X <= 0:
        fish1X = 1790


    elif fish1X >= 1790:
            fish1X_change = -2

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 2

    elif fish2X >= 1790:
            fish2X_change = -2
    fish3X += fish3X_change
    if fish3X <= 0:
        fish3X = 1790


    elif fish3X >= 1790:
            fish3X_change = -2

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 2

    elif fish4X >= 1790:
            fish4X_change = -2
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 2

    elif fish5X >= 1790:
            fish5X_change = -2

    if flag1_pl:
        if playerY <= 810:
            score_value1 += 10
            flag1_pl = False
            flag1_mi = True
            flag2_pl = True

    if flag2_pl:
        if playerY <= 650:
            score_value1 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True

    if flag3_pl:
        if playerY <= 490:
            score_value1 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True

    if flag4_pl:
        if playerY <= 330:
            score_value1 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True

    if flag5_pl:
        if playerY <= 170:
            score_value1 += 10
            flag5_pl = False
            flag5_mi = True


    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)
    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2   Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl1 = True

    elif exfl1:
        score_value1 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl2 = True

    elif exfl2:
        score_value1 -= 20
        break
    elif collision12 or collision13 or collision14 or collision15 or collision16:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl3 = True

    elif exfl3:
        score_value1 -= 20
        break
    elif playerY < 40:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 2", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl4 = True
    elif exfl4:
        break
    pygame.display.update()
#End of Player1 Round2

start_textX = 850
start_textY = 5
end_textX = 850
end_textY = 970
playerX = 370
playerY = 0
flag1_pl = True
flag1_mi = True
flag2_pl = False
flag2_mi = False
flag3_pl = False
flag3_mi = False
flag4_pl = False
flag4_mi = False
flag5_pl = False
flag5_mi = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False
fishX_change = 2
fish1X_change = 2
fish2X_change = 2
fish3X_change = 2
fish4X_change = 2
fish5X_change = 2
start22 = pygame.time.get_ticks()
time22 = 0
#Player2 Round2
while True:
    screen.fill((152, 245, 255))
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    stloop22 = pygame.time.get_ticks()
    time22 += (stloop22 - start22)
    time22 /= 1000
    time22 = round(time22)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 2

    elif fishX >= 1790:
           fishX = 0
           #fishX_change = -1.5

    fish1X += fish1X_change
    if fish1X <= 0:
        fish1X = 1790
            #fish1X_change = 1.5

    elif fish1X >= 1790:
            fish1X_change = -2

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 2

    elif fish2X >= 1790:
            fish2X_change = -2
    fish3X += fish3X_change
    if fish3X <= 0:
        fish3X = 1790
            #fish3X_change = 1.5

    elif fish3X >= 1790:
            fish3X_change = -2

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 2

    elif fish4X >= 1790:
            fish4X_change = -2
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 2
    elif fish5X >= 1790:
            fish5X_change = -2

    if flag1_pl:
        if playerY >= 170:
            score_value2 += 10
            flag1_pl = False
            #flag1_mi = True
            flag2_pl = True


    if flag2_pl:
        if playerY >= 330:
            score_value2 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True

    if flag3_pl:
        if playerY >= 490:
            score_value2 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True


    if flag4_pl:
        if playerY >= 650:
            score_value2 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True


    if flag5_pl:
        if playerY >= 810:
            score_value2 += 10
            flag5_pl = False
            flag5_mi = True


    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)
    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1   Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl1 = True

    elif exfl1:
        score_value2 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl2 = True

    elif exfl2:
        score_value2 -= 20
        break
    elif collision12 or collision13 or collision14 or collision15 or collision16:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl3 = True

    elif exfl3:
        score_value2 -= 20
        break
    elif playerY > 968:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl4 = True
    elif exfl4:
        break
    pygame.display.update()
#End of Player2 Round2

start_textX = 850
start_textY = 970
end_textX = 850
end_textY = 5
playerX = 370
playerY = 968
flag1_pl = True
flag1_mi = True
flag2_pl = False
flag2_mi = False
flag3_pl = False
flag3_mi = False
flag4_pl = False
flag4_mi = False
flag5_pl = False
flag5_mi = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False
fishX_change = 2.5
fish1X_change = 2.5
fish2X_change = 2.5
fish3X_change = 2.5
fish4X_change = 2.5
fish5X_change = 2.5
start13 = pygame.time.get_ticks()
time13 = 0
#Player1 Round3
while True:
    screen.fill((152, 245, 255))
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    stloop13 = pygame.time.get_ticks()
    time13 += (stloop13 - start13)
    time13 /= 1000
    time13 = round(time13)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 2.5

    elif fishX >= 1790:
        fishX = 0
           #fishX_change = -2

    fish1X += fish1X_change
    if fish1X <= 0:
        fish1X = 1790
            #fish1X_change = 2

    elif fish1X >= 1790:
            fish1X_change = -2.5

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 2.5

    elif fish2X >= 1790:
            fish2X_change = -2.5
    fish3X += fish3X_change
    if fish3X <= 0:
        fish3X = 1790
            #fish3X_change = 2

    elif fish3X >= 1790:
            fish3X_change = -2.5

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 2.5

    elif fish4X >= 1790:
            fish4X_change = -2.5
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 2.5

    elif fish5X >= 1790:
            fish5X_change = -2.5

    if flag1_pl:
        if playerY <= 810:
            score_value1 += 10
            flag1_pl = False
            flag1_mi = True
            flag2_pl = True

    if flag2_pl:
        if playerY <= 650:
            score_value1 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True

    if flag3_pl:
        if playerY <= 490:
            score_value1 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True

    if flag4_pl:
        if playerY <= 330:
            score_value1 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True

    if flag5_pl:
        if playerY <= 170:
            score_value1 += 10
            flag5_pl = False
            flag5_mi = True



    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)
    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2   Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl1 = True

    elif exfl1:
        score_value1 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl2 = True

    elif exfl2:
        score_value1 -= 20
        break

    elif collision12 or collision13 or collision14 or collision15 or collision16:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl3 = True

    elif exfl3:
        score_value1 -= 20
        break

    elif playerY < 40:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 3", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl4 = True
    elif exfl4:
        break
    pygame.display.update()
#End of Player1 Round3

start_textX = 850
start_textY = 5
end_textX = 850
end_textY = 970
playerX = 370
playerY = 0
flag1_pl = True
flag1_mi = True
flag2_pl = False
flag2_mi = False
flag3_pl = False
flag3_mi = False
flag4_pl = False
flag4_mi = False
flag5_pl = False
flag5_mi = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False
fishX_change = 2.5
fish1X_change = 2.5
fish2X_change = 2.5
fish3X_change = 2.5
fish4X_change = 2.5
fish5X_change = 2.5

start23 = pygame.time.get_ticks()
time23 = 0
#Player2 Round3
while True:
    screen.fill(skyBlue)
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    stloop23 = pygame.time.get_ticks()
    time23 += (stloop23 - start23)
    time23 /= 1000
    time23 = round(time23)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 2.5

    elif fishX >= 1790:
        fishX = 0
           #fishX_change = -2

    fish1X += fish1X_change
    if fish1X <= 0:
        fish1X = 1790
            #fish1X_change = 2

    elif fish1X >= 1790:
            fish1X_change = -2.5

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 2.5

    elif fish2X >= 1790:
            fish2X_change = -2.5
    fish3X += fish3X_change
    if fish3X <= 0:
        fish3X = 1790
            #fish3X_change = 2

    elif fish3X >= 1790:
            fish3X_change = -2.5

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 2.5

    elif fish4X >= 1790:
            fish4X_change = -2.5
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 2.5

    elif fish5X >= 1790:
            fish5X_change = -2.5

    if flag1_pl:
        if playerY >= 170:
            score_value2 += 10
            flag1_pl = False
            flag1_mi = True
            flag2_pl = True


    if flag2_pl:
        if playerY >= 330:
            score_value2 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True

    if flag3_pl:
        if playerY >= 490:
            score_value2 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True


    if flag4_pl:
        if playerY >= 650:
            score_value2 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True


    if flag5_pl:
        if playerY >= 810:
            score_value2 += 10
            flag5_pl = False
            flag5_mi = True

    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)
    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1   Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl1 = True

    elif exfl1:
        score_value2 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl2 = True

    elif exfl2:
        score_value2 -= 20
        break
    elif collision12 or collision13 or collision14 or collision15 or collision16:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl3 = True

    elif exfl3:
        score_value2 -= 20
        break
    elif playerY > 968:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 1  Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl4 = True

    elif exfl4:
        break
    pygame.display.update()
#End of Player2 Round3

start_textX = 850
start_textY = 970
end_textX = 850
end_textY = 5
playerX = 370
playerY = 968
flag1_pl = True
flag1_mi = True
flag2_pl = False
flag2_mi = False
flag3_pl = False
flag3_mi = False
flag4_pl = False
flag4_mi = False
flag5_pl = False
flag5_mi = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False
fishX_change = 3
fish1X_change = 3
fish2X_change = 3
fish3X_change = 3
fish4X_change = 3
fish5X_change = 3
start14 = pygame.time.get_ticks()
time14 = 0
#Player1 Round4
while True:
    screen.fill(skyBlue)
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    stloop14 = pygame.time.get_ticks()
    time14 += (stloop14 - start14)
    time14 /= 1000
    time14 = round(time11)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 3

    elif fishX >= 1790:
        fishX = 0
           #fishX_change = -2

    fish1X += fish1X_change
    if fish1X <= 0:
        fish1X = 1790
            #fish1X_change = 2

    elif fish1X >= 1790:
            fish1X_change = -3

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 3

    elif fish2X >= 1790:
            fish2X_change = -3
    fish3X += fish3X_change
    if fish3X <= 0:
        fish3X = 1790
            #fish3X_change = 2

    elif fish3X >= 1790:
            fish3X_change = -3

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 3

    elif fish4X >= 1790:
            fish4X_change = -3
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 3

    elif fish5X >= 1790:
            fish5X_change = -3

    if flag1_pl:
        if playerY <= 810:
            score_value1 += 10
            flag1_pl = False
            flag1_mi = True
            flag2_pl = True

    if flag2_pl:
        if playerY <= 650:
            score_value1 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True

    if flag3_pl:
        if playerY <= 490:
            score_value1 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True

    if flag4_pl:
        if playerY <= 330:
            score_value1 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True

    if flag5_pl:
        if playerY <= 170:
            score_value1 += 10
            flag5_pl = False
            flag5_mi = True



    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)

    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2   Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl1 = True

    elif exfl1:
        score_value1 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl2 = True

    elif exfl2:
        score_value1 -= 20
        break
    elif collision12 or collision13 or collision14 or collision15 or collision16:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl3 = True

    elif exfl3:
        score_value1 -= 20
        break
    elif playerY < 40:
        for i in range (5):
            screen.fill((152, 245, 255))
            round1 = font.render("Player 2  Round 4", True, (0, 0, 0))
            screen.blit(round1, (700, 500))
            exfl4 = True
    elif exfl4:
        break
    pygame.display.update()
#End of Player1 Round4

start_textX = 850
start_textY = 5
end_textX = 850
end_textY = 970
playerX = 370
playerY = 0
flag1_pl = True
flag2_pl = False
flag3_pl = False
flag4_pl = False
flag5_pl = False
exfl1 = False
exfl2 = False
exfl3 = False
exfl4 = False
fishX_change = 3
fish1X_change = 3
fish2X_change = 3
fish3X_change = 3
fish4X_change = 3
fish5X_change = 3

start24 = pygame.time.get_ticks()
time24 = 0

#Player2 Round4
while True:
    screen.fill(skyBlue)
    pygame.draw.line(screen, brown, (0, 0), (1854, 0), 64)
    pygame.draw.line(screen, brown, (0, 170), (1854, 170), 30)
    pygame.draw.line(screen, brown, (0, 330), (1854, 330), 30)
    pygame.draw.line(screen, brown, (0, 490), (1854, 490), 30)
    pygame.draw.line(screen, brown, (0, 650), (1854, 650), 30)
    pygame.draw.line(screen, brown, (0, 810), (1854, 810), 30)
    pygame.draw.line(screen, brown, (0, 990), (1854, 990), 30)
    stloop24 = pygame.time.get_ticks()
    time24 += (stloop24 - start24)
    time24 /= 1000
    time24 = round(time24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #setting boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 1822:
            playerX = 1822
        if playerY <= 0:
            playerY = 0
        elif playerY >= 968:
            playerY = 968
        # if key stroke is pressed check whether it is left,right,up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                    playerY_change = 5
            if event.key == pygame.K_RIGHT:
                    playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    fishX += fishX_change
    if fishX <= 0:
            fishX_change = 3

    elif fishX >= 1790:
        fishX = 0
           #fishX_change = -2

    fish1X += fish1X_change
    if fish1X <= 0:
        fish1X = 1790
            #fish1X_change = 2

    elif fish1X >= 1790:
            fish1X_change = -3

    fish2X += fish2X_change
    if fish2X <= 0:
            fish2X_change = 3

    elif fish2X >= 1790:
            fish2X_change = -3
    fish3X += fish3X_change
    if fish3X <= 0:
        fish3X = 1790
            #fish3X_change = 2

    elif fish3X >= 1790:
            fish3X_change = -3

    fish4X += fish4X_change
    if fish4X <= 0:
            fish4X_change = 3

    elif fish4X >= 1790:
            fish4X_change = -3
    fish5X += fish5X_change
    if fish5X <= 0:
            fish5X_change = 3

    elif fish5X >= 1790:
            fish5X_change = -3

    if flag1_pl:
        if playerY >= 170:
            score_value2 += 10
            flag1_pl = False
            flag1_mi = True
            flag2_pl = True


    if flag2_pl:
        if playerY >= 330:
            score_value2 += 10
            flag2_pl = False
            flag2_mi = True
            flag3_pl = True

    if flag3_pl:
        if playerY >= 490:
            score_value2 += 10
            flag3_pl = False
            flag3_mi = True
            flag4_pl = True


    if flag4_pl:
        if playerY >= 650:
            score_value2 += 10
            flag4_pl = False
            flag4_mi = True
            flag5_pl = True


    if flag5_pl:
        if playerY >= 810:
            score_value2 += 10
            flag5_pl = False
            flag5_mi = True


    collision = isCollision(fishX, fishY, playerX, playerY)
    collision1 = isCollision(fish1X, fish1Y, playerX, playerY)
    collision2 = isCollision(fish2X, fish2Y, playerX, playerY)
    collision3 = isCollision(fish3X, fish3Y, playerX, playerY)
    collision4 = isCollision(fish4X, fish4Y, playerX, playerY)
    collision5 = isCollision(fish5X, fish5Y, playerX, playerY)
    collision6 = isCollision(treeX, treeY, playerX, playerY)
    collision7 = isCollision(tree1X, tree1Y, playerX, playerY)
    collision8 = isCollision(tree2X, tree2Y, playerX, playerY)
    collision9 = isCollision(tree3X, tree3Y, playerX, playerY)
    collision10 = isCollision(tree4X, tree4Y, playerX, playerY)
    collision11 = isCollision(tree5X, tree5Y, playerX, playerY)
    collision12 = isCollision(tree6X, tree6Y, playerX, playerY)
    collision13 = isCollision(tree7X, tree7Y, playerX, playerY)
    collision14 = isCollision(tree8X, tree8Y, playerX, playerY)
    collision15 = isCollision(tree9X, tree9Y, playerX, playerY)
    collision16 = isCollision(tree10X, tree10Y, playerX, playerY)

    fish1(fish1X, fish1Y)
    fish5(fish5X, fish5Y)
    fish(fishX, fishY)
    fish2(fish2X, fish2Y)
    fish3(fish3X, fish3Y)
    fish4(fish4X, fish4Y)
    tree(treeX, treeY)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    tree3(tree3X, tree3Y)
    tree4(tree4X, tree4Y)
    tree5(tree5X, tree5Y)
    tree6(tree6X, tree6Y)
    tree7(tree7X, tree7Y)
    tree8(tree8X, tree8Y)
    tree9(tree9X, tree9Y)
    tree10(tree10X,tree10Y)
    show_score1(score_text1X, score_text1Y)
    show_score2(score_text2X, score_text2Y)
    player(playerX, playerY)
    start(start_textX, start_textY)
    end(end_textX, end_textY)
    time_total1 = time11 + time12 + time13 + time14
    time_total2 = time21 + time22 + time23 + time24
    if collision or collision1 or collision2 or collision3 or collision4 or collision5:
     exfl1 = True

    elif exfl1:
        score_value2 -= 20
        break
    elif collision6 or collision7 or collision8 or collision9 or collision10 or collision11:
        exfl2 = True

    elif exfl2:
        score_value2 -= 20
        break
    elif collision12 or collision13 or collision14 or collision15 or collision16:
        exfl3 = True

    elif exfl3:
        score_value2 -= 20
        break
    elif playerY > 968:
            exfl4 = True

    elif exfl4:
        break
    pygame.display.update()
#End of Player2 Round4

flag1 = True
flag2 = True

while True:
    screen.fill(skyBlue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    time_total1 = time11 + time12 + time13 + time14
    time_total2 = time21 + time22 + time23 + time24
    if flag1:
        score_value1 -= time_total1
        flag1 = False

    if flag2:
        score_value2 -= time_total2
        flag2 = False

    if score_value1 > score_value2:
                round1 = font.render("Winner : Player 1", True, (0, 0, 0))
                screen.blit(round1, (710, 500))
    elif score_value1 < score_value2:
                round1 = font.render("Winner : Player 2", True, (0, 0, 0))
                screen.blit(round1, (710, 500))
    else:
        round1 = font.render("This is a tie", True, (0, 0, 0))
        screen.blit(round1, (710, 500))

    pygame.display.update()



