import turtle
#speed
turtle.speed(10)
#color draw
turtle.color('gold')
#color background
turtle.bgcolor("black")
v = 200
while v > 1:
    turtle.left(v)
    turtle.forward(v*3)
    v = v - 1