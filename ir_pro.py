import nltk
import os
nltk.download('stopwords')
import math

from nltk.corpus import stopwords
stop_word=set(stopwords.words('english'))
words=[]
term_id={}
print('               part1')
def clean(line):
    y=''
    x=['.',',','-']
    for i in line:
        for n in i:
            if n in x:
                continue
            else:
                y+=n
    return y
ln=0
def low(z):
    return z.lower()
for i in range(1,11,1):
    ln+=1
    file = open('file/%d.txt'%(i))
    read = file.read()
    read=clean(read)
    lines=read.split()
    index=0
    for word in lines:
        if word in set(stopwords.words('english')) and word != "in" and word != "to" and word != "where":
            continue
        else:
            index += 1
            if word not in term_id:
                term_id[word] = []
                term_id[word].append(1)
                term_id[word].append({ln:[1,index]})
            else:
                if ln in term_id[word][1]:
                    term_id[word][0] += 1
                    term_id[word][1][ln][0] += 1
                    term_id[word][1][ln].append(index)
                else:
                    term_id[word][0] += 1
                    term_id[word][1][ln] = [1,index]
print('tokeniztation and removel stop words')
for i in term_id.keys():
    print(i.ljust(5,' '),end=' ')
print()
print()
print('               part2')
def check(ws,bol='',index=0,doc=0):
    if bol =='and':
        x=0
        y=0
        ans=[]
        while True:
            try:
                doc1 = list(term_id[ws[index - 1]][1].keys())
                doc2 = list(term_id[ws[index + 1]][1].keys())
                if doc1[x]==doc2[y]:
                    ans.append(doc2[y])
                    x+=1
                    y+=1
                elif doc1[x]>doc2[y]:
                    y+=1
                else:
                    x+=1
            except Exception:
                break

        if len(ans)>0:
            return ans
        return None
    elif bol=='or':
        non=True
        non2=True
        try:
            doc2 = list(term_id[ws[index + 1]][1].keys())
        except Exception:
            non=False
        try:
            doc1 = list(term_id[ws[index - 1]][1].keys())
        except Exception:
            if non:
                non2=False
                pass
            else:
                return None
        if non:
            if non2:
                for i in doc2:
                    if i not in doc1:
                        doc1.append(i)
                return sorted(doc1)
            else:
                return doc2
        else:
            return doc1
    else:
        ans={}
        x=0
        y=0
        try:
            doc1 = term_id[ws[0]][1]
            doc2 = term_id[ws[1]][1]
            key1=list(doc1.keys())
            key2=list(doc2.keys())
            while True:
                try:
                    if key1[x] == key2[y]:
                        n = 1
                        m = 1
                        while True:
                            try:
                                if doc2[key2[y]][n] - doc1[key1[x]][m] == 1:
                                    ans[key2[y]]=[doc2[key2[y]][n], doc1[key1[x]][m]]
                                    n += 1
                                    m += 1
                                elif doc2[key2[y]][n] > doc1[key1[x]][m]:
                                    m += 1
                                else:
                                    n += 1
                            except Exception:
                                break
                        x += 1
                        y += 1
                    elif key1[x] > key2[y]:
                        y += 1
                    else:
                        x += 1
                except Exception:
                    break
            return ans
        except Exception:
            return None
def idf(tf):

    t = math.log10(10 / tf)
    return t

def tf_idf(idf,tf):
    return idf*tf
doc1={}
doc2={}
doc3={}
doc4={}
doc5={}
doc6={}
doc7={}
doc8={}
doc9={}
doc10={}

def td(term=''):
    words = []
    ln=0
    term_id1 = {}
    for i in range(1, 11, 1):
        ln += 1
        file = open('file/%d.txt' % (i))
        read = file.read()
        read = clean(read)
        lines = read.split()
        index = 0
        for word in lines:
            if not word :
                continue
            else:

                index += 1
                if word not in term_id1:
                    term_id1[word] = []
                    term_id1[word].append(1)
                    term_id1[word].append({ln: [1, index]})
                else:
                    if ln in term_id1[word][1]:
                        term_id1[word][0] += 1
                        term_id1[word][1][ln][0] += 1
                        term_id1[word][1][ln].append(index)
                    else:
                        term_id1[word][0] += 1
                        term_id1[word][1][ln] = [1, index]

    print(term_id1)
    print('\t\tDoc1')
    print('term'.ljust(15,' '),end='  ')
    print('tf'.ljust(4,' '),end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ln = []
    ans1=0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 1:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
             if key1 == 1 :
                print(key.ljust(15,' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5,' ') % (1 + math.log10(term_id1[key][1][key1][0])),end=' ')
                t=idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1,''.ljust(5,' '),end=' ')
                doc1[key]=t1/math.sqrt(ans1)
                print(t1/math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln=[]
    print()


    print('\t\tDoc2')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 2:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 2:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1)**2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc2[key]=t1/math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln=[]
    print()


    print('\t\tDoc3')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1=0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 3:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []

    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 3:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1)**2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc3[key]=t1/math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()



    print('\t\tDoc4')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 4:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 4:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc4[key] = t1 / math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()


    print('\t\tDoc5')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 5:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 5:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc5[key] = t1 / math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()



    print('\t\tDoc6')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 6:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 6:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc6[key] = t1 / math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()



    print('\t\tDoc7')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 7:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 7:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc7[key] = t1 / math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()



    print('\t\tDoc8')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 8:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 8:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc8[key] = t1 / math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()


    print('\t\tDoc9')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 9:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 9:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc9[key] = t1 / math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()

    print('\t\tDoc10')
    print('term'.ljust(15, ' '), end='  ')
    print('tf'.ljust(4, ' '), end='  ')
    print('tf.wight'.ljust(9, ' '), end='  ')
    print('idf'.ljust(23, ' '), end='  ')
    print('tf.idf'.ljust(25, ' '), end='  ')
    print('norm')
    ans1 = 0
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 10:
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    ln = []
    for key in term_id1.keys():
        for key1 in term_id1[key][1].keys():
            if key1 == 10:
                print(key.ljust(15, ' '), end='  ')
                print('%d'.ljust(5, ' ') % (term_id1[key][1][key1][0]), end=' ')
                print('%f'.ljust(5, ' ') % (1 + math.log10(term_id1[key][1][key1][0])), end=' ')
                t = idf(term_id1[key][0])
                t1 = tf_idf(idf(term_id1[key][0]), (1 + math.log10(term_id1[key][1][key1][0])))
                ln.append((t1) ** 2)
                print(t, ''.ljust(5, ' '), end=' ')
                print(t1, ''.ljust(5, ' '), end=' ')
                doc10[key] = t1 / math.sqrt(ans1)
                print(t1 / math.sqrt(ans1))
    ans1 = 0
    for i in ln:
        ans1 = i + ans1
    print(math.sqrt(ans1))
    ln = []
    print()




def simalar(term):
    rank = {}
    t={}
    print("hi")
    print(term)
    for n in term:
        if n in t.keys():
           t[n] += 1
        else:
            t[n]=1
    ln=[]
    ans1=0
    for k in t.keys():
        t1 = tf_idf(idf(term_id[k][0]), (1 + math.log10(t[k])))
        ln.append((t1) ** 2)
    for i in ln:
        ans1 = i + ans1
    docq={}
    for key in t.keys():
        print(key.ljust(15,' '), end='  ')
        print('%d'.ljust(5, ' ') % (t[key]), end=' ')
        print('%f'.ljust(5,' ') % (1 + math.log10(t[key])), end=' ')
        t0=idf(term_id[key][0])
        t1 = tf_idf(t0,(1 + math.log10(t[key])))
        print(t0, ''.ljust(5, ' '), end=' ')
        print(t1,''.ljust(5,' '),end=' ')
        docq[key]=t1/math.sqrt(ans1)
        print(t1/math.sqrt(ans1))
    print(math.sqrt(ans1))
    print()
    sim=0
    for key in t.keys():
        for doc in doc1:
            if doc == key:
                sim=doc1[doc]*docq[key]+sim
    rank['Doc1']=sim

    sim=0
    for key in t.keys():
        for doc in doc2:
            if doc == key:
                sim=doc2[doc]*docq[key]+sim
    rank['Doc2']=sim

    sim=0
    for key in t.keys():
        for doc in doc3:
            if doc == key:
                sim=doc3[doc]*docq[key]+sim

    rank['Doc3'] = sim


    for key in t.keys():
        for doc in doc4:
            if doc == key:
                sim=doc4[doc]*docq[key]+sim

    rank['Doc4'] = sim

    for key in t.keys():
        for doc in doc5:
            if doc == key:
                sim=doc5[doc]*docq[key]+sim

    rank['Doc5'] = sim

    for key in t.keys():
        for doc in doc6:
            if doc == key:
                sim=doc6[doc]*docq[key]+sim

    rank['Doc6'] = sim


    for key in t.keys():
        for doc in doc7:
            if doc == key:
                sim=doc7[doc]*docq[key]+sim

    rank['Doc7']=sim


    for key in t.keys():
        for doc in doc8:
            if doc == key:
                sim=doc8[doc]*docq[key]+sim

    rank['Doc8'] = sim

    for key in t.keys():
        for doc in doc9:
            if doc == key:
                sim=doc9[doc]*docq[key]+sim

    rank['Doc9'] = sim


    for key in t.keys():
        for doc in doc10:
            if doc == key:
                sim=doc10[doc]*docq[key]+sim

    rank['Doc10']=sim
    k : rank[k] = sorted(rank,key = rank.get)
    for i in k:
        print('similarity of Q,'+str(i)+' : '+str(rank[i]))
for i in term_id.keys():
    print(i,end='')
    for n in term_id[i][1].keys():
        print(': Doc%d : %d'%(n,term_id[i][1][n][1]),end=' ,')
    print()



id=list(term_id)
id.sort(key=low)
query=input('plese enter the query : ')

ws=query.split()

bol=['and','or','not']
if 'and' in ws or 'or' in ws or 'not' in ws:
    i=0
    for w in ws:
        if w in bol:
            ans=check(ws,w,i)
            if ans is list:
                for a in ans:
                    print('Doc',str(a))
            else:
                print(ans)
        i += 1
    s = []
    for n in ws:
        if n not in bol:
            s.append(n)
else:
    if len(ws)==1:
        try:
            ws = [w for w in query.split() if w not in set(stopwords.words('english') and word != "in" and word != "to" and word != "where" )]
            print(ws)
            if len(ws) == 1:
                for w in ws:
                    for i in term_id[w][1]:
                        print('Doc%d :' % (i), end='')
                        for n in range(1, len(term_id[w][1][i]), 1):
                            print(term_id[w][1][i][n], end=',')
                        print()
        except Exception:
            print(None)
    else:
        ws = [w for w in query.split() if w not in set(stopwords.words('english')) or word == "in" or word == "to" or word == "where"]
        ans=check(ws)

        if ans==None:
            print(ans)
        else:
            for i in ans:
                print('Doc%d' % (i))

print()
print('               part3')
td()
print()
query=input('plese enter the query : ')

ws = [w for w in query.split() if w not in set(stopwords.words('english'))]
simalar(ws)






