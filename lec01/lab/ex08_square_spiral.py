import turtle as tl

length = 20

for i in range(10):
    for j in range(4):
        tl.forward(length)
        tl.left(90)
        length += 10

