import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed("fastest")
t.penup()
t.setposition(-35,125)
t.pendown()
t.pensize(2)

t.color("red", "black")

diamond_size = 85

points = 16

angle = 180 - (360 / points)

diamond_angle = 360 / points

for i in range(points):
    t.penup()
    t.forward(diamond_size / 2)
    t.pendown()
    t.begin_fill()
    t.left(45)
    t.forward(diamond_size)
    t.right(135)
    t.forward(diamond_size)
    t.end_fill()
    t.left(45)
    t.penup()
    t.forward(diamond_size / 2)
    t.right(diamond_angle)

t.penup()
t.setposition(-160,0)
t.pendown()
t.color("black","red")

diamond_size2=150
points2 = 8

angle2 = 180 - (360 / points2)

diamond_angle2 = 360 / points2

for i in range(points2):
    t.begin_fill()
    t.forward(diamond_size2)
    t.right(45)
    t.forward(diamond_size2)
    t.right(135)
    t.end_fill()
    t.right(diamond_angle2)

t.penup()
t.setposition(-85,0)
t.pendown()
t.color("","black")

for i in range(points2):
    t.begin_fill()
    t.forward(diamond_size2/2)
    t.right(45)
    t.forward(diamond_size2/2)
    t.right(135)
    t.end_fill()
    t.right(diamond_angle2)

t.penup()
t.setposition(-33,0)
t.pensize(0.5)
t.pendown()
t.color("red","")

diamond_size2=50
points2 = 8

angle2 = 180 - (360 / points2)

diamond_angle2 = 360 / points2

for i in range(points2):
    t.begin_fill()
    t.forward(diamond_size2/2)
    t.right(45)
    t.forward(diamond_size2/2)
    t.right(135)
    t.end_fill()
    t.right(diamond_angle2)

t.hideturtle()

turtle.exitonclick()
