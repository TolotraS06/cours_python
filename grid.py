#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:41:25 2023

@author: nemos06
"""

from tkinter import *

fen = Tk ()

Label(fen,text="first").grid(row=1,sticky=E) 
Label(fen,text="second").grid(row=2,sticky=E)
Label(fen,text="third").grid(row=3,sticky=E)

entry1 = Entry(fen).grid(row=1,column=2)
entry2 = Entry(fen).grid(row=2,column=2)
entry3 = Entry(fen).grid(row=3,column=2)

can1 = Canvas(fen, width =160, height =160, bg ='white')
photo = PhotoImage(file ='pirate.png')
item = can1.create_image(80, 80, image =photo)

can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)

fen.mainloop ()

