import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0, 0,0)
red=(255,0,0)

clock = pygame.time.Clock()
blocksize=10
display_width=800
display_height=600
fps=10


smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)


def snake(blocksize,snakelist):
    for xy in snakelist:
        pygame.draw.rect(display, black, [xy[0],xy[1],blocksize,blocksize])

def text_objects(text,color,size):
    if size == "small":
         textsurface = smallfont.render(text,True,color)
    if size == "medium":
         textsurface = medfont.render(text,True,color)
    if size == "large":
         textsurface = largefont.render(text,True,color)
    return textsurface, textsurface.get_rect()
        
def message_to_screen(msg,color,y_displace,size = "small"):
    textsurf, textrect = text_objects(msg,color,size)
    #screen_text = font.render(msg,True,color)
    #display.blit(screen_text,[display_width/2-100,display_height/2])
    textrect.center = (display_width/2),(display_height/2)+y_displace
    display.blit(textsurf,textrect)

display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake')


def game_loop():
    score = 0
    gameexit = False
    gameover = False
    
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change= 0
    lead_y_change= 0

    snakelist = []
    snakelength=1

    randappleX=round(random.randrange(0 , display_width-blocksize)/10.0)*10.0
    randappleY=round(random.randrange(0 , display_height-blocksize)/10.0)*10.0
    
    while not gameexit:
        
        while gameover == True:
            display.fill(white)
            message_to_screen("Game Over!",red,-50,size="large")
            message_to_screen("press C to play again or Q to quit",black,50,size="medium")
            message_to_screen("Score = %s"%(str(score)),black,100,size="small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                    if event.key == pygame.K_c:
                        game_loop()
                 
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -blocksize
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = blocksize
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -blocksize
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = blocksize
                    lead_x_change = 0

        if lead_x >= display_width or lead_x <= 0 or lead_y >=display_height or lead_y <=0:
            print(score)
            gameover=True
            
        lead_x += lead_x_change
        lead_y += lead_y_change        
        display.fill(white)
        pygame.draw.rect(display, red, [randappleX,randappleY,blocksize,blocksize])

        
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                print(score)
                gameover=True
        
        snake(blocksize,snakelist)
        pygame.display.update()

        if lead_x == randappleX and lead_y == randappleY:
            randappleX=round(random.randrange(0 , display_width-blocksize)/10.0)*10.0
            randappleY=round(random.randrange(0 , display_height-blocksize)/10.0)*10.0
            snakelength+=1
            score +=1
            
        clock.tick(fps)

    pygame.quit()
    quit()
game_loop()

