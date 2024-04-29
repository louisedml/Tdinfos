from tkinter import *
from random import *


def score(x,y):
    if (x-200)**2+(y-200)**2<=15**2:
        return 6
    elif (x-200)**2+(y-200)**2<=35**2:
        return 5
    elif (x-200)**2+(y-200)**2<=75**2:
        return 4
    elif (x-200)**2+(y-200)**2<=105**2:
        return 3
    elif (x-200)**2+(y-200)**2<=135**2:
        return 2
    elif (x-200)**2+(y-200)**2<=165**2:
        return 1
    else:
        return 0
    
class tirer:
    def __init__(self,nombre=0,points=0):
        self.nb=nombre
        self.points=points

def tir(n=5):
    if sc.nb<5:
        if n+sc.nb<=5 and n!=1:
            a=n
        elif n+sc.nb>=5 and n!=1:
            a=5-sc.nb
        elif n==1:
            a=1
    else:
        a=0
    sc.nb=sc.nb+a
    for i in range(a):
        x=400*random()
        y=400*random()
        c.create_oval(x-7,y-7,x+7,y+7,fill="black")
        sc.points=sc.points+score(x,y)
    if sc.nb==5:
        but1['state']=DISABLED
    
    s.config(text=f"Score: {sc.points}")
    
    
root=Tk()
root.geometry('400x430')
c=Canvas(root,width=400, height=400, background="red")
c.create_oval(35,35,365,365,fill="ivory",outline="red")
c.create_oval(65,65,335,335,fill="ivory",outline="red")
c.create_oval(95,95,305,305,fill="ivory",outline="red")
c.create_oval(125,125,275,275,fill="ivory",outline="red")
c.create_oval(155,155,245,245,fill="red",outline="red")
c.create_oval(185,185,215,215,fill="ivory",outline="red")
c.create_line(0,200,400,200,fill="red")
c.create_line(200,0,200,400, fill="red")
c.create_text(200,195,fill="red",text="6",width=30)
c.create_text(200,165,fill="ivory",text="5")
c.create_text(200,135,fill="red",text="4")
c.create_text(200,105,fill="red",text="3")
c.create_text(200,75,fill="red",text="2")
c.create_text(200,45,fill="red",text="1")
c.grid(row=1,column=1,columnspan=2)
but1=Button(root,text="Feu!", command=tir)
but1.grid(row=2,column=1,sticky=W)
but2=Button(root,text="Quitter",command=root.destroy)
but2.grid(row=2,column=2,sticky=E)
sc=tirer()
s=Label(root,text=f"Score:0")
s.grid(row=2,column=1)
root.bind("f", lambda e: tir(1))
root.mainloop()