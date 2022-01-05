import mysql.connector
alph = 'abcdefghijklmnopqrstuvwxyz'
numbers = '?#%&!$^>*<'
def encryption(name):
    enc = ''
    enc2 = ''
    print(name)
    for i in name:
        if i ==' ':
            enc+=i
            continue
        if i in alph:
            num = alph.index(i)
            enc += alph[(num + 2) % 26]
            enc += alph[(num + 3) % 26]
        else:
            try:
                num = int(i)
                enc += numbers[num]
                enc += numbers[num]
                continue
            except Exception:
                pass
            enc += i
            enc += i
    for i in range(len(enc), 0, -1):
        enc2 += enc[i - 1]
    enc = ''
    for i in enc2:
        if i in alph:
            num = alph.index(i)
            enc += alph[(num + 2)%26]
        else:
            enc += i
    return enc
def decryption(name1):
    dec = ''
    dec2 = ''
    for i in name1:
        if i in alph:
            num = alph.index(i)
            dec += alph[num - 2]
        else:
            dec += i

    for i in range(len(dec), 0, -1):
        dec2 += dec[i - 1]
    dec = ''
    i = 0
    for n in dec2:
        if i % 2 == 0:
            if n in alph:
                num = alph.index(n)
                dec += alph[num - 2]
            else:
                if n in numbers:
                    dec += str(numbers.index(n))
                    i += 1
                    continue
                dec += n
        i += 1
    return dec

class admin():
    mybd = mysql.connector.connect(host='localhost', user='root', passwd='2412', database='admin')
    def chek(self,aith,email,passwd):
        if not aith:
            cursor = self.mybd.cursor()
            cursor.execute('select * from admins ;')
            datas = cursor.fetchall()
            for data in datas:
                 if email == decryption(data[3]) and passwd == decryption(data[4]):
                    return True
            return False
        else:
            if aith=='top':
                cursor = self.mybd.cursor()
                cursor.execute('select email,passwords from admins where auth="high";')
                datas = cursor.fetchall()
                for data in datas:
                    if email == decryption(data[0]) and passwd == decryption(data[1]):
                        return True
            elif aith=='medium':
                cursor = self.mybd.cursor()
                cursor.execute('select email,passwords from admins  where auth="medium"; ')
                datas1 = cursor.fetchall()
                for data in datas1:
                    if email == decryption(data[0]) and passwd == decryption(data[1]):
                        return True
                return False
    def add(self,id,f_n,l_n,email,passwd,aith=''):
        if aith:
            cursor = self.mybd.cursor()
            f_n=encryption(f_n)
            query = 'insert into admins(ID,f_n,l_n,email,passwords,auth) values("%d","%s","%s","%s","%s","%s")' % (int(id),f_n,encryption(l_n),encryption(email),encryption(passwd),aith)
            value = [(id, f_n, l_n, email, passwd)]
            cursor.execute(query)
            self.mybd.commit()

class user():
    e_m=''
    pasd=''
    mybd = mysql.connector.connect(host='localhost', user='root', passwd='2412', database='admin')
    def add(self,id,f_n,l_n,email,passwd,depart):
            cursor = self.mybd.cursor()
            f_n=encryption(f_n)
            query = 'insert into customers(ID,f_n,l_n,email,passwords,dpart) values("%d","%s","%s","%s","%s","%s")' % (int(id),f_n,encryption(l_n),encryption(email),encryption(passwd),encryption(depart))
            value = [(id, f_n, l_n, email, passwd)]
            cursor.execute(query)
            self.mybd.commit()
    def check(self,email,passwd):
        cursor = self.mybd.cursor()
        cursor.execute('select * from customers ;')
        datas = cursor.fetchall()
        self.e_m=email
        self.pasd=passwd
        for data in datas:
            if email == decryption(data[3]) and passwd == decryption(data[4]):
                return True
        return False
    def update(self,f_n,l_n,email,passwd,depart):
        cursor = self.mybd.cursor()
        f_n = encryption(f_n)
        query = 'update customers set f_n="%s",l_n="%s",email="%s",passwords="%s",dpart="%s" where email="%s"' % (
        f_n, encryption(l_n), encryption(email), encryption(passwd), encryption(depart), encryption(self.e_m))
        cursor.execute(query)
        self.mybd.commit()
    def delete(self,email,passwd):
        cursor = self.mybd.cursor()
        query = "delete from customers where email='%s' and passwords='%s' " % (encryption(email), encryption(passwd))
        cursor.execute(query)
        self.mybd.commit()
    def dispaly(self):
        cursor = self.mybd.cursor()
        print(self.e_m,self.pasd)
        cursor.execute("select * from customers where email='%s' and passwords='%s';" %(encryption(self.e_m),encryption(self.pasd)))
        datas = cursor.fetchall()
        print(datas)
        self.mybd.commit()
        x=[]
        for i in datas[0]:
            if i is int:
                x.append(i)
                continue
            x.append(decryption(i))
        return x
class product():
    mybd = mysql.connector.connect(host='localhost', user='root', passwd='2412', database='admin')
    def add(self, id,p_n,pri, depart):
        cursor = self.mybd.cursor()
        p_n = encryption(p_n)
        print(pri)
        query = 'insert into product(ID,p_n,price,dpart) values("%d","%s","%s","%s")' % (int(id), p_n ,str(pri),encryption(depart))
        cursor.execute(query)
        self.mybd.commit()
