import pygame
import random
import os

pygame.mixer.init()
pygame.mixer.music.load("fly.mp3")
pygame.mixer.music.play()

pygame.init()

#coloursssssssssssssss
wite=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
cyan=(0,255,255)
grey=(233,210,229)

rwidth=1200
rheight=600

root=pygame.display.set_mode((rwidth,rheight))
pygame.display.set_caption("MY FIRST SNAKE GAME")


clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)



def textscore(text,color,x,y):
    screentext=font.render(text,True,color)
    root.blit(screentext,[x,y])

def  plotsnake(root,color,slist,snakesize):
    for x,y  in slist:
      pygame.draw.rect(root,color,[x,y,snakesize,snakesize])

def welcome():
    egame=False
    while not egame:
        root.fill((grey))
        textscore("welcome to snakes",blue,400,270)
        textscore("press space for start game",green,325,370)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                egame=True
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_SPACE:
                  gameloop()
        pygame.display.update()
        clock.tick(60)

#game looppppppppppppppppp
def gameloop():
    # varibles
    egame = False
    gover = False

    # snakepogesion
    snakex = 45
    snakey = 55

    # points
    score = 0

    # snake velocity
    vsnakex = 0
    vsnakey = 0

    #inc lenght
    slist = []
    slenght = 1
    #for store and make high score
    if(not os.path.exists("storage.txt")):
        with open("storage.txt","w")as f:
            f.write("0")
    with open("storage.txt", "r") as f:
        highscore = f.read()

    # food of snake by cordinates
    fsnakex = random.randint(20, rwidth / 2)
    fsnakey = random.randint(20, rheight / 2)
    score=0

    # snakesize
    snakesize = 10

    # clock or frame per seconds functions
    fps = 60

    while not egame:
       if gover:
           with open("storage.txt","w")as f:
               f.write(str(highscore))
           root.fill(red)
           textscore("game over press enter to continue",black,100,300)
           for event in pygame.event.get():
               # print(event)
               # quit function

               if event.type == pygame.QUIT:
                   egame = True
               if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()

       else:
           for event in pygame.event.get():
               # print(event)
               # quit function

               if event.type == pygame.QUIT:
                   egame = True
               # player moving function
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RIGHT:
                       vsnakex = vsnakex + 5  # for increasing in one tap by fix velocity
                       vsnakey = 0  # for not moving in diangular
                       print ('RIGHT')  # right moving function
                   if event.key == pygame.K_LEFT:
                       vsnakex = vsnakex - 5
                       vsnakey = 0
                       print ('LEFT')  # left moving function
                   if event.key == pygame.K_UP:
                       vsnakey = vsnakey - 5
                       vsnakex = 0
                       print ('UP')  # up moving function
                   if event.key == pygame.K_DOWN:
                       vsnakey = vsnakey + 5
                       vsnakex = 0
                       print ('DOWN')  # down moving function
#for move in right direction
           snakex = snakex + vsnakex
           snakey = snakey + vsnakey
           # scoring function
           if abs(snakex - fsnakex) < 10 and abs(snakey - fsnakey) < 10:
               score += 10
               print ("scour=", score)
               fsnakex = random.randint(20, rwidth / 2)
               fsnakey = random.randint(20, rheight / 2)
               slenght += 5
               if score>int(highscore):
                   highscore=score

           # colour function
           root.fill(cyan)

           # score printing
           textscore("score:  " + str(score)+"Highscore:  "+str(highscore), green, 5, 5)
           #pygame.draw.rect(root,red,[fsnakex,fsnakey,snakesize,snakesize])

           # lenght maker
           head = []
           head.append(snakex)
           head.append(snakey)
           slist.append(head)
           # lenght checker
           if len(slist) > slenght:
               del slist[0]
               #outer window game over
           if head in slist[:-1]:
               gover=True
           # wall not go
           if snakex < 0 or snakex > rwidth or snakey < 0 or snakey > rheight:
               gover = True
               #print("game over")

           # snake building
           pygame.draw.rect(root, grey, (snakex, snakey, snakesize, snakesize))  # snake
           pygame.draw.rect(root, blue, (fsnakex, fsnakey, snakesize, snakesize))  # food
           plotsnake(root, wite, slist, snakesize)


#main window updating function
       pygame.display.update()
#clock tick function
       clock.tick(fps)
#quit
    pygame.quit()
    quit()
welcome()
