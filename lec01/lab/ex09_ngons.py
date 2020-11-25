import math
import turtle as tl

import numpy


def draw_poly(n, length):
    for i in range(n):
        tl.left(360/n)
        tl.forward(length)


def my_sin(n):
    return math.sin(math.radians(n))


def get_radius(a, n):
    return a / (2*my_sin(360/(2*n)))


x, y = 0, 0

distance = 20
length = 50
radius = 0

for i in range(3, 10):
    radius = get_radius(length, i)
    tl.penup()
    tl.goto(x + radius, y)
    tl.pendown()
    tl.left((180 - (360/i))/2)
    draw_poly(i, length)
    tl.right((180 - (360 / i)) / 2)
    length += 20
