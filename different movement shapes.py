import turtle 




def make_circle(t, s):# arguements 
    for i in range (100):
        t.forward(s)
        t.left(1)


t1 = turtle.Turtle()
t1.goto(-200, 0)
make_circle(t1, 2)

t2 = turtle.Turtle()
t2.goto(200, 0)
make_circle(t2, 2)

turtle.mainloop()

