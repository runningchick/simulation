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
    if (200 <= state[1] < 300 and state[0] == 200):
        y_down_velocity = 1
        location = (state[0]+state[2], state[1]+y_down_velocity, state[2], state[3])
    elif (state[1] == 300 and 200 <= state[0] < 300):
        x_right_velocity = 1
        location = (state[0]+x_right_velocity, state[1]+state[3], state[2], state[3])
    elif (200 < state[1] <= 300 and state[0] == 300):
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
    
initState = [200, 200, 0, 0]

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
