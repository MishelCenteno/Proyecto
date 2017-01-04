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
canvas1.create_polygon(10,10,10,60,50,35)

def mover_imagen(event):
    if event.keysym == 'Up':
        canvas.move(1,0,-3)
    elif event.keysym=='Down':
        canvas.move(1,0,3)
    elif event.keysym =='Left':
        canvas.move(1,-3,0)
    else:
        canvas.move(1,3,0)
        
def mover_triangulo(event):
    if event.keysym == 'w':
        canvas1.move(1,0,-3)
    elif event.keysym=='s':
        canvas1.move(1,0,3)
    elif event.keysym =='a':
        canvas1.move(1,-3,0)
    else:
        canvas1.move(1,3,0)        
ventana1 = Tk()
ventana1.title("Mando")
ventana1.geometry("425x305")
ventana1.configure(background="black")
mensaje = "Movimeinto de la imagen con las teclas direccionales"
msg = Message(ventana1, text = mensaje)
msg.config(bg='black',fg ="white",font=('times', 20, 'italic'))
msg.pack( )

mensaje1 = "Movimeinto del triángulo: \n'W': arriba \n'S': abajo \n'D':derecha \n'A': izquierda"
msg = Message(ventana1, text = mensaje1)
msg.config(bg='black',fg="skyblue",font=('times', 20, 'italic'))
msg.pack( )
canvas1.bind_all('<KeyPress-Up>',mover_imagen)
canvas1.bind_all('<KeyPress-Down>',mover_imagen)
canvas1.bind_all('<KeyPress-Left>',mover_imagen)
canvas1.bind_all('<KeyPress-Right>',mover_imagen)

canvas1.bind_all('<KeyPress-w>',mover_triangulo)
canvas1.bind_all('<KeyPress-s>',mover_triangulo)
canvas1.bind_all('<KeyPress-a>',mover_triangulo)
canvas1.bind_all('<KeyPress-d>',mover_triangulo)
    
ventana.mainloop()
