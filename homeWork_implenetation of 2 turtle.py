import turtle

import random

import time

turt1 = turtle.Turtle()
turt1.shape("turtle")
turt1.shapesize(3,3)
turt1.color('blue')
turt1.penup()
turt1.goto(-300,0)
turt1.speed(6)
# home work make it anohter turtle



for i in range(100):
    turt1.forward(random.randint(1,10))
    x1,y = turt1.pos()
    if x1 > 400:
        break


turt2 = turtle.Turtle()
turt2.shape("turtle")
turt2.shapesize(3,3)
turt2.color('red')
turt2.penup()
turt2.goto(-600,100)
turt2.speed(7)
# home work make it anohter turtle



for i in range(100):
    turt2.forward(random.randint(1,10))
    x2,y2 = turt2.pos()
    if x2 > 400:
        break

turtle.done()