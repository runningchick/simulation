import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

name = "Planets"
width = 500
height = 500
rw.newDisplay(width, height, name)

def loadImage(filename):
    imageSurface = pg.image.load(filename)
    imageSurface.convert()
    return imageSurface

sun = loadImage("sun2.jpeg")
earth = loadImage("earth1.jpeg")

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(sun, (200, 200))
    dw.draw(earth, (state[0], state[1]))

def updateState(state):
    if (50 <= state[1] < 350 and state[0] == 50):
        y_down_velocity = 1
        location = (state[0]+state[2], state[1]+y_down_velocity, state[2], state[3])
    elif (state[1] == 350 and 50 <= state[0] < 350):
        x_right_velocity = 1
        location = (state[0]+x_right_velocity, state[1]+state[3], state[2], state[3])
    elif (50 < state[1] <= 350 and state[0] == 350):
        y_up_velocity = -1
        location = (state[0]+state[2], state[1]+y_up_velocity, state[2], state[3])
    else: 
       x_left_velocity = -1
       location = (state[0]+x_left_velocity, state[1]+state[3], state[2], state[3])
    return location

def endState(state):
    if (state[0] == 1000 and state[1] == 1000):
        return True
    else:
        return False

def handleEvent(state, event):
    print(event)
    return(state)
    
initState = [50, 50, 0, 0]

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
