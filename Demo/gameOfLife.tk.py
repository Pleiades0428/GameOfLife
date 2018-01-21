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
from gameOfLifeWorld import *

width = 100
height = 100
mainForm = None
canvas = None
cellSize = 5
world = None


def PrintScreen():
    global canvas
    for h in range(height):
        for w in range(width):
            tag_pos = '%d_%d' % (h, w)
            if world.cells[h][w] == LIVE:
                found = canvas.find_withtag(tag_pos)
                if len(found) == 0:
                    canvas.create_rectangle(w * cellSize, h * cellSize, (w + 1) *
                                            cellSize, (h + 1) * cellSize, fill='blue', tags=('cell', tag_pos))
            else:
                canvas.delete(tag_pos)


def Update():
    world.Update()


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

    canvas = Canvas(mainForm, bg='black', width=width *
                    cellSize, height=height * cellSize)
    canvas.grid(row=0, column=0)

    Button(mainForm, text='Next', command=BtnNext_OnClick).grid(row=1, column=0)

    global world
    world = GameOfLifeWorld(width, height)
    world.InitRandom()
    PrintScreen()

    StartTimer()

    mainForm.mainloop()


timer = threading.Timer(1, StartTimer)

if __name__ == "__main__":
    Start()
