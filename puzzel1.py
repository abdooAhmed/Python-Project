import pygame
from pygame.locals import *
import sys
import random
import arabic_reshaper
from bidi.algorithm import get_display
res1=arabic_reshaper.reshape('ا')
bid1=get_display(res1)
res2=arabic_reshaper.reshape('ب')
bid2=get_display(res2)
res3=arabic_reshaper.reshape('ت')
bid3=get_display(res3)
res4=arabic_reshaper.reshape('ث')
bid4=get_display(res4)
res5=arabic_reshaper.reshape('ج')
bid5=get_display(res5)
res6=arabic_reshaper.reshape('ح')
bid6=get_display(res6)
res7=arabic_reshaper.reshape('خ')
bid7=get_display(res7)
res8=arabic_reshaper.reshape('د')
bid8=get_display(res8)
res9=arabic_reshaper.reshape('ذ')
bid9=get_display(res9)
res10=arabic_reshaper.reshape('ر')
bid10=get_display(res10)
res11=arabic_reshaper.reshape('ز')
bid11=get_display(res11)
res12=arabic_reshaper.reshape('س')
bid12=get_display(res12)
res13=arabic_reshaper.reshape('ش')
bid13=get_display(res13)
res14=arabic_reshaper.reshape('ص')
bid14=get_display(res14)
res15=arabic_reshaper.reshape('ض')
bid15=get_display(res15)
res16=arabic_reshaper.reshape('ط')
bid16=get_display(res16)
res17=arabic_reshaper.reshape('ظ')
bid17=get_display(res17)
res18=arabic_reshaper.reshape('ع')
bid18=get_display(res18)
res19=arabic_reshaper.reshape('غ')
bid19=get_display(res19)
res20=arabic_reshaper.reshape('ف')
bid20=get_display(res20)
res21=arabic_reshaper.reshape('ق')
bid21=get_display(res21)
res22=arabic_reshaper.reshape('ك')
bid22=get_display(res22)
res23=arabic_reshaper.reshape('ل')
bid23=get_display(res23)
res24=arabic_reshaper.reshape('م')
bid24=get_display(res24)
res25=arabic_reshaper.reshape('ن')
bid25=get_display(res25)
res26=arabic_reshaper.reshape('ه')
bid26=get_display(res26)
res27=arabic_reshaper.reshape('و')
bid27=get_display(res27)
res28=arabic_reshaper.reshape('ي')
bid28=get_display(res28)

char3=[[bid26,bid2],[bid28,bid1],[bid12,bid6],[bid8,bid10],[bid4,bid14],[bid24,bid16],[bid18,bid20],[bid22,bid15]]
char2=[[bid26,bid2],[bid28,bid1],[bid12,bid6],[bid8,bid10],[bid4,bid14],[bid24,bid16],[bid18,bid20],[bid22,bid15]]
char=['',bid1,bid2,bid3,bid4,bid5,bid6,bid7,bid8,bid9,bid10,bid11,bid12,bid13,bid14,bid15,bid16]
char1=[bid1,bid2,bid3,bid4,bid5,bid6,bid7,bid8,bid9,bid10,bid11,bid12,bid13,bid14,bid15,bid16,bid17,bid18,bid19,bid20,bid21,bid22,bid23,bid24,bid25,bid26,bid27,bid28]
bordwidth=4
bordheight=4
titlesize=80
titlesize1=60
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

def main1():
    global basicfont, dis, basicfont1
    pygame.init()
    sound1 = pygame.mixer.Sound('Recording_2.wav')
    dis = pygame.display.set_mode((widthbox, heightbox))
    pygame.display.set_caption('manu')
    basicfont = pygame.font.Font('Fonts/arial.ttf', 32)
    basicfont1 = pygame.font.Font('Fonts/arial.ttf', 18)
    text_to_be_reshaped = 'اللغة العربية رائعة'
    reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
    bidi_text = get_display(reshaped_text)
    newsuf, newrect = makeText('game 1', white, green,320,200)
    resetsurf, resetrect = makeText('game 2',white, green, 320, 260)
    bacg = darkTur
    dis.fill(bacg)
    while True:
        dis.blit(resetsurf, resetrect)
        dis.blit(newsuf, newrect)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                if resetrect.collidepoint(event.pos):
                     main2()
                elif newrect.collidepoint(event.pos):
                    main()
        pygame.display.update()
def main():
    global basicfont, dis, basicfont1,sound1
    pygame.init()
    dis=pygame.display.set_mode((widthbox,heightbox))
    pygame.display.set_caption('puzzel')
    basicfont = pygame.font.Font('Fonts/arial.ttf', 32)
    basicfont1 = pygame.font.Font('Fonts/arial.ttf', 18)
    newsuf, newrect = makeText('new game', white, green, widthbox - 120, heightbox - 90)
    resetsurf, resetrect = makeText('reset', white, green, widthbox - 120, heightbox - 60)
    solvsur,solfrect=makeText('back',white,green,widthbox-120,heightbox-30)
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
                    elif newrect.collidepoint(event.pos):
                        mainbord,seq=genertnewPuz(40)
                    elif solfrect.collidepoint(event.pos):
                        main1()
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
                    sound1.stop()
            if slidto:
                slidanimation(mainbord,slidto,int(titlesize/2))
                makemove(mainbord,slidto)
                allmove.append(slidto)
            slidto=None
        pygame.display.update()
def makeText(text,col,bcol,top,left):
        textsur = basicfont1.render(text.encode('utf-8'), True, col, bcol)
        textrec = textsur.get_rect()
        textrec.topleft = (top, left)
        return (textsur, textrec)
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
            colum.append(char[count])
            count+=bordwidth
        bord.append(colum)
        count -= bordwidth * (bordheight - 1) + bordwidth - 1
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
    sound1.play()
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
def main2():
    global basicfont, dis, basicfont1
    pygame.init()
    sound1 = pygame.mixer.Sound('Recording_2.wav')
    dis = pygame.display.set_mode((widthbox, heightbox))
    pygame.display.set_caption('manu')
    basicfont = pygame.font.Font('Fonts/arial.ttf', 32)
    basicfont1 = pygame.font.Font('Fonts/arial.ttf', 18)
    newsuf, newrect = makeText('new game', white, green, widthbox - 120, heightbox - 90)
    resetsurf, resetrect = makeText('reset', white, green, widthbox - 120, heightbox - 60)
    solvsur, solfrect = makeText('back', white, green, widthbox - 120, heightbox - 50)
    bacg = darkTur
    dis.fill(bacg)
    x = 1
    mainbroad=generate()
    solve=[]
    count=1
    last = 0
    for i in range(7):
        colum=[]
        for n in range(bordheight):
            if i>last:
                if x == 1:
                    x = 2
                else:
                    x = 1
            if x==1:
                if (i+1)%2!=0:
                    colum.append(None)
                else:
                    colum.append(char1[count])
            else:
                if  (i+1)%2==0:
                    colum.append(None)
                else:
                    colum.append(char1[count])
            count+=7
        mainbroad.append(colum)
        last = i
        count -= 7 * (bordheight - 1) + 7 - 1
    mainbroad[2][0]=bid3
    mainbroad[6][0]=bid7
    count = 0
    x=1
    for i in range(7):
        colum=[]
        for n in range(bordheight):
            if i>last:
                if x == 1:
                    x = 2
                else:
                    x = 1
            if x==1:
                if False and (i+1)%2!=0:
                    colum.append(None)
                else:
                    colum.append(char1[count])
            else:
                if False and (i+1)%2==0:
                    colum.append(None)
                else:
                    colum.append(char1[count])
            count+=7
        solve.append(colum)
        last = i
        count -= 7 * (bordheight - 1) + 7 - 1
    noneV=[]
    v11=0
    for v1 in mainbroad:
        v12 = 0
        for v2 in v1:
            if v2==None:
                noneV.append((v11,v12))
            v12+=1
        v11+=1
    while True:
        drawect1(mainbroad)
        nonedect(char2)
        dis.blit(newsuf, newrect)
        dis.blit(solvsur, solfrect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                spotx, spoty = getspotClicked1(char2, event.pos[0], event.pos[1])
                if (spotx,spoty)==(None,None):
                    if newrect.collidepoint(event.pos):
                        mainbroad=generate()
                        char2.clear()
                        for i in char3:
                            char2.append(i)
                    elif solfrect.collidepoint(event.pos):
                        main1()
                else:
                    sound1.play()
                    value=[]
                    drawhiglite1(char2, spotx, spoty)
                    pygame.time.wait(300)
                    c=0
                    x=0
                    y=0
                    for m in solve:
                        try:
                            value.append((c,m.index(char2[spotx][spoty])))
                        except Exception:
                            pass
                        c+=1
                    if value[0] in noneV:

                        mainbroad[value[0][0]][value[0][1]]=char2[spotx][spoty]
                        char2[spotx][spoty]=None
                        for s in range(0,int(titlesize1+titlesize1/2),int(titlesize1/2)):
                            drawtitle1(value[0][0],value[0][1],char2[spotx][spoty],i,0)
                            drawblank1(spotx,spoty,i,0)
                    noneV.remove(value[0])
                    value.clear()
                    pygame.time.wait(200)
                    sound1.stop()
        pygame.display.update()

def drawect1(bord):
    borx=0
    bory=0
    for x in range(7):
        for y in range(bordheight):
            if bord[x][y]!=None:
                left, right = lef_top1(x, y)
                pygame.draw.rect(dis, green, (left, right, titlesize1, titlesize1))
                surtext = basicfont.render(str(bord[x][y]), True, white)
                recttext = surtext.get_rect()
                recttext.center = int(left+(titlesize1 / 2)),int(right+(titlesize1 / 2))
                dis.blit(surtext,recttext)
            else:
                left, right = lef_top1(x, y)
                pygame.draw.rect(dis,darkTur, (left, right, titlesize1, titlesize1))
            bory=1
        borx=1
        pygame.draw.line(dis, darkTur, (lef_top1(1, 0)), (lef_top1(1, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(2, 0)), (lef_top1(2, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(3, 0)), (lef_top1(3, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(4, 0)), (lef_top1(4, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(5, 0)), (lef_top1(5, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(6, 0)), (lef_top1(6, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(0, 1)), (lef_top1(7,1)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(0, 2)), (lef_top1(7, 2)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(0, 3)), (lef_top1(7, 3)), 1)
        pygame.draw.line(dis, darkTur, (lef_top1(0, 4)), (lef_top1(7, 4)), 1)
        pygame.draw.line(dis, green, (lef_top1(0, 0)), (lef_top1(0, 4)), 1)
        pygame.draw.line(dis, green, (lef_top1(7, 0)), (lef_top1(7, 4)), 1)
        pygame.draw.line(dis, green, (lef_top1(7, 4)), (lef_top1(0, 4)), 1)
        pygame.draw.line(dis, green, (lef_top1(0, 0)), (lef_top1(7, 0)), 1)


def nonedect(bord):
    borx=0
    bory=0
    for x in range(8):
        for y in range(2):
            if bord[x][y]!=None:
                left, right = lef_top2(x, y)
                pygame.draw.rect(dis, green, (left, right, titlesize1, titlesize1))
                surtext = basicfont.render(str(bord[x][y]), True, white)
                recttext = surtext.get_rect()
                recttext.center = int(left+(titlesize1 / 2)),int(right+(titlesize1 / 2))
                dis.blit(surtext,recttext)
            else:
                left, right = lef_top2(x, y)
                pygame.draw.rect(dis,darkTur, (left, right, titlesize1, titlesize1))
            bory=1
        borx=1
        pygame.draw.line(dis, darkTur, (lef_top2(1, 0)), (lef_top2(1, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top2(2, 0)), (lef_top2(2, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top2(3, 0)), (lef_top2(3, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top2(4, 0)), (lef_top2(4, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top2(5, 0)), (lef_top2(5, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top2(6, 0)), (lef_top2(6, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top2(7, 0)), (lef_top2(7, 4)), 1)
        pygame.draw.line(dis, darkTur, (lef_top2(0, 1)), (lef_top2(8, 1)), 1)
def lef_top1(x,y):
    left=60+(titlesize1*x)
    right=15+(titlesize1*y)
    return (left,right)

def lef_top2(x,y):
    left=20+(titlesize1*x)
    right=330+(titlesize1*y)
    return (left,right)

def generate():
    mainbroad=[]
    count=0
    x = 1
    last = 0
    for i in range(7):
        colum=[]
        for n in range(bordheight):
            if i>last:
                if x == 1:
                    x = 2
                else:
                    x = 1
            if x==1:
                if (i+1)%2!=0:
                    colum.append(None)
                else:
                    colum.append(char1[count])
            else:
                if  (i+1)%2==0:
                    colum.append(None)
                else:
                    colum.append(char1[count])
            count+=7
        mainbroad.append(colum)
        last = i
        count -= 7 * (bordheight - 1) + 7 - 1
    return mainbroad


def getspotClicked1(bord,x,y):
    for tx in range(len(bord)):
        for ty in range(len(bord[0])):
            left,top=lef_top2(tx,ty)
            rect=pygame.Rect(left,top,titlesize1,titlesize1)
            if rect.collidepoint(x,y):
                return (tx,ty)
    return(None,None)
def drawhiglite1(bord,x,y):
    left,top=lef_top2(x,y)
    num=bord[x][y]
    surt = basicfont.render(str(num),True,darkTur)
    surr=surt.get_rect()
    surr.center=int(left+titlesize1/2),int(top+titlesize1/2)
    dis.blit(surt,surr)
    pygame.display.update()

def drawtitle1(bx,by,num,advx,advy):
    x,y=lef_top1(bx,by)
    pygame.draw.rect(dis,green,(x+advx,y+advy,titlesize1,titlesize1))
    surtext = basicfont.render(str(num), True, white)
    recttext = surtext.get_rect()
    recttext.center = int(x + (titlesize1 / 2)), int(y + (titlesize1 / 2))
    dis.blit(surtext, recttext)
    pygame.display.update()
def drawblank1(x,y,advx,advy):
    x,y=lef_top2(x,y)
    pygame.draw.rect(dis,darkTur,(x+advx,y+advy,titlesize1,titlesize1))
    pygame.display.update()


main1()