import turtle as tl
from time import sleep

radius = 100
offset = 10
tl.left(90)
for i in range(10):
    tl.circle(radius)
    tl.circle(-radius)
    radius += offset

sleep(2)
