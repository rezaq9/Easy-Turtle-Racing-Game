import turtle

turt1 = turtle.Turtle()
turt1.shape("turtle")
turt1.shapesize(3,3)
turt1.color('blue')
turt1.penup()
turt1.goto(-300,0)
# home work make it anohter turtle


import random

for i in range(100):
    turt1.forward(random.randint(1,10))
    x1,y = turt1.pos()
    if x1 > 400:
        break

turtle.done()