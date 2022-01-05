import pygame
from pygame.locals import *
import sys
import random
c=['','ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط']
bordwidth=4
bordheight=4
titlesize=80
widthbox=640
heightbox=480
fbs=30
up='up'
down='down'
left='left'
right='right'
blank=None
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
Bblue=(0,50,255)
darkTur=(3,54,73)
xmargin=int((widthbox-(titlesize*bordwidth))/2)
ymargin=int((heightbox-(titlesize*bordheight))/2)
def main():
    global basicfont,dis
    pygame.init()
    dis=pygame.display.set_mode((widthbox,heightbox))
    pygame.display.set_caption('manu')
    basicfont = pygame.font.Font('Fonts/arial.ttf', 20)
    basicfont1 = pygame.font.Font('Fonts/arial.ttf', 32)
    resetsurf,resetrect=makeText('Reset',white,green,widthbox-120,heightbox-90)
    newsuf,newrect=makeText('New Game',white,green,widthbox-120,heightbox-60)
    solvsur,solfrect=makeText('Solve',white,green,widthbox-120,heightbox-30)
    bacg=darkTur
    dis.fill(bacg)
    mainbord,seq=genertnewPuz(40)
    solve=getstarting()
    slidto=None
    allmove=[]
    while True:
        drawect(mainbord)
        dis.blit(resetsurf,resetrect)
        dis.blit(newsuf,newrect)
        dis.blit(solvsur,solfrect)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONUP:
                spotx,spoty=getspotClicked(mainbord,event.pos[0],event.pos[1])
                if (spotx,spoty)==(None,None):
                    if resetrect.collidepoint(event.pos):
                        resetanimation(mainbord,allmove)
                        drawect(mainbord)
                        allmove=[]
                else:
                    drawhiglite(mainbord,spotx,spoty)
                    pygame.time.wait(300)
            elif event.type==KEYUP:
                    if  event.key in (K_LEFT, K_a) and isvalid(mainbord,left):
                        slidto=left
                    elif event.key in (K_RIGHT, K_d) and isvalid(mainbord,right):
                        slidto=right
                    elif event.key in (K_UP, K_w) and isvalid(mainbord, up):
                        slidto=up
                    elif event.key in (K_DOWN,K_s) and isvalid(mainbord,down):
                        slidto=down
            if slidto:
                slidanimation(mainbord,slidto,int(titlesize/2))
                makemove(mainbord,slidto)
                allmove.append(slidto)
            slidto=None
        pygame.display.update()

def makeText(text,col,bcol,top,left):
    textsur=basicfont.render(text,True,col,bcol)
    textrec=textsur.get_rect()
    textrec.topleft=(top,left)
    return (textsur,textrec)
def drawect(bord):
    borx=0
    bory=0
    for x in range(bordwidth):
        for y in range(bordheight):
            if bord[x][y]!=None:
                left, right = lef_top(x, y)
                pygame.draw.rect(dis, green, (left, right, titlesize, titlesize))
                surtext = basicfont.render(str(bord[x][y]), True, white)
                recttext = surtext.get_rect()
                recttext.center = int(left+(titlesize / 2)),int(right+(titlesize / 2))
                dis.blit(surtext,recttext)
            else:
                left, right = lef_top(x, y)
                pygame.draw.rect(dis,darkTur, (left, right, titlesize, titlesize))
            bory=1
        borx=1
        pygame.draw.line(dis, darkTur, (lef_top(1, 0)), (lef_top(1, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top(2, 0)), (lef_top(2, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top(3, 0)), (lef_top(3, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top(0, 1)), (lef_top(4, 1)), 1)
        pygame.draw.line(dis, darkTur, (lef_top(0, 2)), (lef_top(4, 2)), 1)
        pygame.draw.line(dis, darkTur, (lef_top(0, 3)), (lef_top(4, 3)), 1)
def genertnewPuz(num):
    seq=[]
    bord=getstarting()
    pygame.display.update()
    pygame.time.wait(2000)
    lastmove=None
    for i in range(num):
        move=getrandommove(bord,lastmove)
        makemove(bord,move)
        seq.append(move)
        lastmove=move
    return (bord,seq)

def slidanimation(bord,move,speed):
    movex=0
    movey=0
    x,y=getblank(bord)
    if move==up:
        movex=x
        movey=y+1
    if move==down:
        movex=x
        movey=y-1
    if move=='left':
        movex=x+1
        movey=y
    if move==right:
        movex=x-1
        movey=y
    bacgk=dis.copy()
    left,top=lef_top(movex,movey)
    for i in range(0,titlesize+speed,speed):
        if move==up:
            drawtitle(movex,movey,bord[movex][movey],0,-i)
            drawblank(movex,movey,0,i)
        if move==down:
            drawtitle(movex,movey,bord[movex][movey],0,i)
            drawblank(movex,movey,0,-i)
        if move==left:
            drawtitle(movex,movey,bord[movex][movey],-i,0)
            drawblank(movex,movey,i,0)
        if move==right:
            drawtitle(movex,movey,bord[movex][movey],i,0)
            drawblank(movex,movey,-i,0)
    pygame.display.update()
def getrandommove(bord,move):
    moves=[up,down,left,right]
    if move==up or not isvalid(bord,down):
        moves.remove(down)
    if move==down or not isvalid(bord,up):
        moves.remove(up)
    if move==left or not isvalid(bord,right):
        moves.remove(right)
    if move==right or not isvalid(bord,left):
        moves.remove(left)
    return random.choice(moves)

def isvalid(bord,move):
    x,y=getblank(bord)
    return (move==up and y!=len(bord[0])-1) or \
           (move==down and y!=0) or \
           (move==left and x!=len(bord)-1) or \
           (move==right and x!=0)
def getblank(bord):
    for x in range(bordwidth):
        for y in range(bordheight):
            if bord[x][y]==None:
                return (x,y)
def lef_top(x,y):
    left=xmargin+(titlesize*x)
    right=ymargin+(titlesize*y)
    return (left,right)
def makemove(bord,move):
    x,y=getblank(bord)
    if move==up:
        bord[x][y],bord[x][y+1]=bord[x][y+1],bord[x][y]
    elif move==down:
        bord[x][y],bord[x][y-1]=bord[x][y-1],bord[x][y]
    elif move==left:
        bord[x][y],bord[x+1][y]=bord[x+1][y],bord[x][y]
    elif move==right:
        bord[x][y],bord[x-1][y]=bord[x-1][y],bord[x][y]
def getstarting():
    count=1
    bord=[]
    for i in range(bordwidth):
        colum=[]
        for n in range(bordheight):
            colum.append(c[count])
            count+=bordwidth
        bord.append(colum)
        count-=bordwidth*(bordheight-1)+bordwidth-1
    bord[bordwidth-1][bordheight-1]=None
    return bord
def getspotClicked(bord,x,y):
    for tx in range(len(bord)):
        for ty in range(len(bord[0])):
            left,top=lef_top(tx,ty)
            rect=pygame.Rect(left,top,titlesize,titlesize)
            if rect.collidepoint(x,y):
                return (tx,ty)
    return (None,None)
def drawhiglite(bord,x,y):
    left,top=lef_top(x,y)
    num=bord[x][y]
    surt = basicfont.render(str(num),True,darkTur)
    surr=surt.get_rect()
    surr.center=int(left+titlesize/2),int(top+titlesize/2)
    dis.blit(surt,surr)
    pygame.display.update()
def drawtitle(bx,by,num,advx,advy):
    x,y=lef_top(bx,by)
    pygame.draw.rect(dis,green,(x+advx,y+advy,titlesize,titlesize))
    surtext = basicfont.render(str(num), True, white)
    recttext = surtext.get_rect()
    recttext.center = int(x + (titlesize / 2)), int(y + (titlesize / 2))
    dis.blit(surtext, recttext)
    pygame.display.update()
def drawblank(x,y,advx,advy):
    pygame.draw.rect(dis,darkTur,(x+advx,y+advy,titlesize,titlesize))
    pygame.display.update()
def resetanimation(bord,allmove):
    moves=allmove[:]
    moves.reverse()
    opp=''
    for move in moves:
        if move==up:
            opp=down
        elif move==down:
            opp=up
        elif move==left:
            opp=right
        elif move==right:
            opp=left
        makemove(bord,opp)
main()