from math import gcd
#exercice 1

class Fraction:
    def __init__(self,a,b=1):
        """Crée une fraction a/b"""
        self.num=a
        self.den=b
    def add(self,self2):
        """additionne deux fractions"""
        return Fraction(self.num*self2.den + self2.num*self.den, self.den*self2.den)
    def mult(self,self2):
        """multiplie deux fractions"""
        return Fraction(self.num*self2.num, self.den*self2.den).simplify()
    def simplify(self):
        """Simplifie une fraction en cherchant le dénominateur commun du numérateur et du dénominateur"""
        return Fraction(self.num//gcd(self.num,self.den),self.den//gcd(self.num,self.den))
        
    def toString(self):
        return f"({self.num} / {self.den})"

if __name__=='__main__':
    f=Fraction(4,5)
    print (f.toString())
    g=Fraction(3,2)
    print (g.toString())
    s=f.add(g)
    print('somme',s.toString())
    m=f.mult(g)
    print('multiplication', m.toString())
    q=Fraction(75,5)
    k=q.simplify()
    print('simplification', k.toString())
    
#exercice 2
assert (Fraction(1,2).mult(Fraction(1,5))).toString()==Fraction(1,10).toString()

#exercice 3
def H(n):
    h=Fraction(0)
    for k in range(1,n):
        h=h.add(Fraction(1,k))
        h=h.simplify()
    return h.toString()

print(H(1000))
        
#exercice 4

def leibnitz(n):
    s=Fraction(1,1)
    for k in range(1,n):
        s=s.add(Fraction((-1)**k,2*k+1))
        s.simplify()
    return s.toString()

print(leibnitz(1000))

#exercice 5

class polynomial:
    """Classe permettant de manipuler des polynômes"""
    def __init__(self,L):
        self.coeff=L
    def __str__(self):
        if self.coeff[0]!=0:
            P=f"({self.coeff[0]}+"
            if self.coeff[1]!=0:
                P=P+f"{self.coeff[1]}*X+"
        else:
            if self.coeff[1]!=0:
                P=f"({self.coeff[1]}*X+"
            else:
                P=f"(" 
        for k in range(2,len(self.coeff)-1):
            if self.coeff[k]!=0:
                P=P+f"{self.coeff[k]}*X**{k}+"
        P=P+f"{self.coeff[len(self.coeff)-1]}*X**{len(self.coeff)-1})"
        return P
    def add(self,other):
        """Prend en argument un deuxième polynôme et renvoit la somme des deux"""
        m=min(len(self.coeff),len(other.coeff))
        L=[]
        for k in range(m):
            L=L+[self.coeff[k]+other.coeff[k]]
        if len(other.coeff)>m:
            for k in range(m+1, len(other.coeff)-1):
                L=L+[other.coeff[k]]
        elif len(self.coeff)>m:
            for k in range(m+1, len(self.coeff)-1):
                L=L+[self.coeff[k]]
        return polynomial(L)
    def deriv(self):
        """Dérive un polynôme"""
        L=[]
        for i in range(1,len(self.coeff)):
            L=L+[self.coeff[i]*i]
        return polynomial(L)
    def integrate(self,constante):
        """intègre un polynôme"""
        L=[constante]
        for i in range(len(self.coeff)):
            L=L+[self.coeff[i]/(i+1)]
        return polynomial(L)
        
            
        
if __name__=='__main__':
    p1=polynomial([0,0,3,4])
    print('p1',p1)
    p2=polynomial([5,0,3,4,0,6])
    print('p2',p2)
    p3=polynomial([7,8,1,4])
    print('p3',p3)
    p4=p2.add(p3)
    print('somme de p2 et p3',p4)
    p5=p1.add(p2)
    print('somme de p2 et p1',p5)
    p6=p2.deriv()
    print('p6 dérivée de p2',p6)
    p7=p6.integrate(5)
    print('intégration de p6 avec 5 comme cst',p7)
