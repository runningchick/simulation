import runWorld as rw
import drawWorld as dw
import pygame as pg
import time
from random import randint

## Class Declaration

#initState = [50, 50, randint(0,499), randint(0,499), randint(-2,2), randint(-2,2)]

name = "Planets"
width = 500
height = 500
rw.newDisplay(width, height, name)

def loadImage(filename):
    imageSurface = pg.image.load(filename)
    imageSurface.convert()
    return imageSurface

my_sun = loadImage("sun2.jpeg")
my_earth = loadImage("earth1.jpeg")
my_comet = loadImage("comet.png")
my_impact = dw.loadImage("impact.jpg")

class State:
    _sun = None
    _earth = None
    _comet = None
    _impact = None
    earth_x = 50
    earth_y = 50
    comet_x = randint(0,499)
    comet_y = randint(0,499)
    comet_x_velocity = randint(-2,2)
    comet_y_velocity = randint(-2,2)
    def setImage(self,sun,earth,comet,impact):
        self._earth = earth
        self._comet = comet
        self._sun = sun
        self._impact = impact
    def __init__(self,sun,earth,comet,impact):
        self.setImage(sun,earth,comet,impact)

ooInitState = State(my_sun,my_earth,my_comet,my_impact)

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(state._sun, (200, 200))
    dw.draw(state._earth, (state.earth_x, state.earth_y))
    dw.draw(state._comet, (state.comet_x, state.comet_y))

def updateState(state):
    if (50 <= state.earth_y < 350 and state.earth_x == 50):
        state.earth_y += 1
    elif (state.earth_y == 350 and 50 <= state.earth_x < 350):
        state.earth_x += 1
    elif (50 < state.earth_y <= 350 and state.earth_x == 350):
        state.earth_y -= 1
    else:
       state.earth_x -= 1
    state.comet_x += state.comet_x_velocity
    state.comet_y += state.comet_y_velocity
    return state

def endState(state):
    if ((state.earth_x <= state.comet_x <= (state.earth_x+70)) and (state.earth_y <= state.comet_y <= (state.earth_y+70))):
        dw.draw(state._impact,[0,0])
        pg.display.update()
        time.sleep(2)
        font = pg.font.SysFont (None, 50)
        end_text = font.render("By: Cody, Emma, Corey", True, dw.green)
        dw.fill(dw.black)
        dw.draw(end_text, [100, height/2])
        pg.display.update()
        time.sleep(2)
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
            state.comet_x_velocity = -2
            state.comet_y_velocity = 0
        elif(event.key == pg.K_RIGHT):
            state.comet_x_velocity = 2
            state.comet_y_velocity = 0
        elif (event.key == pg.K_UP):
            state.comet_x_velocity = 0
            state.comet_y_velocity = -2
        elif (event.key == pg.K_DOWN):
            state.comet_x_velocity = 0
            state.comet_y_velocity = 2
    return state

frameRate = 60

rw.runWorld(ooInitState, updateDisplay, updateState, handleEvent, endState, frameRate)
