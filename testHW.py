import turtle

import random

screen = turtle.Screen()
screen.title("USD $1 Trillion Game")


# Object 1 set up
obj1 = turtle.Turtle()
obj1.color("blue") # Sets obj1's colour
obj1.speed(0) # The drawing speed will go as fast as it can if it is set to zero
obj1.penup() # Don't want it to draw a line 
obj1.goto(-300,100) # goes to 0, -50
obj1.shape("turtle")
obj1.shapesize(3,3)
x1,y1 = obj1.pos()





# Movement of objects

for i in range(100):
    obj1.forward(random.randint(1,10))
    obj1.right(random.randint(1,10))
  
  
    if x1 > 400:
        break
    
        


turtle.done()

