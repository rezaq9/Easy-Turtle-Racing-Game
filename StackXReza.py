import turtle

import random

screen = turtle.Screen()
screen.title("Turtle Movement")


# Object 1 set up
obj1 = turtle.Turtle()
obj1.color("red") # Sets obj1's colour
obj1.speed(0) # The drawing speed will go as fast as it can if it is set to zero
obj1.penup() # Don't want it to draw a line as I goes to 0, -50
obj1.goto(0, -50) # goes to 0, -50
obj1.pendown() # Now we want it to draw
obj1.shape("turtle")
obj1.shapesize(3,3)
x1,y1 = obj1.pos()



### Object 2 set up
obj2 = turtle.Turtle()
obj2.color("blue") # sets obj2's colour
obj2.speed(0) # The drawing speed will go as fast as it can if it is set to zero
obj2.penup() # Don't want it to draw a line as I goes to 0, -50
obj2.goto(0, 50) # goes to 0, 50
obj2.pendown() # Now we want it to draw
obj2.shape("turtle")
obj2.shapesize(3,3)
x2,y2 = obj2.pos()

# Movement of objects


for i in range(100):
    obj1.forward(random.randint(1,10))
  
    obj2.forward(random.randint(1,10))
  
    if x2 > 400 or x1 > 400:
        break


turtle.done()