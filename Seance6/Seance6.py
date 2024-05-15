from tkinter import *
from random import *
import numpy as np

graph = [[2,7,3],[3,4,9,10],[5,8,0],[10,1,4,6,0], 
[3,1,6],[2],[3,10,4],[0],[2],[10,1],[3,1,6,9]]

WIDTH=700
HEIGHT=700
pos = np.array([(random()*WIDTH, random()*HEIGHT)
       for i in range(len(graph))])
vit = np.array([((random()-0.5)*10, (random()-0.5)*10)
       for i in range(len(graph))])

class points:
    def __init__(self,p=pos,v=vit):
        self.p=p
        self.v=v

root=Tk()
root.geometry('700x700')
can=Canvas(root,width=700, height=700, background="light goldenrod")
n=len(graph)
point=points()

def draw(can, graph,pos):
    can.delete("all")
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-8,y-8,x+8,y+8,fill="#f3e1d4")
        
draw(can, graph,point.p)

k=100
tau=0.001
n=len(graph)
G=30
def ressort():
    barycentre=[sum(point.p[i][0] for i in range(n)),sum(point.p[i][1] for i in range(n))]
    F=[[[0,0] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            F[i][j][0]=-k*(point.p[i][0]-point.p[j][0])+G/(point.p[i][0]-barycentre[0])**2
            F[i][j][1]=-k*(point.p[i][1]-point.p[j][1])+G/(point.p[i][1]-barycentre[1])**2
    f=[[0,0] for _ in range(n)]
    v=[[0,0] for i in range(n)]
    pos=[[0,0] for i in range(n)]
    for i in range(n):
        for j in range(n):
            f[i][0]=f[i][0]+F[i][j][0]
            f[i][1]=f[i][0]+F[i][j][1]
        v[i][0]=point.v[i][0]+tau*f[i][0]
        v[i][1]=point.v[i][1]+tau*f[i][1]
        pos[i][0]=point.p[i][0]+v[i][0]*tau
        pos[i][1]=point.p[i][1]+v[i][1]*tau
    point.p=pos
    point.v=v
    draw(can,graph,point.p)
    

        
    
root.bind("f", lambda e: ressort())

can.grid(row=1,column=1)   
root.mainloop()