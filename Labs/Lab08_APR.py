# Aden Roof
# 005
# 10/10/2025
# turtle controls with functions

import turtle

## Creating turtle
gmc = turtle.Turtle()
gmc.shape("turtle")
gmc.shapesize(2)
gmc.penup()

## Creating screen object
screen = turtle.Screen()
screen.bgcolor("blue")

## Defining functions
def turn_right():
    gmc.right(30)
def reset():
    gmc.setposition(-250,250)

## event handlers
screen.listen()
screen.onkey(turn_right,"Right")
screen.onkey(reset,"space")
    
## variables
speed = 2
running = True

## game loop
while running:
    gmc.forward(speed)
