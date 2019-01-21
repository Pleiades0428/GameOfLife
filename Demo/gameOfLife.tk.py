#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Game of life
author: Pleiades
'''

import os
import random
import threading
from tkinter import *
from tkinter import ttk
import patternsLoader

from gameOfLifeWorld import *

formWidth = 650
formHeight = 550
canvasHorizentalCount = 100
canvasVerticalCount = 100
mainForm = None
canvas = None
cellSize = 5
world = None
currentPattern = None


def PrintScreen():
    global canvas
    for h in range(canvasHorizentalCount):
        for w in range(canvasHorizentalCount):
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

def BtnStart_OnClick():
    StartTimer()


def StartTimer():
    Loop()
    global timer
    timer = threading.Timer(1, StartTimer)
    timer.start()




def Start():
    global mainForm
    mainForm = Tk()
    mainForm.title('Game Of Life -- Pleiades')
    size = '%dx%d' % (formWidth, formHeight)
    mainForm.geometry(size)
    global canvas

    canvas = Canvas(mainForm, bg='black', width=canvasHorizentalCount *
                    cellSize, height=canvasVerticalCount * cellSize)
    canvas.grid(row=0, column=0)

    Button(mainForm, text='Start', command=BtnStart_OnClick).grid(row=1, column=0, sticky=W, padx=50)
    Button(mainForm, text='Next', command=BtnNext_OnClick).grid(row=1, column=0, sticky=E, padx=50)

    # right frame
    group = LabelFrame(mainForm, text="Patterns", padx=5, pady=5, width=120, height=500)
    group.grid(row=0, column=1, sticky=NW)

    # draw category selector
    lbCategory = Label(group, text='Category:')
    lbCategory.pack(anchor=W)

    global patterns
    patterns = patternsLoader.LoadPatterns()

    cbCategory = ttk.Combobox(group, width=10, state='readonly')
    cateValues = []
    for category in patterns:
        cateValues.append(category)
    cbCategory['value'] = cateValues
    if(len(cateValues) > 0):
        cbCategory.current(0)
    cbCategory.pack(anchor=W)
    def onCategoryChanged(*args):
        currentCategory = cbCategory.get()
        print(currentCategory)
        patValues = []
        for pat in patterns[currentCategory]:
            patValues.append(pat['name'])
        cbPatterns['value'] = patValues
        if(len(patValues) > 0):
            cbPatterns.current(0)
        onPatternChanged()
    cbCategory.bind("<<ComboboxSelected>>", onCategoryChanged)

    # draw pattern selector
    lbPatterns = Label(group, text='Patterns:')
    lbPatterns.pack(anchor=W)
    cbPatterns = ttk.Combobox(group, width=10, state='readonly')
    cbPatterns.pack(anchor=W)
    
    # draw pattern previewer
    patCanvas = Canvas(group, bg='black', width=10 * cellSize, height=10 * cellSize)
    patCanvas.pack()

    # bind pattern canvas redraw event
    def onPatternChanged(*args):
        currentCategory = cbCategory.get()
        currentPatternName = cbPatterns.get()
        print(currentPatternName)
        global currentPattern
        for p in patterns[currentCategory]:
            if(p['name'] == currentPatternName):
                currentPattern = p
        if(currentPattern == None):
            return
        h = 0
        for row in currentPattern['content']:
            w = 0
            for cell in row:
                #print(cell)
                tag_pos = '%d_%d' % (h, w)
                if cell == '1':
                    found = patCanvas.find_withtag(tag_pos)
                    if len(found) == 0:
                        patCanvas.create_rectangle(w * cellSize, h * cellSize, (w + 1) *
                                                cellSize, (h + 1) * cellSize, fill='blue', tags=('cell', tag_pos))
                else:
                    patCanvas.delete(tag_pos)
                w = w + 1
            h = h + 1
            #todo: preview canvas can be dynamic
        
    cbPatterns.bind("<<ComboboxSelected>>", onPatternChanged)
    onCategoryChanged()
    

    # init world
    global world
    world = GameOfLifeWorld(canvasHorizentalCount, canvasVerticalCount)
    world.InitRandom()
    PrintScreen()

    #StartTimer()

    mainForm.mainloop()


timer = threading.Timer(1, StartTimer)

if __name__ == "__main__":
    Start()
