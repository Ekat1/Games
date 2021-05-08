#make sure to install pygame before running this. To do so on windows 10, open command prompt and type "py -m pip install pygame"
import pygame
#initial variables
x = 500
y = 500
xvel = 0
yvel = 0
speed = 8
jump_height = 15
platforms = []
ground = False
window = pygame.display.set_mode((1500, 1000))
#Set platform generation
platforms.append((0,750,1500,250))
platforms.append((1300,700,200,50))
platforms.append((1000,640,200,50))

                     
run = True
#Main game loop
while run:
    window.fill((255,255,255)) #window color
    pygame.draw.rect(window,(175, 0, 255),(x,y,50,50)) #draw player
    
    #keyboard input system for player movement. Arrow keys to move
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #Changing y and x velocity instead of just y and x to add momentum and gravity
    if keys[pygame.K_LEFT]:
        if xvel >= -10:
            xvel -= speed
        if xvel < -10:
            xvel = -10
    if keys[pygame.K_RIGHT]:
        if xvel <= 10:
            xvel += speed
        if xvel > 10:
            xvel = 10
    if keys[pygame.K_UP]:
        if ground == True:
            yvel = jump_height * -1
    
    #Platform hitboxes(currently not functional under platforms)

    for platform in platforms:
        pygame.draw.rect(window,(0, 0, 0),(platform[0],platform[1],platform[2],platform[3]))
        #top and bottom hitbox
        if x + xvel > platform[0] - 50:
            if x + xvel < platform[0] + platform[2]:
                if y <= platform[1] - 50:
                    if y + yvel >= platform[1] - 50:
                        ground = True
                        y = platform[1] - 50
                        yvel = 0
                    else:
                        ground = False
            
                if y >= platform[1] + platform[3]:
                    if y + yvel < platform[1] + platform[3]:
                        y  = platform[1] + platform[3]
                        yvel = 0

        #side hitboxes

        if y > platform[1] - 50:
            if y < platform[1] + platform[3]:
                if x + 50 <= platform[0]:
                    if x + 50 + xvel > platform[0]:
                        xvel = 0
                        x = platform[0] - 50        
                if x >= platform[0] + platform[2]:
                    if x + xvel < platform[0] + platform[2]:
                        xvel = 0
                        x = platform[0] + platform[2]
    
    #Gravity, momemtum, friction, and movement

    if xvel < 0:
        xvel += 1
    if xvel > 0:
        xvel -= 1

    if ground == False:
        yvel += 1
    y += yvel
    x += xvel
    
    pygame.display.update() #Update display
            
    pygame.time.delay(30) #Tick delay

pygame.quit() #Closes window when loop is borken by hitting the exit button
