from math import gcd
#exercice 1

class Fraction:
    def __init__(self,a,b=1):
        """Crée une fraction a/b"""
        self.num=a
        self.den=b
    def add(self,self2):
        return Fraction(self.num*self2.den + self2.num*self.den, self.den*self2.den)
    def mult(self,self2):
        return Fraction(self.num*self2.num, self.den*self2.den)
    def simplify(self):
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
    k=m.simplify()
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

print(H(10000))
        
#exercice 4

def leibnitz(n):
    s=Fraction(1,1)
    for k in range(1,n):
        s=s.add(Fraction((-1)**k,2*k+1))
        s.simplify()
    return s.toString()

print(leibnitz(10000))

#exercice 5

class polynomial:
    """Retourne un polynôme à partir d'une liste de coefficients"""
    def __init__(self,L):
        self.coeff=L
    def __str__(self):
        P=f"("
        for k in range(len(self.coeff)-1):
            P.append(f"{self.coeff[k]}*X**{k}")
        P.append(f")")
        return P
    def add(self,self2):
        m=max(len(self.coeff,self2.coeff))
        
if __name__=='__main__':
    p=polynomial([1,2,3,4])
    print(p.str())
    
