def queen(title,row=0):
    if row>=len(title):
        return True
    for col in range(len(title[row])):
        title[row][col]=1


        if safe_queen(title,row,col):
            if queen(title,row+1):
                return True
            title[row][col] = 0
        else:
            title[row][col] = 0
    return False
def safe_queen(title,row,col):
    if row ==0:
        return True
    else:
       col1=[]
       for i in range(row):
           col1.append((i,title[i].index(1)))
           print(col1)
       for x in col1:
           if col == x[1]:
               return False
           elif col == x[1] + 1 and row==x[0]+1:
               return False
           elif col == x[1] - 1  and row==x[0]+1:
               return False
       return True

lenth=input('please enter number of chassboard : ')
lenth=int(lenth)
a = []
c = []
for i in range(lenth):
    for n in range(lenth):
        c.append(0)
    a.append(c)
    c = []

if queen(a):
    for i in a:
        for n in i:
            print(n,end='')
        print()
