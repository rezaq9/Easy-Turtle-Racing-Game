import turtle

import random

screen = turtle.Screen()
screen.title("USD $1 Trillion Game")


# Object 1 set up
obj1 = turtle.Turtle()
obj1.color("red") # Sets obj1's colour
obj1.speed(0) # The drawing speed will go as fast as it can if it is set to zero
obj1.penup() # Don't want it to draw a line 
obj1.goto(-300,150) # goes to 0, -50
obj1.shape("turtle")
obj1.shapesize(3,3)
x1,y1 = obj1.pos()

### Object 2 set up
obj2 = turtle.Turtle()
obj2.color("blue") # sets obj2's colour
obj2.speed(0) # The drawing speed will go as fast as it can if it is set to zero
obj2.penup() # Don't want it to draw a line 
obj2.goto(-300,0) # goes to 0, 50
obj2.shape("turtle")
obj2.shapesize(3,3)
x2,y2 = obj2.pos()

### Object 3 set up
obj3 = turtle.Turtle()
obj3.color("green") # sets obj3's colour
obj3.speed(0) # The drawing speed will go as fast as it can if it is set to zero
obj3.penup() # Don't want it to draw a line 
obj3.goto(-300,-150) # goes to 0, 50
obj3.shape("turtle")
obj3.shapesize(3,3)
x3,y3 = obj2.pos()

### Object 4 set up
obj4 = turtle.Turtle()
obj4.color("purple") # sets obj4's colour
obj4.speed(0) # The drawing speed will go as fast as it can if it is set to zero
obj4.penup() # Don't want it to draw a line 
obj4.goto(-300,-300) # goes to 0, 50
obj4.shape("turtle")
obj4.shapesize(3,3)
x4,y4 = obj2.pos()

# add it lower to make it move down


# Movement of objects

for i in range(100):
    obj1.forward(random.randint(1,10))
    obj1.right(random.randint(1,10))
  
    obj2.forward(random.randint(1,10))
    obj2.right(random.randint(1,10))

    obj3.forward(random.randint(1,10))
    obj3.right(random.randint(1,10))

    obj4.forward(random.randint(1,10))
    obj4.right(random.randint(1,10))
  
    if x1 > 400 or x2 > 400 or x3 > 400 or x4 > 400:
        break
    
        


turtle.done()

