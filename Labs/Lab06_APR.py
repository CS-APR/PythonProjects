# APR
# 005
# 9/26/2025
# lab 06 Turtle Spiral

import turtle

#turtle construction
cherry = turtle.Turtle()
cherry.shape('turtle')
cherry.shapesize(2)
cherry.color('white')
cherry.width(6)

#background
window = turtle.Screen()
window.bgcolor('black')

#var declaration
length = 10
i= 0
#drawing loop
for i in range(20):
    cherry.forward(length)
    cherry.left(360/10)
    
    #color switching
    if i % 3 == 0:
        cherry.color('red')
    if i % 3 == 1:
        cherry.color('blue')
    if i % 3 == 2:
        cherry.color('green')
    if i % 3 == 3:
        cherry.color('yellow')
        
    #var updates
    i+1
    length = length+5
