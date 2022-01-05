import random
import math

lenth=input('please enter number of n : ')
lenth=int(lenth)
CR=.7
print(CR)
wight=1
Numbers_v=150
def start():
    population = []
    for i in range(Numbers_v):
        colum = []
        for n in range(lenth):
            num = 0
            while True:
                num = random.randint(1, lenth)
                if (num) in colum:
                    continue
                else:
                    break
            colum.append(num)
        population.append(colum)
    return population


def evaluate(pop):
    fit_pop={}
    for i in range(len(pop)):
        fit=0
        for n in range(len(pop[i])):
            l = 1
            for x in range(n-1,-1,-1):
                if pop[i][n]==(pop[i][x]+l) or pop[i][n]==(pop[i][x]-l):
                     fit+=1
                l+=1
            l=1
            for y in range(n+1,lenth,1):
                if pop[i][n]==(pop[i][y]+l) or pop[i][n]==(pop[i][y]-l):
                    fit+=1
                l+=1
        fit_pop[i]=fit
    return fit_pop

def subtract(v1,v2):
    v3=[]
    for i in range(len(v1)):
        num= wight*abs(v1[i]-v2[i])
        if num>lenth:
            num=num-lenth
        v3.append(num)
    return v3

def add(v1,v2):
    v3=[]
    for i in range(len(v1)):
        num = abs(v1[i]+v2[i])
        if num > lenth:
            num = num - lenth
        if num in v3:
            while True:
                num =random.randint(1,lenth)
                if num not in v3:
                    break
        v3.append(num)
    return v3
def crossover(pop,mpop):
    p=[]
    last=0
    mut=len(pop)/4
    for i in range(len(pop)):

        if i == last:
            p.append(mpop[i])
            mut-=1
            continue
        last = 4+last
        if random.randint(1,100)/100 > CR:
            if pop[i] not in p:
                p.append(pop[i])
            else:
                if mpop[i] not in p:
                    p.append(mpop[i])
                else:
                    while True:
                        n = random.randint(1,lenth)
                        if n not in p:
                            p.append(n)
                            break

        else:
            if mpop[i] not in p:
                p.append(mpop[i])
            else:
                if pop[i] not in p:
                    p.append(pop[i])
                else:
                    while True:
                        n = random.randint(1,lenth)
                        if n not in p:
                            p.append(n)
                            break
    return p



def preper_to_mutant(population):
    Mpopulation = []
    for pop in population:
        i = random.randint(0, 99)
        x = i
        vector1 = population[i]
        i = random.randint(0, 99)
        if i == x:
            while True:
                i = random.randint(0, 99)
                if i != x:
                    break
        x = i
        vector2 = population[i]

        i = random.randint(0, 99)
        if i == x:
            while True:
                i = random.randint(0, 99)
                if i != x:
                    break
        x = i
        vector3 = population[i]
        SubVector = subtract(vector2, vector3)
        MVector = add(vector1, SubVector)
        Mpopulation.append(crossover(pop, MVector))
    return Mpopulation


OPopulation = start()
fit=evaluate(OPopulation)

a=sorted(fit.values())

for i in range(200):
    SPopualtion=[]
    MutantPopulation=[]
    TrialPopulation=[]
    MutantPopulation = preper_to_mutant(OPopulation)
    for g in range(len(OPopulation)):
        TrialPopulation.append(crossover(OPopulation[g], MutantPopulation[g]))
    fit2=evaluate(TrialPopulation)
    equals=0
    for x in range(len(OPopulation)):
        if fit[x] < fit2[x]:
            SPopualtion.append(OPopulation[x])
        elif fit2[x] == fit[x]:
            SPopualtion.append(OPopulation[x])
        elif fit2[x] < fit[x]:
            equals+=1
            SPopualtion.append(TrialPopulation[x])
    fit3=evaluate(SPopualtion)
    OPopulation=SPopualtion.copy()
    fit=evaluate(OPopulation)
    if 0 in fit.values():
        print('Solved')
        for k, v in fit.items():
            if v == 0:
                print(OPopulation[k])
                break
        break





























#fit2={}
#for m in a:
    #for i,n in fit.items():
       #if n == m:
          #fit2[i]=n
