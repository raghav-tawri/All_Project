import pygame
import random

pygame.init()

#coloursssssssssssssss
wite=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)

rwidth=1200
rheight=600

root=pygame.display.set_mode((rwidth,rheight))
pygame.display.set_caption("MY FIRST SNAKE GAME")

#varibles
egame=False
gover=False

#snakepogesion
snakex=45
snakey=55

#snake velocity
vsnakex=0
vsnakey=0

#food of snake by cordinates
fsnakex=random.randint(20,rwidth/2)
fsnakey=random.randint(20,rheight/2)

#snakesize
snakesize=10
#clock or time per frame functions
fps=60
clock=pygame.time.Clock()

#points
score=0

font=pygame.font.SysFont(None,55)

def textscore(text,color,x,y):
    screentext=font.render(text,True,color)
    root.blit(screentext,[x,y])

def  plotsnake(root,color,slist,snakesize):
    for x,y  in slist:
      pygame.draw.rect(root,color,[x,y,snakesize,snakesize])


slist=[]
slenght=1
#game looppppppppppppppppp
while not egame:
    if egame:
        root.fill(red)
        textscore("game over",red,rwidth/2,rheight/2)

    for event in pygame.event.get():
         #print(event)
         #quit function

          if event.type==pygame.QUIT:
             egame=True
            #player moving function
          if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_RIGHT:
                vsnakex=vsnakex + 5  #for increasing in one tap by fix velocity
                vsnakey=0            #for not moving in diangular
                print ('RIGHT')       #right moving function
             if event.key==pygame.K_LEFT:
                vsnakex=vsnakex - 5
                vsnakey=0
                print ('LEFT')        # left moving function
             if event.key == pygame.K_UP:
                vsnakey = vsnakey - 5
                vsnakex=0
                print ('UP')        # up moving function
             if event.key == pygame.K_DOWN:
                vsnakey = vsnakey + 5
                vsnakex=0
                print ('DOWN')     # down moving function


    snakex=snakex+vsnakex
    snakey=snakey+vsnakey
    # scoring function
    if abs(snakex - fsnakex) < 6 and abs(snakey - fsnakey) < 6:
           score += 1
           print ("scour=", score)
           fsnakex = random.randint(20, rwidth / 2)
           fsnakey = random.randint(20, rheight / 2)
           slenght+=5
#colour function
    #root.fill(black)
#score printing
    textscore("score:  "+str(score*10),red,5,5)
 #lenght maker
    head=[]
    head.append(snakex)
    head.append(snakey)
    slist.append(head)
#lenght checker
    if len(slist)>slenght:
        del slist[0]
    if snakex<0 or snakex>rwidth or snakey<0 or snakey>rheight:
        gover=True
        print("game over")
#snake building
    pygame.draw.rect(root,blue,(snakex,snakey,snakesize,snakesize))#snake
    pygame.draw.rect(root, red,( fsnakex, fsnakey,snakesize,snakesize))#food
    plotsnake(root,wite,slist,snakesize)
#main window updating function
    pygame.display.update()
#clock tick function
    clock.tick(fps)

pygame.quit()
quit()
