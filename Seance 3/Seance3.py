#Exercice 1

#Exercice 2

class Tree:
    """Classe premettant de créer et d'utiliser des arbres"""
    def __init__(self, label, *children):
        self._racine=label
        self._children=children      
   
    def label(self):
        """Renvoit la racine de l'arbre"""
        return str(self._racine)
    
    def children(self):
        """Renvoit un tuple contenant les racines de chaques sous arbre"""
        chi=[child.label() for child in self._children]
        chi=tuple(chi)
        return chi
    
    def nb_children(self):
        """renvoit le nombre de sous arbre"""
        return len(self._children)
    
    def child(self,i:int):
        """Renvoit le ième sous arbre"""
        return self._children[i]._racine
    
    def is_leaf(self):
        """Renvoit True si l'arbre n'a pas de descendants, si c'est une feuille"""
        if self._children==():
            return True
        else:
            return False
        
    def depth(self):
        """Renvoit la profondeur maximale de l'arbre"""
        if self._children==():
            return 0
        else:
            m=0
            for k in range(len(self._children)):
                a=self._children[k].depth()
                if a>=m:
                    m=a
            return m+1
        
    def __eq__(self, object):
        """Compare deux arbres.

        Prends en argument un deuxième arbre
        Renvoit True si les deux arbres sont identiques"""
        if self._racine==object._racine and self._children==object._children:
            return True
        else:
            return False
        
        
    def __str__(self):
        if self._children:
            children_str = ', '.join(str(child) for child in self._children)
            return f"{self._racine}({children_str})"
        else:
            return str(self._racine)
    
    def deriv(self, var):
        """Dérive l'arbre par rapport à une variable donnée en argument"""
        if self.is_leaf():
            if self.label() == var:
                return Tree('1')
            else:
                return Tree('0')
        elif self.label() == '+':
            a=self._children[0].deriv(var)
            b=self._children[1].deriv(var)
            return Tree('+', a, b)
        elif self.label() == '*':
            u=self._children[0]
            v=self._children[1]
            ud=u.deriv(var)
            vd=v.deriv(var)
            return Tree('+', Tree('*', ud, v), Tree('*', u, vd))
        
        
if __name__=='__main__':
    f=Tree('f',Tree('a'),Tree('b'))
    a=f.children()
    print('les enfants sont',a)
    b=f.label()
    print('la racine est',b)
    c=f.nb_children()
    print('le nombre d enfants est',c)
    d=f.child(0)
    print('l enfant demandé est',d)
    e=f.is_leaf()
    print('réponse à la question: est ce que c est une feuille?',e)
    g=f.depth()
    print('la profondeur est',g)
    h=Tree('+',Tree('a'),Tree('X')).deriv('X')
    print(h)
    i=Tree('*',Tree('X'),Tree('X'))
    i2=Tree('*',Tree('3'),i)
    i3=Tree('*',Tree('5'),Tree('X'))
    i4=Tree('+',i3,Tree('7'))
    I=Tree('+',i2,i4)
    ii=I.deriv('X')
    print(ii)
    k=Tree('a')
    l=k.deriv('X')
    print(l)
    m=Tree('0')
    print(m)
    

    