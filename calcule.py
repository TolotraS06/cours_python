#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:01:08 2023

@author: nemos06
"""

from tkinter import *
from math import *

def evaluer (event):
    chaine.configure(text = "result = " + str(eval(entree.get())))
    

fen = Tk()
entree = Entry(fen)
entree.bind("<Return>", evaluer)
chaine = Label(fen)
entree.pack ()
chaine.pack ()

fen.mainloop ()
