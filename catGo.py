# from trepan.api import debug

# import pdb
# pdb.set_trace()

import runWorld as rw
import drawWorld as dw


# Initialize world
name = "Cat Go!"
width = 500
height = 500
rw.newDisplay(width, height, name)

# World state will be single x coordinate at left edge of world
initState = 0

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")

#type - state -> image (IO)
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state, height/2))

#state -> state
# We'll update the state on each tick by incrementing the x stateinate
def updateState(state):
    return((state[0]+state[1],state[1]))

# We'll terminate when the x stateinate reaches the screen edge

#state -> bool
def endState(state):
    if (state >= width):
        return True
    else:
        return False


# For now we'll handle events just logging them to the console
#state ->  event -> state
def handleEvent(state, event):
    print(event)
    return(state)

# Off we go! Start the cat at the left edge, and try for 30 FPS
#world state will be single x coordinate at the left edgeof the world
#x coord and delta x
frameRate = 60
initState = (0,1)
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
