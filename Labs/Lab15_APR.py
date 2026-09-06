#APR
#12/5/25
#005
#turtle white board

import turtle

###create screen objects
whiteboard = turtle.Screen()
marker = turtle.Turtle()
marker.speed(0)
marker.shapesize(3)
marker.width(3)

###marker functions
def clear(functions, mouse_button):
    marker.clear()

def change_color(functions, mouse_button):
    if marker.color()[0] == "black":
        marker.color("red")
    else:
        marker.color("black")

###event handlers
marker.ondrag(marker.goto)
whiteboard.onscreenclick(clear, btn=2)
whiteboard.onscreenclick(change_color,btn=3)
