#Main game loop
platforms = []

class system:

    def build_platform(x,y,width,height,level):
        platforms.append((x,y,width,height,level))
        
    
    def main(x,y,speed,jump_height,windowx,windowy,level_num):
        import pygame
        startx = x
        starty = y
        level = 1
        xvel = 0
        yvel = 0
        ground = False
        window = pygame.display.set_mode((windowx, windowy))
        player = pygame.image.load('player.png')
        top = pygame.image.load('top.png')
        groundtex = pygame.image.load('ground.png')
        run = True
        while run:
            window.fill((255,255,255)) #window color#draw player
            window.blit(player, (x, y))
    
            #keyboard input system for player movement. Arrow keys to move
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            #Changing y and x velocity instead of just y and x to add momentum and gravity
            if keys[pygame.K_LEFT]:
                if xvel >= speed * -1:
                    xvel -= 2
                if xvel < -10:
                    xvel = -10
            if keys[pygame.K_RIGHT]:
                if xvel <= speed:
                    xvel += 2
                if xvel > 10:
                    xvel = 10
            if keys[pygame.K_UP]:
                if ground == True:
                    yvel = jump_height * -1
    
            #Platform hitboxes

            for platform in platforms:
                if platform[4] == level:
                    repeat = int(platform[2] / 50)
                    repeaty = int(platform[3] / 50)
                    start = platform[0]
                    startdwn = platform[1]
                    for i in range(repeaty):
                        for i in range(repeat):
                            window.blit(groundtex, (start, startdwn))
                            start += 50
                        cropground = pygame.Surface(((platform[2] - (repeat * 50)), 50))
                        cropground.blit(groundtex, (0, 0), (0, 0, (platform[2] - (repeat * 50)), 50))
                        window.blit(cropground, (start, startdwn))
                        startdwn += 50
                        start = platform[0]
                    cropgrounddwn = pygame.Surface((platform[2], (platform[3] - (repeaty * 50))))
                    start = 0
                    for i in range(repeat):
                        cropgrounddwn.blit(groundtex, (start, 0))
                        start += 50
                    window.blit(cropgrounddwn, (platform[0], startdwn))

                        
                    start = platform[0]
                    for i in range(repeat):
                        window.blit(top, (start, platform[1]))
                        start += 50
                    croptop = pygame.Surface(((platform[2] - (repeat * 50)), 50), pygame.SRCALPHA)
                    croptop.blit(top, (0, 0), (0, 0, (platform[2] - (repeat * 50)), 50))
                    window.blit(croptop, (start, platform[1]))
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

                        else:
                            ground = False

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

            if x + 50 + xvel > windowx:
                if level < level_num:
                    x = windowx - 50
                    xvel = 0
                    pygame.time.delay(90)
                    level += 1
                    x = startx
                    y = starty
                elif level >= level_num:
                    x = windowx - 50
                    xvel = 0

            if x + xvel < 0:
                x = 0
                xvel = 0

            if y > windowy:
                x = startx
                y = starty
                    
    
            #Gravity, momemtum, friction, and movement

            if xvel < 0:
                xvel += 1
            if xvel > 0:
                xvel -= 1
    
            if ground == False:
                if yvel < 20:
                    yvel += 1
            y += yvel
            x += xvel

        
            pygame.display.update() #Update display
            
            pygame.time.delay(30) #Tick delay

        pygame.quit() #Closes window when loop is borken by hitting the exit button
