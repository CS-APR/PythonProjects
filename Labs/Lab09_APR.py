# Aden Roof
# 005
# 10/17/2025
# turtle game phase 1

import turtle
import random

## Creating turtle
gmc = turtle.Turtle()
gmc.shape("turtle")
gmc.shapesize(2)
gmc.penup()
gmc.color("gray")

## creating chaser turtles
chaser_list = []
for i in range(5):
    chaser = turtle.Turtle()
    chaser_list.append(chaser)
    chaser.shape("square")
    chaser.color("sea green")
    chaser.shapesize(2)
    chaser.penup()
    random_x = random.randint(-200,200)
    random_y = random.randint(-200,200)
    chaser.setposition(random_x, random_y)

## Creating screen object
screen = turtle.Screen()
screen.bgcolor("aqua")

## Defining functions
def turn_right():
    gmc.right(30)
def turn_left():
    gmc.left(30)
def reset():
    gmc.setposition(-250,250)

## event handlers
screen.listen()
screen.onkey(turn_right,"Right")
screen.onkey(turn_left,"Left")
screen.onkey(reset,"space")
    
## variables
speed = 5
running = True

## game loop
while running:
    gmc.forward(speed)
