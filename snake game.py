import pygame
import random

pygame.init()

savedpos = []
savedpos2 = []

myfont = pygame.font.SysFont('Arial', 30)

textsurface = myfont.render('Some Text', False, (255, 0, 0))

score = 0

foodlocx = (random.randint(0, 25)*20)
foodlocy = (random.randint(0, 25)*20)

win = pygame.display.set_mode((520,520))

pygame.display.set_caption("Snake Game by Sammy T.")

x = 240
y = 240
width = 20
height = 20
vel = 20

up = False
down = False
left = False
right = True

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left = True
        right = False
        up = False
        down = False

    if keys[pygame.K_RIGHT]:
        left = False
        right = True
        up = False
        down = False

    if keys[pygame.K_UP]:
        left = False
        right = False
        up = True
        down = False

    if keys[pygame.K_DOWN]:
        left = False
        right = False
        up = False
        down = True

    savedpos.append((x,y))

    if score == 1:
        savedpos2.append((x,y))
        if (len(savedpos2)-1) > score:
            del savedpos2[0]
            

    if (len(savedpos)) > score:
        del savedpos[0]

    if left:
        x -= vel

    if right:
        x += vel

    if up:
        y -= vel

    if down:
        y += vel
    win.fill((0,0,0))
    if (x > 500) or (x < 0) or (y > 500) or (y < 0):
        textsurface = myfont.render('YOU HIT THE WALL! SCORE: ' + str(score), False, (255, 0, 0))
        win.fill((0,0,0))
        win.blit(textsurface,(70,250))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
    
    if (foodlocx == x) and (foodlocy == y):
        score += 1
        foodlocx = (random.randint(0, 25)*20)
        foodlocy = (random.randint(0, 25)*20)

    for i in savedpos:
        pygame.draw.rect(win, (200, 200, 200), (i[0], i[1], width, height))
        if (i[0] == x) and (i[1] == y):
            textsurface = myfont.render('YOU HIT YOUR TAIL! SCORE: ' + str(score), False, (255, 0, 0))
            win.fill((0,0,0))
            win.blit(textsurface,(70,250))
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
    if score == 1:
        for i in savedpos2:
            if (i[0] == x) and (i[1] == y):
                textsurface = myfont.render('YOU HIT YOUR TAIL! SCORE: ' + str(score), False, (255, 0, 0))
                win.fill((0,0,0))
                win.blit(textsurface,(70,250))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()

    pygame.draw.rect(win, (255, 0, 0), (foodlocx, foodlocy, width, height))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
