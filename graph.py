import collections
def bts(g,s):
    vis,Q=[],collections.deque([s])
    vis.append(s)
    while Q:
        vertix=Q.popleft()
        print(vertix)
        for n in g[vertix]:
            if n not in vis:
                Q.append(n)
                vis.append(n)
    print(vis)
def dbs(g,s,vis=[]):
    if s not in vis:
        vis.append(s)
        for n in g[s]:
            dbs(g,n,vis)
        print(vis)
if __name__=='__main__':
    g={'a':['b','c'],'b':['d','e'],'c':['f'],'d':[],'e':['f'],'f':[]}
    dbs(g,'a')

