import pygame
import math
def game_loop():
    lost = 0
    clock = pygame.time.Clock()

    pygame.init()

    fps=10

    velocity= 0
    velocity_change = 0
    bulletX_change=0
    bulletY_change=0
    velocity2= 0
    velocity2_change = 0
    bullet2X_change=0
    bullet2Y_change=0

    time = 1

    white=(255,255,255)
    black=(0,0,0)
    red = (255,0,0)
    light_red = (200,0,0)

    display_width=1000
    display_height=600

    tankcircleradius=20
    bulletradius=5
    tankwidth=100
    tankheight=50
    aimerwidth=5

    flightX = 0
    flightY = 0

    flight2X = 0
    flight2Y = 0

    tankX=900
    tankY=500
    tankX_change=0
    tankY_change=0
    movelength = 10


    tank2X=100
    tank2Y=500
    tank2X_change=0
    tank2Y_change=0


    aimerchoice=0
    aimerchoice_change=0
    aimerlength = 50

    aimerchoice2=0
    aimerchoice2_change=0

    lifeX = 850
    lifeY = 100
    life_width = 50
    life_height = 20
    life_widthchange = 0

    life2X = 50
    life2Y = 100
    life2_width = 50
    life2_height = 20
    life2_widthchange = 0

    smallfont = pygame.font.SysFont("comicsansms",25)
    medfont = pygame.font.SysFont("comicsansms",50)
    largefont = pygame.font.SysFont("comicsansms",80)

    def text_objects(text,color,size):
        if size == "small":
             textsurface = smallfont.render(text,True,color)
        if size == "medium":
             textsurface = medfont.render(text,True,color)
        if size == "large":
             textsurface = largefont.render(text,True,color)
        return textsurface, textsurface.get_rect()
        
    def message_to_screen(msg,color,y_displace,x_displace,size = "small"):
        textsurf, textrect = text_objects(msg,color,size)
        textrect.center = (display_width/2)+x_displace,(display_height/2)+y_displace
        display.blit(textsurf,textrect)

    def text_to_button(msg,color,buttonX,buttonY,buttonwidth,buttonheight,size="small"):
         textsurf, textrect = text_objects(msg,color,size)
         textrect.center = buttonX+(buttonwidth/2),buttonY+(buttonheight/2)              
         display.blit(textsurf,textrect)

    def rad_angle(a):
        return a*math.pi/180

    possibleaimer=[rad_angle(30),
                   rad_angle(45),
                   rad_angle(60),
                   rad_angle(75),
                   rad_angle(90)]

    aimerX= float(tankX - aimerlength * math.sin(possibleaimer[aimerchoice]))
    aimerY= float(tankY - aimerlength * math.cos(possibleaimer[aimerchoice]))
    aimer2X= float(tank2X + aimerlength * math.sin(possibleaimer[aimerchoice2]))
    aimer2Y= float(tank2Y - aimerlength * math.cos(possibleaimer[aimerchoice2]))

    bulletX = aimerX
    bulletY = aimerY
    bullet2X = aimer2X
    bullet2Y = aimer2Y

    def tank(x,y,aimerchoice,aimerx,aimery):
        
        pygame.draw.circle(display,black,[x,y],tankcircleradius)
        pygame.draw.rect(display,black,[x-50,y,tankwidth,tankheight])
        pygame.draw.line(display,black,[x,y],[aimerx,aimery],aimerwidth)



    def fire(bulletx , bullety, aimerx,v,x,y,aimerchoicek,aimery):
            
                            
        fire =True
        while fire == True:
            
            if x==tankX:
                bulletx -= int(6 - (6-(aimerchoicek+2)))**2
                bullety += int((((aimerx - bulletx)/(v+100))**2) - ((6-(aimerchoicek+2)) + (6-(aimerchoicek+2)) /(7 - (6-(aimerchoicek+2))))) 
                display.fill(white)
                tank(x,y,aimerchoicek,aimerx,aimery)
                tank(tank2X,tank2Y,aimerchoice2,aimer2X,aimer2Y)
                pygame.draw.circle(display,red,[int(bulletx),int(bullety)],bulletradius)
                pygame.draw.rect(display,black,[475,450,50,display_height-440])
                message_to_screen("velocity= %s "%(str(velocity)),black,-250,300,"small")
                message_to_screen("velocity= %s "%(str(velocity2)),black,-250,-300,"small")
                pygame.draw.rect(display,red,[lifeX,lifeY,life_width,life_height])
                pygame.draw.rect(display,red,[life2X,life2Y,life2_width,life2_height])
                pygame.display.update()
                clock.tick(100)
                if bullety >= display_height:
                       fire = False
                if bulletx < 525 and bulletx > 475 and bullety > 450:
                       fire = False
                if bulletx > tank2X - tankwidth/2 and bulletx < tank2X + tankwidth/2 and bullety > tank2Y + tankcircleradius:
                       fire = False           
                       x = 0
                       return x;
                
            if x==tank2X:
                bulletx += int(6 - (6-(aimerchoicek+2)))**2
                bullety += int((((aimerx - bulletx)/(v+100))**2) - ((6-(aimerchoicek+2)) + (6-(aimerchoicek+2)) /(7 - (6-(aimerchoicek+2))))) 
                display.fill(white)
                tank(x,y,aimerchoicek,aimerx,aimery)
                tank(tankX,tankY,aimerchoice,aimerX,aimerY)
                pygame.draw.circle(display,red,[int(bulletx),int(bullety)],bulletradius)
                pygame.draw.rect(display,black,[475,450,50,display_height-440])
                message_to_screen("velocity= %s "%(str(velocity)),black,-250,300,"small")
                message_to_screen("velocity= %s "%(str(velocity2)),black,-250,-300,"small")
                pygame.draw.rect(display,red,[lifeX,lifeY,life_width,life_height])
                pygame.draw.rect(display,red,[life2X,life2Y,life2_width,life2_height])
                pygame.display.update()
                clock.tick(100)
                if bullety >= display_height:
                       fire = False
                if bulletx < 525 and bulletx > 475 and bullety > 450:
                       fire = False
                if bulletx > tankX - tankwidth/2 and bulletx < tankX + tankwidth/2 and bullety > tankY + tankcircleradius:
                       fire = False           
                       x = 0
                       return x;
    gameexit=False
    gameover=False
    gamemenu=True
    gamecontrols = False

    def pause():
        pause = True
        while pause:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            display.fill(white)
            message_to_screen("""PAUSED""",red,0,0,size="medium")
            tank(tankX,tankY,aimerchoice,aimerX,aimerY)
            tank(tank2X,tank2Y,aimerchoice2,aimer2X,aimer2Y)
            pygame.draw.rect(display,black,[475,450,50,display_height-440])
            pygame.draw.rect(display,red,[lifeX,lifeY,life_width,life_height])
            pygame.draw.rect(display,red,[life2X,life2Y,life2_width,life2_height])
            
            if button("play",10,200,100,50,red,light_red,action= "play")== False:
                pause= False
                
            pygame.display.update()

            
       
    def button(text,x,y,width,height,inactivecolor,activecolor,action=None):
        
        cur=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(display,activecolor,(x,y,width,height))
            if click[0] == 1 and action != None:
                if action == "quit":
                    pygame.quit()
                elif action == "play":
                    gameexit = False
                    gamemenu = False
                elif action == "controls":
                    gamemenu = False
                    gameexit = False
                return gamemenu   
                    
                
        else:
            pygame.draw.rect(display,inactivecolor,(x,y,width,height))
        text_to_button(text,black,x,y,width,height)

    display = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('tank')
    
    while not gameexit:

        while gamemenu:

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    gamemenu = False
                    gameexit = True
                else:
                    break
                
            
            display.fill(white)
            message_to_screen("""WELCOME TO TANK GAME""",red,-50,0,size="medium")
            message_to_screen("""This is a 2 player game.""",black,0,0,size="small")
            message_to_screen("""your aim is to destroy your opponent!""",black,50,0,size="small")
            
            
            if button("play",100,500,100,50,red,light_red,action="play") == False:
                gamemenu = False
            
            
            if button("controls",450,500,100,50,red,light_red,action="controls")== False:
                gamecontrols = True
                gamemenu = False
                
            button("quit",800,500,100,50,red,light_red,action="quit")

            pygame.display.update()

        while gamecontrols:

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    gamemenu = False
                    gameexit = True
                
            display.fill(white)
            message_to_screen("Player Left",black,-200,-300,size="medium")
            message_to_screen("Move Left : A",red,-150,-300,size="small")
            message_to_screen("Move Right : D",red,-100,-300,size="small")
            message_to_screen("Turret angle increase : W",red,-50,-300,size="small")
            message_to_screen("Turret angle decrease : S",red,0,-300,size="small")
            message_to_screen("Velocity increase : hold Q ",red,50,-300,size="small")
            message_to_screen("FIRE : release Q ",red,100,-300,size="small")

            message_to_screen("Player right",black,-200,300,size="medium")
            message_to_screen("Move Left : LEFT",red,-150,300,size="small")
            message_to_screen("Move Right : RIGHT",red,-100,300,size="small")
            message_to_screen("Turret angle increase : UP",red,-50,300,size="small")
            message_to_screen("Turret angle decrease : DOWN",red,0,300,size="small")
            message_to_screen("Velocity increase : hold SPACEBAR ",red,50,300,size="small")
            message_to_screen("FIRE : release SPACEBAR ",red,100,300,size="small")

            if button("play",100,500,100,50,red,light_red,action="play") == False:
                gamecontrols = False
            button("quit",800,500,100,50,red,light_red,action="quit")
            
            pygame.display.update()
                
                        
            
        while gameover == True:
            display.fill(white)
            message_to_screen("%s wins"%(lost),black,0,0,size="medium")
            message_to_screen("press C to play again or Q to quit",black,100,0,size="medium")
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if button("play again",100,500,200,50,red,light_red,action="play") == False:
                game_loop()
            button("quit",800,500,100,50,red,light_red,action="quit")
            pygame.display.update()        
            

        bulletX = aimerX
        bulletY = aimerY
        bullet2X = aimer2X
        bullet2Y = aimer2Y


        possibleaimer=[rad_angle(30),
                   rad_angle(45),
                   rad_angle(60),
                   rad_angle(75),
                   rad_angle(90)]

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        tankX_change = 0
                    elif event.key == pygame.K_RIGHT:
                        tankX_change = 0
                    elif event.key == pygame.K_UP:
                        aimerchoice_change = 0
                    elif event.key == pygame.K_DOWN:
                        aimerchoice_change = 0
                    elif event.key == pygame.K_SPACE:
                        v=velocity
                        if fire(bulletX , bulletY, aimerX,v,tankX,tankY,aimerchoice,aimerY) == 0:
                            life2_width-=10
                        velocity = 0
                        velocity_change = 0
                    elif event.key == pygame.K_a:
                        tank2X_change = 0
                    elif event.key == pygame.K_d:
                        tank2X_change = 0
                    elif event.key == pygame.K_w:
                        aimerchoice2_change = 0
                    elif event.key == pygame.K_s:
                        aimerchoice2_change = 0
                    elif event.key == pygame.K_q:
                        v2=velocity2
                        if fire(bullet2X , bullet2Y, aimer2X,v2,tank2X,tank2Y,aimerchoice2,aimer2Y) == 0:
                            life_width-=10
                        velocity2 = 0
                        velocity2_change = 0
                        life_widthchange = 10
                        
                         
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        tankX_change = -movelength
                    elif event.key == pygame.K_RIGHT:
                        tankX_change = movelength
                    elif event.key == pygame.K_UP:
                        aimerchoice_change = -1
                    elif event.key == pygame.K_DOWN:
                        aimerchoice_change = 1
                    elif event.key == pygame.K_SPACE:
                        velocity_change += 5
                    elif event.key == pygame.K_a:
                        tank2X_change = -movelength
                    elif event.key == pygame.K_d:
                        tank2X_change = movelength
                    elif event.key == pygame.K_w:
                        aimerchoice2_change = -1
                    elif event.key == pygame.K_s:
                        aimerchoice2_change = 1
                    elif event.key == pygame.K_q:
                        velocity2_change += 5
                        
        velocity += velocity_change
        velocity2 += velocity2_change
        message_to_screen("velocity= %s "%(str(velocity)),black,-250,300,"small")
        message_to_screen("velocity= %s "%(str(velocity2)),black,-250,-300,"small")
        pygame.display.update()
        clock.tick(200)
        
        tankX += tankX_change
        tank2X += tank2X_change
        
                    
        aimerchoice += aimerchoice_change
        if aimerchoice > 4:
            aimerchoice=0
        if aimerchoice < 0:
            aimerchoice=4
        aimerchoice2 += aimerchoice2_change
        if aimerchoice2 > 4:
            aimerchoice2=0
        if aimerchoice2 < 0:
            aimerchoice2=4
            
        aimerX=tankX - aimerlength * math.sin(possibleaimer[aimerchoice])
        aimerY=tankY - aimerlength * math.cos(possibleaimer[aimerchoice])
        aimer2X=tank2X + aimerlength * math.sin(possibleaimer[aimerchoice2])
        aimer2Y=tank2Y - aimerlength * math.cos(possibleaimer[aimerchoice2])
        
        
       
        display.fill(white)

        tank(tankX,tankY,aimerchoice,aimerX,aimerY)
        tank(tank2X,tank2Y,aimerchoice2,aimer2X,aimer2Y)
        pygame.draw.rect(display,black,[475,450,50,display_height-440])
        pygame.draw.rect(display,red,[lifeX,lifeY,life_width,life_height])
        pygame.draw.rect(display,red,[life2X,life2Y,life2_width,life2_height])
        message_to_screen("velocity= %s "%(str(velocity)),black,-250,300,"small")
        message_to_screen("velocity= %s "%(str(velocity2)),black,-250,-300,"small")
        if button("pause",200,200,100,50,red,light_red,action= "play")== False:
            pause()
      
        
        clock.tick(fps)
        pygame.display.update()

        if life_width <= 0 :
            lost = "player LEFT"
            gameover = True
        if life2_width <= 0 :
            lost = "player RIGHT"
            gameover = True

    pygame.quit()
    quit()
game_loop()
