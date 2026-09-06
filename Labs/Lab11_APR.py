# Aden Roof
# 005
# 10/24/2025
# turtle game phase 2

import turtle
import random
import time

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
    chaser.shape("triangle")
    chaser.color("sea green")
    chaser.shapesize(2)
    chaser.penup()
    random_x = random.randint(-200,200)
    random_y = random.randint(-200,200)
    chaser.setposition(random_x, random_y)
    random_angle = random.randint(1,360)
    chaser.left(random_angle)

## Creating screen object
screen = turtle.Screen()
screen.bgcolor("aqua")
screen.tracer(0)

## Defining functions
def turn_right():
    gmc.right(30)
def turn_left():
    gmc.left(30)
def reset():
    gmc.setposition(-250,250)
def speed_up():
    global speed
    if speed < 5:
        speed += 1
def slow_down():
    global speed
    if speed > 1:
        speed -= 1

## event handlers
screen.listen()
screen.onkey(turn_right,"Right")
screen.onkey(turn_left,"Left")
screen.onkey(reset,"space")
screen.onkey(speed_up,"Up")
screen.onkey(slow_down,"Down")
    
## variables
speed = 5
running = True

## game loop
while running:
    gmc.forward(speed)
    screen.update()
    time.sleep(0.03)
    for chaser in chaser_list:
        chaser.forward(4)
        if (chaser.distance(0,0) > 250 or chaser.distance(0,0) < -250):
            chaser.left(180)
        
