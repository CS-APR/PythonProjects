# APR
# 005
# 11/14/2025
# turtle game phase 4

import turtle
import random
import time

## Creating screen object
screen = turtle.Screen()
screen.bgcolor("aqua")
screen.tracer(0)

## Creating turtle
gmc = turtle.Turtle()
gmc.shape("turtle")
gmc.shapesize(2)
gmc.penup()
gmc.color("gray")
#added code
gmc.setposition(-250,250)

#creating goal turtle
goal = turtle.Turtle()
goal.shape("square")
goal.color("orange")
goal.shapesize(3)

#creating scorekeeper turtle
scorekeeper = turtle.Turtle()
scorekeeper.hideturtle()
scorekeeper.penup()
scorekeeper.setposition(-250,250)
scorekeeper.pendown()

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
lives = 2

## game loop
while running:
    #write current lives
    scorekeeper.undo()
    scorekeeper.write(f"Lives: {lives}",font=("Tahoma",26,"normal"))
    
    gmc.forward(speed)
    screen.update()
    time.sleep(0.03)
    #is game over?
    if (lives == 0):
        running = False
        scorekeeper.undo()
        scorekeeper.write(f"No more lives!",font=("Tahoma",26,"normal"))
    #win condition(added for rubric requirment
    if (gmc.distance(goal) < 20):
        running = False
        scorekeeper.undo()
        scorekeeper.write(f"You Win!",font=("Tahoma",26,"normal"))
    for chaser in chaser_list:
        chaser.forward(4)
        if (chaser.distance(gmc) < 10):
            gmc.setposition(-250,250)
            lives -= 1
        if (chaser.distance(0,0) > 250 or chaser.distance(0,0) < -250):
            chaser.left(180)
        
