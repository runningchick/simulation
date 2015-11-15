import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

name = "Planets"
width = 500
height = 500
rw.newDisplay(width, height, name)

sun = dw.loadImage("cat.bmp")
earth = dw.loadImage("cat.bmp")

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(sun, (250, 250))
    dw.draw(earth, (state[0], state[1]))

def updateState(state):
    if (state[1] < 300 and state[0] == 200):
        state[2] = 0
        state[3] = 1
    elif (state[1] == 300 and state[0] < 300):
        state[2] = 1
        state[3] = 0
    elif (state[1] > 200 and state[0] == 300):
        state[2] = 0
        state[3] = -1
    else:
        state[2] = -1
        state[3] = 0
    return(state[0]+state[2], state[1]+state[3], state[2], state[3])

def endState(state):
    if (state[0] > width):
        return True
    else:
        return False

def handleEvent(state, event):
    print(event)
    return(state)
    
initState = (200, 200, 0, 1)

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
