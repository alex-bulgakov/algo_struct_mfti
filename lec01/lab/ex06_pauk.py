import turtle as tl

n = 12
length = 100
tl.shape('turtle')
for i in range(n):
    tl.forward(length)
    tl.stamp()
    tl.left(180)
    tl.forward(length)
    tl.left(180 + 360/n)
