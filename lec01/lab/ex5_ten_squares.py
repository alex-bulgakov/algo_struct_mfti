import turtle as tl
from time import sleep

length = 100
distance = 20

x = 0
y = 0
for i in range(10):
    tl.pendown()
    for j in range(4):
        tl.forward(length)
        tl.left(90)
    tl.penup()
    x -= distance / 2
    y -= distance / 2
    tl.goto(x, y)
    length += distance

sleep(2)
