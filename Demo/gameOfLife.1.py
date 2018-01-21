#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Game of life
author: Pleiades
'''

import os
import random
#import functools

width = 60
height = 15
screen = []


def Init():
    global screen
    screen = [['#' if random.random() > 0.8 else ' ' for i in range(width)]
              for j in range(height)]


def PrintScreen():
    print('|\n'.join([' '.join(line) for line in screen]))


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


def Start():
    os.system("cls")
    print('== Game of Life ==')
    print('Author: Pleiades')
    print('Press any key...')
    input()
    os.system("cls")
    Init()
    PrintScreen()
    c = input()
    while c != 'q':  # todo:
        os.system("cls")
        Loop()
        c = input()
    print('End')


if __name__ == "__main__":
    Start()
