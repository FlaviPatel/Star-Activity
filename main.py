import turtle

turtle.title("A Bright Star")

# Screen
screen = turtle.Screen()
screen.bgcolor("Black")

# Turtle
t = turtle.Turtle()
t.shape('arrow')
t.color('yellow')
t.speed(1)
t.pensize(5)
t.fillcolor('white')

t.begin_fill()
# Draw Star
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.right(150)
t.penup()
t.forward(50)
t.right(90)

t.pendown()
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)

t.end_fill()

turtle.done()