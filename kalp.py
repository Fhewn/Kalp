import turtle
import time

size=2
x,y=turtle.position()
turtle.setposition(x,y-size*85)
turtle.pendown()
turtle.color('purple')
turtle.begin_fill()
turtle.pensize(3)
turtle.left(50)
turtle.forward(133*size)
turtle.circle(50*size,200)
turtle.right(140)
turtle.circle(50*size,200)
turtle.forward(133*size)
turtle.end_fill()
turtle.sleep(6)


///Fhewn tarafında yapılmıştır.////
