import pygame
from pygame.locals import *
import sys
import random
from pygame import locals
def left_top(x,y):
    if x==0:
        left = x * (100) + 50
    else:
        left = x * (100) + 50
    if y==0:
        top = y * (100) + 50
    else:
        top = y * (100) + 50
    return left,top
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
gold=(47, 54,60)
def main():
    global DISPLAYSURF,surt
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)
    pygame.display.set_caption('Drawing')
    basicfont = pygame.font.Font('Fonts/framd.ttf', 40)

    # draw on the surface object

    DISPLAYSURF.fill(gold)
    surt = basicfont.render('Q', True, (255, 215, 0))

    for i in range(4):
        for n in range(4):
            if i % 2 == 0:
                if n % 2 == 0:
                    x, y = left_top(i, n)
                    mer = 2 * i
                    mer1 = 2 * n
                    pygame.draw.rect(DISPLAYSURF, WHITE, (x + mer, y + mer1, 100, 100))
                else:
                    x, y = left_top(i, n)
                    mer = 2 * i
                    mer1 = 2 * n
                    pygame.draw.rect(DISPLAYSURF, BLACK, (x + mer, y + mer1, 100, 100))
            else:
                if n % 2 == 0:
                    x, y = left_top(i, n)
                    mer = 2 * i
                    mer1 = 2 * n
                    pygame.draw.rect(DISPLAYSURF, BLACK, (x + mer, y + mer1, 100, 100))
                else:
                    x, y = left_top(i, n)
                    mer = 2 * i
                    mer1 = 2 * n
                    pygame.draw.rect(DISPLAYSURF, WHITE, (x + mer, y + mer1, 100, 100))
    if queen(a):
        print(a)
        print('solve')
        for i in a:
            for n in i:
                print(n, end='')
            print()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
def drow_queen(i,n):
        x, y = left_top(i, n)
        surr = surt.get_rect()
        surr.center = int(x + 100 / 2), int(y + 100 / 2)
        DISPLAYSURF.blit(surt, surr)
        pygame.display.update()
        pygame.time.wait(1000)
def remove(x,y):
    if x%2==0:
        if y%2==0:
            mer = 2 * x
            mer1 = 2 * y
            x, y = left_top(x, y)
            pygame.draw.rect(DISPLAYSURF, WHITE, (x + mer, y + mer1, 100, 100))
        else:
            mer = 2 * x
            mer1 = 2 * y
            x, y = left_top(x, y)
            pygame.draw.rect(DISPLAYSURF, BLACK, (x + mer, y + mer1, 100, 100))
    else:
        if y%2==0:
            mer = 2 * x
            mer1 = 2 * y
            x, y = left_top(x, y)
            pygame.draw.rect(DISPLAYSURF, BLACK, (x + mer, y + mer1, 100, 100))
        else:
            mer = 2 * x
            mer1 = 2 * y
            x, y = left_top(x, y)
            pygame.draw.rect(DISPLAYSURF, WHITE, (x + mer, y + mer1, 100, 100))
    pygame.display.update()

def queen(title,row=0):
    if row>=len(title):
        return True
    for col in range(len(title[row])):
        title[row][col]=1
        drow_queen(col,row)
        if safe_queen(title,row,col):
            if queen(title,row+1):
                return True
            title[row][col] = 0
            remove(col,row)
        else:
            pygame.time.wait(2)
            title[row][col] = 0
            remove(col,row)
    return False
def safe_queen(title,row,col):
    if row ==0:
        return True
    else:
       col1=[]
       for i in range(row):
           col1.append((i,title[i].index(1)))

       for x in col1:
           if col == x[1]:
               return False
           elif col == x[1] + 1 and row==x[0]+1:
               return False
           elif col == x[1] - 1  and row==x[0]+1:
               return False
       return True
a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
main()
