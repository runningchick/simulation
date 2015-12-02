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
    sun = 0
    earth = 0
    comet = 0
    impact = 0
    earth_x = 50
    earth_y = 50
    comet_x = randint(0,499)
    comet_y = randint(0,499)
    comet_x_velocity = randint(-2,2)
    comet_y_velocity = randint(-2,2)
    def setImage(self,s,e,c,i):
        self.earth = e
        self.comet = c
        self.sun = s
        self.impact = i
    def __init__(self,s,e,c,i):
        self.setImage(s,e,c,i)

ooInitState = State(my_sun,my_earth,my_comet,my_impact)

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(my_sun, (200, 200))
    dw.draw(my_earth, (state.earth_x, state.earth_y))
    dw.draw(my_comet, (state.comet_x, state.comet_y))

def updateState(state):
    if (50 <= state.earth_y < 350 and state.earth_x == 50):
        y_down_velocity = 1
        location = (state.earth_x, state.earth_y+y_down_velocity, state.comet_x+state.comet_x_velocity, state.comet_y+state.comet_y_velocity, state.comet_x_velocity, state.comet_y_velocity)
    elif (state.earth_y == 350 and 50 <= state.earth_x < 350):
        x_right_velocity = 1
        location = (state.earth_x+x_right_velocity, state.earth_y, state.comet_x+state.comet_x_velocity, state.comet_y+state.comet_y_velocity, state.comet_x_velocity, state.comet_y_velocity)
    elif (50 < state.earth_y <= 350 and state.earth_x == 350):
        y_up_velocity = -1
        location = (state.earth_x, state.earth_y+y_up_velocity, state.comet_x+state.comet_x_velocity, state.comet_y+state.comet_y_velocity, state.comet_x_velocity, state.comet_y_velocity)
    else: 
       x_left_velocity = -1
       location = (state.earth_x+x_left_velocity, state.earth_y, state.comet_x+state.comet_x_velocity, state.comet_y+state.comet_y_velocity, state.comet_x_velocity, state.comet_y_velocity)
    return location

def endState(state):
    if ((state.earth_x <= state.comet_x <= (state.earth_x+70)) and (state.earth_y <= state.comet_y <= (state.earth_y+70)) ):
        dw.draw(my_impact,[0,0])
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
            x_velocity = -2
            y_velocity = 0
            return((state.earth_x, state.earth_y, state.comet_x, state.comet_y, x_velocity, y_velocity))
        elif(event.key == pg.K_RIGHT):
            x_velocity = 2
            y_velocity = 0
            return((state.earth_x, state.earth_y, state.comet_x, state.comet_y, x_velocity, y_velocity))
        elif (event.key == pg.K_UP):
            x_velocity = 0
            y_velocity = -2
            return((state.earth_x, state.earth_y, state.comet_x, state.comet_y, x_velocity, y_velocity))
        elif (event.key == pg.K_DOWN):
            x_velocity = 0
            y_velocity = 2
            return((state.earth_x, state.earth_y
                    , state.comet_x, state.comet_y, x_velocity, y_velocity))
    return(state)

frameRate = 60

rw.runWorld(ooInitState, updateDisplay, updateState, handleEvent, endState, frameRate)
