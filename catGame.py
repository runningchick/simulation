import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

width = 620
height = 620
name = "Cat Game"
rw.newDisplay(width, height, name)

myimage = dw.loadImage("cat.bmp")

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0],state[1]))

def updateState(state):
    return((state[0]+state[2],state[1]+state[3],state[2],state[3]))

def endState(state):
    if (state[0] >= width or state[0] <= 0 or state[1] >= height or state[1] <= 0):
        return True
    else:
        return False

def handleEvent(state, event):
    if (event.type == pg.QUIT):
        endState = True
    if (event.type == pg.KEYDOWN):
        if (event.key == pg.K_LEFT):
            newStatex = -randint(1,5)
            newStatey = 0
            return(state[0],state[1],newStatex,newStatey)
        elif (event.key == pg.K_RIGHT):
            newStatex = randint(1,5)
            newStatey = 0
            return(state[0],state[1],newStatex,newStatey)
        elif (event.key == pg.K_UP):
            newStatex = 0
            newStatey = -randint(1,5)
            return(state[0],state[1],newStatex,newStatey)
        elif (event.key == pg.K_DOWN):
            newStatex = 0
            newStatey = randint(1,5)
            return(state[0], state[1], newStatex, newStatey)
    else:
        return(state)

initState = (randint(0,200),randint(0,200),randint(1,5),randint(1,5))

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
