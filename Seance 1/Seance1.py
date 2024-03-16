#EXO 1
import copy
tirage=['a','r','b','g','e','s','c','j']
def pluslongmot(tirage):
    f=open("frenchssaccent.dic",'r')
    lexique=[]
    for ligne in f: #On convertit en liste
        lexique.append(ligne[0:len(ligne)-1])
    f.close()
    mots=[]
    for L in lexique: #On parcourt les mots qui sont dans la liste
        copie=copy.deepcopy(tirage)
        a=1
        joker=0 #Compteur des jokers utilisés
        for x in L: #Pour chaque mot, on parcourt les lettres qui le compose
            if x in copie:
                copie.remove(x) #si la lettre est dans notre tirage, on la retire car on ne peut plus la réutiliser
            elif '?' in copie and joker==0: #si on a au moins un joker et qu'on en a utilisé aucun
                joker=joker+1
                copie.remove('?')
            else:
                a=0 #si la lettre n'y est pas on change la valeur de a, de sorte que le mot ne puisse pas être pris
        if a==1:
            mots.append(L)
    mots.sort(key=len)
    points=[]
    for m in mots:
        points.append(score(m))
        maximum=max(points)
    return 'plus long mot:', mots[-1], 'maximum de points:', maximum, 'avec ce mot:', mots[points.index(maximum)] #la fonction retourne le mot le plus long , le maximum de points et le mot associé

#EXO 3

valeur={'?':0,'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10}
def score(mot):
    s=0
    for x in mot:
        s=s+valeur[x]
    return s
        
#EXO 4
liste=['z','x','c','v','r','r','t','?']
