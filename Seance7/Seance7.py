from tkinter import *
from random import randint, random

graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]
pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])
COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']
color=[i for i in range(len(graph))]


class graphes:
    def __init__(self,p=pos,g=graph,c=color):
        self.p=p
        self.g=g
        self.c=c


graph2 = [[2], [], [4], [1], [6], [3], [7], [5]]
pos2= [[100, 200], [450, 200], [150, 200], [400, 200], [200, 200], [350, 200], [250, 200], [300, 200]]

root=Tk()
can=Canvas(root,width=700, height=700)

def draw(graph,pos,couleur):
    can.delete("all")
    for i in range(len(pos)):
        for j in graph[i]:
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
        
    for i in range(len(pos)):
        x=pos[i][0]
        y=pos[i][1]
        can.create_oval(x-8,y-8,x+8,y+8,fill=COLORS[couleur[i]])
        can.create_text(x,y,text=f"{i}")
    
def min_local(i,graph,color):
    mini=i
    for j in graph[i]:
        if j<mini:
            mini=j
    color[i]=color[mini]
    for j in graph[i]:
        color[j]=color[mini]
    for j in range(len(graph)):
        if i in graph[j]:
            color[j]=color[mini]
def g1():
    graphe1=graphes()
    draw(graphe1.g,graphe1.p,graphe1.c)
    can.create_text(300,20,text='appuyez sur m')
    min_local(6,graphe1.g,graphe1.c)
    root.bind("m", lambda e: draw(graphe1.g,graphe1.p,graphe1.c))


def connex(graph,color):
    L=[i for i in range(len(graph))]
    L.sort(key= lambda i: color[i])
    for i in L:
        min_local(i,graph,color)
        
def g2():
    graphe2=graphes()
    draw(graphe2.g,graphe2.p,graphe2.c)
    can.create_text(300,20,text='appuyez sur c')
    connex(graphe2.g,graphe2.c)
    root.bind("c", lambda e: draw(graphe2.g,graphe2.p,graphe2.c))

root.bind("a", lambda e: g1()) #pour lancer l'exemple du minimum local au point 6
root.bind("b", lambda e: g2()) #pour lancer l'exemple du graphe connexe


def pos_grille(n,p):
    pos=[[] for _ in range(n**2)]
    l=600/n
    graph=[[] for _ in range(n**2)]
    for a in range(n**2):
        q=a//n
        r=a%n
        pos[a]=[r*l+l/2,(q+1)*l]
        r=[random() for _ in range(2)]
        if (r[0]>p and (a+1)%n!=0):
            graph[a].append(a+1)
        if r[1]>p and a+n<n**2:
            graph[a].append(a+n)
    
    col=[randint(1,13) for _ in range(n**2)]
    return([pos,graph,col])

pos3=pos_grille(50,0.4)[0]
graph3=pos_grille(50,0.4)[1]
color3=pos_grille(50,0.4)[2]

def draw2(graph,pos,couleur):
    can.delete("all")
    for i in range(len(pos)):
        for j in graph[i]:
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
        
    for i in range(len(pos)):
        x=pos[i][0]
        y=pos[i][1]
        can.create_oval(x-4,y-4,x+4,y+4,fill=COLORS[couleur[i]])



def g3():
    graphe3=graphes(pos3,graph3,color3)
    draw2(graphe3.g,graphe3.p,graphe3.c)
    can.create_text(300,20,text='appuyez sur c')
    connex(graphe3.g,graphe3.c)
    root.bind("c", lambda e: draw2(graphe3.g,graphe3.p,graphe3.c))

root.bind("c", lambda e: g3()) #pour lancer l'exemple de la grille connexe
can.grid(row=1,column=1)
root.mainloop()