
import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# Initialize world
name = "Simulation"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")
myimage2 = dw.loadImage("cat.bmp")
myimage3 = dw.loadImage("cat.bmp")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0], state[1]))
    dw.draw(myimage2, (state[4], state[5]))
    dw.draw(myimage3, (state[8], state[9]))

################################################################

# state -> state
def updateState(state):
    return(state[0]+state[2], state[1]+state[3], state[2],state[3], state[4]+state[6], state[5]+state[7], state[6], state[7], state[8]+state[10], state[9]+state[11], state[10], state[11])

################################################################
# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0 or state[1] > height or state[1] < 0):
        return True
    else:
        return False


################################################################
# state -> event -> state
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        newStatex = randint(-2,2)
        newStatey = randint(-2,2)
        newStatex1 = randint(-2,2)
        newStatey1 = randint(-2,2)
        newStatex2 = randint(-2,2)
        newStatey2 = randint(-2,2)
        return((state[0],state[1], newStatex, newStatey, state[4], state[5], newStatex1, newStatey1, state[8], state[9], newStatex2, newStatey2))
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right 
initState = (randint(0,500),randint(0,500), randint(1,2), randint(1,2), randint(0,500), randint(0,500), randint(1,2), randint(1,2), randint(0,500), randint(0,500), randint(1,2), randint(1,2))

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
