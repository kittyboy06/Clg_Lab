import turtle

def draw_circle(radius, color):
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_square(length, color):
    turtle.begin_fill()
    turtle.color(color)
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()

def draw_rectangle(length, breadth, color):
    turtle.begin_fill()
    turtle.color(color)
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(breadth)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(length, color):
    turtle.begin_fill()
    turtle.color(color)
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()

radius = 50
length = 100
breadth = 200

turtle.speed(2)

draw_circle(radius, "purple")

draw_square(radius, "red")

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

draw_rectangle(length, breadth, "green")

turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

draw_triangle(length, "grey")




turtle.exitonclick()