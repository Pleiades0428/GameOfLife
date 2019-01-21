#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Game of life
Pattern Loader
author: Pleiades
'''

import os

def LoadPatterns():
    patterns = {}
    patternsRoot = 'patterns'
    folders = os.listdir(patternsRoot)
    print(folders)
    for f in folders:
        patterns[f] = []
        patternFiles = os.listdir(patternsRoot + '/' + f)
        for fileName in patternFiles:
            fo = open(patternsRoot + '/' + f + '/' + fileName, "r")
            lines = fo.readlines()
            patternName = os.path.splitext(fileName)[0]
            patternObj = {'name': patternName, 'content': lines}
            patterns[f].append(patternObj)
    return patterns
            
            

def Test():
    p = LoadPatterns()
    print(p)
    print('End')


if __name__ == "__main__":
    Test()
