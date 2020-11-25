import math
import turtle as tl
from time import sleep

n = 10
for i in range(1, math.floor(n/2)):
    tl.circle(100)
    tl.circle(-100)
    tl.left((360/n))

sleep(2)
