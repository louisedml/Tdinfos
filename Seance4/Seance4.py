import matplotlib.pyplot as plt

def h(string): #première fonction de hachage
    hashVal=0
    for x in string:
        hashVal +=ord(x)
    return hashVal

print('la valeur pour "abc" est', h('abc'))

def h2(string):#deuxième fonction de hachage
    h=0
    for c in string:
        h=31*h+ord(c)
    return h
    

class Hashtable:
    def __init__(self,f=h,taille=20):
        self.function=f
        self.taille=taille
        self.table=[[] for _ in range(taille)]
    
    def put(self,key,value):
        N=self.taille
        index=self.function(key)%N
        for i in range(len(self.table[index])):
            if self.table[index][i][0]==key:
                del(self.table[index][i])
        self.table[index].append((key,value))
            
    def get(self,key):
        for i in range(self.taille):
            for j in range(len(self.table[i])):
                if self.table[i][j][0]==key:
                    return self.table[i][j]
        return None
    
    def repartition(self):
        rep=[]
        for i in range(self.taille):
            rep.append(len(self.table[i]))
        N=self.taille
        x=range(N)
        width=1/1.5
        plt.bar(x,rep,width)
        plt.show()
        return rep
    
    def resize(self):
        self.taille= self.taille*2
        table=[[] for _ in range(self.taille)]
        for L in range(len(self.table)):
            for i in range(len(self.table[L])):
                index=self.function(self.table[L][i][0])%self.taille
                table[index].append(self.table[L][i])
        self.table=table
                
                
def liste_dict():
    d=open("frenchssaccent.dic",'r')
    lexique=[]
    for ligne in d:
        mot=ligne[0:len(ligne)-1]
        lexique.append((mot,len(mot)))
    d.close
    return lexique

def table(entrees,fonction):
    L=liste_dict()
    H=Hashtable(fonction,entrees)
    for i in range(len(L)):
        H.put(L[i][0],L[i][1])
    return H
        
    
    
            
if __name__=='__main__':
    H=Hashtable()
    H.put('abc',3)
    g1=H.get('aaa')
    print(g1)
    g2=H.get('abc')
    print(g2)
    r=H.repartition()
    print(r)
    H.put('aaa',5)
    H.put('rcv',3)
    H.put('tg',6)
    H.put('tg',8)
    r2=H.repartition()
    print(r2)
    H3=table(320,h)
    H3.repartition()
    H4=table(320,h2)
    H4.repartition()
    H4.resize()
    H4.repartition()
    
    
    