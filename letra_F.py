import turtle

fondo = turtle.Screen()
fondo.bgcolor("skyblue")

t = turtle.Pen()
t.color(1,1,0)
t.begin_fill()

t.forward(40)
t.left(90)
t.forward(90)
t.right(90)
t.forward(50)
t.left(90)
t.forward(40)
t.left(90)
t.forward(50)
t.right(90)
t.forward(40)
t.right(90)
t.forward(70)
t.left(90)
t.forward(40)
t.left(90)
t.forward(110)
t.left(90)
t.forward(210)

t.end_fill()

turtle.getscreen()._root.mainloop()
