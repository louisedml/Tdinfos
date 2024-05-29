import struct
from math import floor

f = open("the_wall.wav", "rb")
data = f.read()
head=data[0:39]
print(head)



def echantillon(data):
    nb_canal=data[22]+data[23]
    l=len(data[44:])
    print(l)
    l=l/4
    d=[]
    g=[]
    for i in range(int(l)):
        s=struct.unpack_from("hh",data,44+4*i)
        d.append(s[0])
        g.append(s[1])
    return d,g

d,g=echantillon(data)



def dedouble(d,g,nom):
    f=open(nom,"wb")
    l=len(d)
    f.write(b"RIFF")
    f.write(struct.pack("I",44+l*4-8))
    f.write(b"WAVEfmt ")
    f.write(struct.pack("IHHIIHH",16,1,2,44100,176400,4,16))
    f.write(b"data")
    f.write(struct.pack("I",l*4))
    for i in range(l):
        if i%2==0:
            f.write(struct.pack("hh",g[i],d[i]))
    f.close()
    return(f)

# musique accélérée par 2 (perte d'une donnée sur deux)

def interpolation(d,g):
    d1=[]
    g1=[]
    l=len(d)
    for i in range(l-1):
        d1.append(d[i])
        d1.append(floor((d[i]+d[i+1])/2))
        g1.append(g[i])
        g1.append(floor((g[i]+g[i+1])/2))
    d1.append(d[l-1])
    g1.append(g[l-1])
    return d1,g1

d1,g1=interpolation(d,g)
    
def creation(d,g,nom):
    f=open(nom,"wb")
    l=len(d)
    f.write(b"RIFF")
    f.write(struct.pack("I",44+l*4-8))
    f.write(b"WAVEfmt ")
    f.write(struct.pack("IHHIIHH",16,1,2,44100,176400,4,16))
    f.write(b"data")
    f.write(struct.pack("I",l*4))
    for i in range(l):
        f.write(struct.pack("hh",g[i],d[i]))
    f.close()
    return(f)
    
#fichier original reconstitué
creation(d,g,"recons.wav")

#fichier avec 1 sur donnée sur 2 pour chaque canal
dedouble(d,g,"dedoublé.wav")

#fichier interpolé
creation(d1,g1,"interpolé.wav")


    
    
    
    

