#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Game of life World
author: Pleiades
'''

#import os
import random

LIVE = '#'
DEAD = ' '

class GameOfLifeWorld:

    width = 100
    height = 100
    cells = []


    def __init__(self, width, height):
        self.width = width
        self.height = height

    def InitRandom(self):
        self.cells = [[LIVE if random.random() > 0.8 else DEAD for i in range(self.width)]
                       for j in range(self.height)]

    def TryGetCell(self, h, w):
        return self.cells[min(h, self.height - 1)][min(w, self.width - 1)]

    def GetNearbyCellsCount(self, h, w):
        nearby = [self.TryGetCell(h + dy, w + dx) for dx in [-1, 0, 1]
                  for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
        return len(list(filter(lambda x: x == LIVE, nearby)))

    def GetNewCell(self, h, w):
        count = self.GetNearbyCellsCount(h, w)
        return LIVE if count == 3 else (DEAD if count < 2 or count > 3 else self.cells[h][w])

    def Update(self):
        self.cells = [[self.GetNewCell(h, w) for w in range(self.width)]
                  for h in range(self.height)]


if __name__ == "__main__":
    w = 10
    h = 10
    world = GameOfLifeWorld(w, h)
    world.InitRandom()
    print('\n'.join(' '.join(line) for line in world.cells))
    world.Update()
    print('\n'.join(' '.join(line) for line in world.cells))
