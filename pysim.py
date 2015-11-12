import runWorld as rw
import drawWorld as dw
import pygame as pg

# Initialize Simulation
name = "Simulation"
width = 500
height = 500
rw.newDisplay(width, height, name)

image = dw.loadImage("cat.bmp")

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(image, (state[0], height/2))

def updateState(state):
    if (state >= width):
        return(state[0]+state[1],state[1])
    else:
        return(state[0]-state[1],state[1])

def endState(state):
    if (state[0] > width or state[0] < 0):
        return True
    else:
        return False
    
def handleEvent(state, event):
    return(state)
        

frameRate = 60
initState = (0, 1)

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)

















































