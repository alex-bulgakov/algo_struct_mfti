import turtle as tl

big_rad = 50
small_rad = 10

tl.left(90)
tl.penup()
tl.goto(-300, 0)
tl.pendown()
for i in range(10):
    tl.circle(-big_rad, extent=180)
    tl.circle(-small_rad, 180)

