#import turtle
#t = turtle.Pen()
#for x in range(1,38):
#    t.forward(100)
#    t.left(175)
#turtle.getscreen()._root.mainloop()
from tkinter import *
import time
ventana =Tk()
ventana.title("Animación")
canvas = Canvas(ventana,width=400,height=400)
canvas.pack()
imagen = PhotoImage(file="dibujo.gif")
canvas.create_image(50,50,anchor=NW,image=imagen)

canvas1 = Canvas(ventana,width=400,height=200)
canvas1.pack()
canvas.create_polygon(10,10,10,60,50,35)
#for x in range(0,60):
#    canvas.move(1,5,0)
#    ventana.update()
#    time.sleep(0.5)
    
def movertriangle(event):
    if event.keysym == 'Up':
        canvas.move(1,0,-3)
    elif event.keysym=='Down':
        canvas.move(1,0,3)
    elif event.keysym =='Left':
        canvas.move(1,-3,0)
    else:
        canvas.move(1,3,0)
canvas1.bind_all('<KeyPress-Up>',movertriangle)
canvas1.bind_all('<KeyPress-Down>',movertriangle)
canvas1.bind_all('<KeyPress-Left>',movertriangle)
canvas1.bind_all('<KeyPress-Right>',movertriangle)
    
ventana.mainloop()
