from random import randint

class polynome_Z_q :
    def __init__(self,q,n,coeffs):
        self.q=q
        self.n=n
        self.c=coeffs
    
    def redu(self):
        for i in range(len(self.c)):          
            if i>=self.n:
                self.c[i%self.n]=self.c[i%self.n]+self.c[i]*(-1)**(i//self.n)
        self.c=self.c[:self.n] #réduction des puissances, remplacement par -1 et nouvelle liste de coeffs réduite
        
        for i in range(len(self.c)):
            self.c[i]=self.c[i]%self.q
    
    def add(self,other):
        L=[]
        for i in range(len(self.c)):
            L.append(self.c[i]+other.c[i])
        P=polynome_Z_q(self.q,self.n,L)
        return(P)
    
    def mul(self,other):
        L=[0 for _ in range(len(self.c)+len(other.c))]
        for i in range(len(self.c)):
            for j in range(len(other.c)):
                L[i+j]=self.c[i]*other.c[j]
        P=polynome_Z_q(self.q,self.n,L)
        P.redu()
        return(P)
    
    def scalar(self,c):
        self.c=c*self.c

    
    def rescale(self,r):
        coeffs=[]
        for i in range(len(self.c)):
            coeffs.append(self.c[i]%r)
        P=polynome_Z_q(r,self.n,coeffs)
        return(P)
    
    def fscalar(self,r,a):
        coeffs=[]
        for i in range(len(self.c)):
            coeffs.append(round(self.c[i]*a)%r)
        Q=polynome_Z_q(self.q,self.n,coeffs)
        return(Q)
    
    def __str__(self):
        if self.n!=0:
            polynome=f"{self.c[0]}"
            for i in range(1,len(self.c)):
                if self.c[i]!=0:
                    polynome=polynome+f"+{self.c[i]}*X^{i}"
    
        return(polynome)            
     
if __name__=='__main__':
    A=polynome_Z_q(4,5,[1,4,7,2,7,8])
    A.redu()
    print(A)
    B=polynome_Z_q(4,7,[1,2,3,2,1,3])
    B.redu()
    print(B) #B respecte les conditions q et n, il n'est pas réduit
    C=A.add(B)
    print(C)
    D=A.mul(B)
    print(D)
    
    E=polynome_Z_q(4,5,[1,4,7,2,7,8])
    E.redu()
    E.scalar(3)
    print("E",E)
