#Aden Roof
# 005
# 11/7/2025
# part 2 turtle methods

import turtle
import random

#create turtle
robber = turtle.Turtle()
robber.shape("arrow")
robber.color("Black")
robber.shapesize(2)

#create screen
screen = turtle.Screen()

#make lsit
police_squad = []

#fill list
for i in range(3):
    cop = turtle.Turtle()
    police_squad.append
    cop.shape("circle")
    cop.color("Blue")
    cop.shapesize(2)
    cop.penup()
    cop.setposition(random.randint(-150,150),random.randint(-150,150))
    
def change_color():
    robber.color("Red")

#event handlers
screen.listen()
screen.onkey(change_color,"r")


    
