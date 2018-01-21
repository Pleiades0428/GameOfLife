#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Game of life
author: Pleiades
'''

import os
import random
from tkinter import *
import threading

width = 100
height = 100
screen = []
mainForm = None
canvas = None
cellSize = 5

def Init():
    global screen
    screen = [['#' if random.random() > 0.8 else ' ' for i in range(width)]
              for j in range(height)]


def PrintScreen():
    #print('Enter PrintScreen()')
    global canvas
    canvas.delete('cells')
    #canvas.create_rectangle(15, 15, cellSize, cellSize, fill='blue', tags='cells')
    for h in range(height):
        for w in range(width):
            if screen[h][w] == '#':
                canvas.create_rectangle(w * cellSize, h * cellSize, (w + 1) * cellSize, (h + 1) * cellSize, fill='blue', tags='cells')
                #pass


def TryGetCell(h, w):
    return screen[min(h, height - 1)][min(w, width - 1)]


def GetNearbyCellsCount(h, w):
    nearby = [TryGetCell(h + dy, w + dx) for dx in [-1, 0, 1]
              for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
    return len(list(filter(lambda x: x == '#', nearby)))


def GetNewCell(h, w):
    count = GetNearbyCellsCount(h, w)
    return '#' if count == 3 else (' ' if count < 2 or count > 3 else screen[h][w])


def Update():
    global screen
    screen = [[GetNewCell(h, w) for w in range(width)]
              for h in range(height)]


def Loop():
    Update()
    PrintScreen()

def BtnNext_OnClick():
    Loop()

def StartTimer():
    Loop()
    global timer
    timer = threading.Timer(1, StartTimer)
    timer.start()

def Start():
    global mainForm
    mainForm = Tk()
    size = '%dx%d' % (width * cellSize, height * cellSize + 50)
    mainForm.geometry(size)
    global canvas

    canvas = Canvas(mainForm, bg='black', width=width * cellSize, height=height * cellSize)
    canvas.grid(row=0,column=0)
    Button(mainForm, text='Next', command=BtnNext_OnClick).grid(row=1,column=0)
    
    Init()
    PrintScreen()

    StartTimer()

    mainForm.mainloop()

timer = threading.Timer(1, StartTimer)

if __name__ == "__main__":
    Start()
