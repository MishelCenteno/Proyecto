## dibujo solbre la estrella de n lados pares e impares
import turtle
t = turtle.Pen()
n = int(input("ingrese el numero de lados: "))
angulo = 180/n
if n%2==0:
    for i in range(0,n):
        t.forward(100)
        t.left(angulo*2)
else:
    for i in range(0,n):
        t.forward(100)
        t.left(angulo*4)
