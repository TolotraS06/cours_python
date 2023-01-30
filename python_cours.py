#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:41:52 2023

@author: nemos06
"""

from tkinter import *
from random import randrange

def drawline ():
    "trace une ligne dans le canevas"
    global x1,y1,x2,y2,coul
    can1.create_line (x1,y1,x2,y2,width=2, fill=coul)
    
    y2,y1 = y2 + 10,y1-10


def changecolor ():
    "changement aleatoire de la couleur du trace"
    global coul
    pal= ['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8)
    coul = pal [c]
    
    
x1,y1,x2,y2 = 10,190,190,10
coul = 'dark green'    
    
fen1 = Tk()
can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)

#tex1 = Label (fen1,text ='Bonjour tout le monde', fg = 'red')
#tex1.pack ()

bou1 = Button (fen1, text = 'Quitter', command = fen1.quit)
bou1.pack (side=BOTTOM)
bou2 = Button (fen1, text = 'tracer une ligne', command = drawline)
bou2.pack ()
bou3 = Button (fen1, text = 'autre couleur', command = changecolor)
bou3.pack ()
fen1.mainloop()

fen1.destroy ()