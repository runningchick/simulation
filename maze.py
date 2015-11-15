import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

#height and width of the maze
width = 620
height = 620

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Maze')

#starting (x,y) for the red dot
lead_x = 0
lead_y = 55

#initial "velocity" of the red dot if no events (arrow keys) occur
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

block_size = 4
FPS = 30

def loadImage(filename):
    imageSurface = pygame.image.load(filename)
    imageSurface.convert()
    return imageSurface

myimage = loadImage("maze.jpg")

def background(myimage):
    gameDisplay.blit(myimage,[0,0])

#chooses type of font (in this case none), and size of font 
font = pygame.font.SysFont (None, 50)

#displays the strings for winning or losing
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [width/2, height/2])

gameExit = False

#as you hold down each arrow key, the red dot keeps moving in the
#direction that your arrow key is pointing too. 
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
#once you let got of the key, the red dot stops moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            if  event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0
#if you solve the maze, and you pass through width of the display between the y coordinates:
#458 and 492, you win!               
    if (lead_x > width and 458 < lead_y < 492):
        gameDisplay.fill(white)
        message_to_screen("You Win!", red)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
#if you exceed the borders, you lose the game        
    if (lead_x > width or lead_x < 0 or lead_y > height or lead_y < 0):
        gameExit = True
        
                
    lead_x += lead_x_change
    lead_y += lead_y_change
    #displays the maze first
    background(myimage)
    #then draws the red dot over the maze
    pygame.draw.rect(gameDisplay, red, [lead_x,lead_y,block_size,block_size])
    pygame.display.update()
    clock.tick(FPS)

gameDisplay.fill(white)
message_to_screen("You Lose :(", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
