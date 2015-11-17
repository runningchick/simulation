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
comet = dw.loadImage("comet.jpeg")

def updateDisplay(state):
        dw.fill(dw.black)
        dw.draw(sun, (200, 200))
        dw.draw(earth, (state[0], state[1]))
        dw.draw(comet, (state[4], state[5]))

def updateState(state):
    if (50 <= state[1] < 350 and state[0] == 50):
        y_down_velocity = 1
        location = (state[0]+state[2], state[1]+y_down_velocity, state[2], state[3], state[4]+state[6], state[5]+state[7], state[6], state[7])
    elif (state[1] == 350 and 50 <= state[0] < 350):
        x_right_velocity = 1
        location = (state[0]+x_right_velocity, state[1]+state[3], state[2], state[3], state[4]+state[6], state[5]+state[7], state[6], state[7])
    elif (50 < state[1] <= 350 and state[0] == 350):
        y_up_velocity = -1
        location = (state[0]+state[2], state[1]+y_up_velocity, state[2], state[3], state[4]+state[6], state[5]+state[7], state[6], state[7])
    else: 
       x_left_velocity = -1
       location = (state[0]+x_left_velocity, state[1]+state[3], state[2], state[3], state[4]+state[6], state[5]+state[7], state[6], state[7])
    return location

def endState(state):
    if (state[0] == state[4]):
        return True
    else:
        return False

def handleEvent(state, event):
    if event.type == pg.QUIT:
        pg.quit()
        quit()
    if(event.type == pg.KEYDOWN):
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if(event.key == pg.K_LEFT):
            x_velocity = -2
            y_velocity = 0
            return((state[0], state[1], state[2], state[3], state[4], state[5], x_velocity, y_velocity))
        elif(event.key == pg.K_RIGHT):
            x_velocity = 2
            y_velocity = 0
            return((state[0], state[1], state[2], state[3], state[4], state[5], x_velocity, y_velocity))
        elif (event.key == pg.K_UP):
            x_velocity = 0
            y_velocity = -2
            return((state[0], state[1], state[2], state[3], state[4], state[5], x_velocity, y_velocity))
        elif (event.key == pg.K_DOWN):
            x_velocity = 0
            y_velocity = 2
            return((state[0], state[1], state[2], state[3], state[4], state[5], x_velocity, y_velocity))
    return(state)
    
initState = [50, 50, 0, 0, randint(0,499), randint(0,499), randint(-2,2), randint(-2,2)]

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
