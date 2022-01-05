import random




mylist=[[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solved_soduko=[[8, 2, 7, 1,5, 4 ,3, 9, 6],
              [9, 6, 5, 3, 2, 7, 1, 4, 8],
              [3, 4, 1, 6, 8, 9, 7, 5, 2],
              [5, 9, 3, 4, 6, 8, 2, 7, 1],
              [4, 7, 2, 5, 1, 3, 6, 8, 9],
              [6, 1, 8, 9, 7, 2, 4, 3, 5],
              [7, 8, 6, 2, 3, 5, 9, 1, 4],
              [1, 5, 4, 7, 9, 6, 8, 2, 3],
              [2, 3, 9, 8, 4, 1, 5, 6, 7]]
def rowisvalid(grid,i,e):
    rowok=0
    for c in range(9):
        if e!=grid[i][c] :
            rowok=rowok+1

    return rowok==8

def colisvalid(grid,j,e):
    colok=0
    for c in range(9):
        if e!=grid[c][j] :
            colok=colok+1

    return colok==8

def sectisvalid(grid,i,j,e):
    secok=0
    sectopx,sectopy=3*(i//3),3*(j//3)
    for x in range(sectopx,sectopx+3):
        for y in range(sectopy,sectopy+3):
            if e != grid[x][y]:
                secok=secok+1
    return secok==8

def gridsvalid(grid):
    count=0
    for i in range (9):
        for j in range (9):
            row=rowisvalid(grid,i,grid[i][j])
            col=colisvalid(grid,j,grid[i][j])
            sect=sectisvalid(grid,i,j,grid[i][j])
            if row and col and sect:
                count=count+1

    return count


def population_fit(population):
    dictionary_fit={}
    for i in range (100):
        fit=gridsvalid(population[i])
        dictionary_fit[i] = fit
    return dictionary_fit

def sortpopulation(population):
    dictionary_fit={}
    for i in range (100):
        fit=gridsvalid(population[i])
        dictionary_fit[i] = fit
    result=sorted(dictionary_fit.values())
    return result



population=[]
sorted_population=[]



for i in range(100):
    population.append(mylist)

for i in range(100):
        for r in range(9):
           for c in range (9):
               if(population[i][r][c]==0):
                    population[i][r][c]=random.randint(1,9)


dd=population_fit(population)

a=sorted(dd.values())

mm={}
for m in a:
    for i,n in dd.items():
       if n == m:
          mm[i]=n

index_of_sorted_population=[]
for key in mm.keys() :
    index_of_sorted_population.append(key)
index_of_sorted_population.reverse()
#print(index_of_sorted_population)

for i in range (100):
    sorted_population.append(population[index_of_sorted_population[i]])

trial=[[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

mutant=[[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
mutant[8][8]=sorted_population[98][8][8]-sorted_population[98][8][8]+sorted_population[98][8][8]
print(mutant[8][8])
print(sorted_population[98][8][8])
f=1
cr=8
while sorted_population[1]!=60:
    for i in range(100):
        #election of target vector and other 3 vector
        target=sorted_population[i]
        #p1=random.randint(0,10)
        v1=sorted_population[1]
        #p2=random.randint(0,10)
        v2=sorted_population[2]
        #p3=random.randint(0,10)
        v3=sorted_population[3]
        for r in range (9):
            for c in range (9):
                #a1=random.randint(0,99)
                #a2=random.randint(0,99)
                #a3=random.randint(0,99)
                mutant[r][c]=v1[r][c]-(v2[r][c]+v3[r][c])
                if (mutant[r][c]>9):
                    mutant[r][c]=9
        #making crossover between mutant vector and target vector
        n=random.randint(0,10)
        for r in range (9):
            for c in range (9):
                n = random.randint(0, 10)
                if (n>cr):
                    trial[c][r]=target[c][r]
                else:
                    trial[c][r]=mutant[c][r]
                    ##look at tep number 6 ya
                    # calculate the fit of target and trail vector to choose which on will be in the next population
                target_fit = gridsvalid(target)
                trial_fit = gridsvalid(trial)
                if (target_fit>trial_fit):
                    sorted_population[i]=target
                else:
                    sorted_population=trial



