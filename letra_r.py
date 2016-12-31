import turtle
from turtle import *
turtle.setup(1000, 600)
screensize(2000, 1200)

def r(a,color): #a es el ancho 
    fillcolor(color)
    b = int(a/2)
    begin_fill()
    goto(a,0)
    goto(a,a*2)
    goto(a*3,0)
    goto(a*4,0)
    goto(a*2,a*2)
    LinInv(a*2,a*5)
    turtle.circle(-(b*3),180)
    LinInv(a*2,a*5)
    goto(0,a*5)
    goto(0,0)
    end_fill()
    LinInv(a*2,a*3)
    goto(a*2+5,a*3)
    goto(a*2,a*3)
    CirInv(-25,180)
    fillcolor('white')
    begin_fill()
    turtle.circle(-25,180)
    end_fill()
    LinInv(a*2,a*4)
    fillcolor('white')
    begin_fill()
    goto(a,a*4)
    goto(a,a*3)
    goto(a*2,a*3)
    end_fill()
    turtle.hideturtle()
    return a*4

def LinInv(x,y):
    penup()
    goto(x,y)
    pendown ()
     
def CirInv(x,y):
    penup()
    turtle.circle(x,y)
    pendown ()

    
r(50,"green")
