import pygame,sys,random,os
from pygame.locals import*
pygame.init()
canvas=pygame.display.set_mode((1200,720))
wt = pygame.image.load("images/1.png")
bingo = pygame.image.load("images/correct.png.png")
error  = pygame.image.load("images/error.png")
goahead = pygame.image.load("images/gohead.png")
state = 'START'
que = ''
isRight = 'none'
def fillText(text, position):
    TextFont = pygame.font.Font('images/font1.ttf', 50)
    newText = TextFont.render(text, True, (234,255,128))
    canvas.blit(newText, position) 

def handleEvent():
    global state,que
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_n:
            state = 'RUNNING'
            que = 1
        if state == 'WIN':
            if event.type == MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 1200>x>1000 and 660>y>600:
                    exit()
        
def button():
    global isRight,que,wt
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                return 'UP'
            elif event.key == K_DOWN:
                return 'DOWN'
            elif event.key == K_LEFT:
                return 'LEFT'
            elif event.key == K_RIGHT:
                return 'RIGHT'
        if isRight==True:
            if event.type == MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if 1200>x>1000 and 660>y>600:
                    que += 1
                    if que <=5:
                        wt = pygame.image.load("images/"+str(que)+".png")
                    isRight = 'none'
def ans():
    for i in range(0,-1):
        print(ans)

def question():
    global state,que,isRight
    if que == 1:
        k = button()
        if k == 'DOWN':
            isRight = True
            comPaint()
        if k=='UP' or k=='LEFT' or k=='RIGHT':
            isRight = False
            comPaint()
    if que == 2:
        k = button()
        if k == 'DOWN':
            isRight = True
            comPaint()
        if k=='UP' or k=='RIGHT' or k=='LEFT':
            isRight = False
            comPaint()
    if que == 3:
        k = button()
        if k == 'DOWN':
            isRight = True
            comPaint()
        if k=='UP' or k=='LEFT' or k=='RIGHT':
            isRight = False
            comPaint()
    if que == 4:
        k = button()
        if k == 'UP':
            isRight = True
            comPaint()
        if k=='RIGHT' or k=='DOWN' or k=='LEFT':
            isRight = False
            comPaint()
    if que == 5:
        k = button()
        if k == 'UP':
            state = 'WIN'
        if k=='LEFT' or k=='DOWN' or k=='RIGHT':
            isRight = False
            
            
def comPaint():
    global isRight
    if isRight==True:
            canvas.blit(wt,(0,0))
            canvas.blit(bingo,(1000,620))
    elif isRight=='none':
        canvas.blit(wt,(0,0))
        canvas.blit(error,(1000,620))
    elif isRight==False:
        canvas.blit(wt,(0,0))
        canvas.blit(error,(1000,620))
        
        
canvas.blit(s,(0,0))
fillText('',(500,650))

            

while True:
    if state == 'RUNNING':
        comPaint()
        question()
    if state == 'WIN':
        canvas.blit(wt,(0,0))
        canvas.blit(goahead,(1000,620))
        
    handleEvent()
    pygame.display.update()
    
