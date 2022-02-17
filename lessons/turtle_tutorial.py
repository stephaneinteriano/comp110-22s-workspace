from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.pencolor("pink")
leo.fillcolor(255, 255, 255)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(200)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob.penup()
bob.goto(-150, -60)
bob.pendown()

bob.speed(60)

bob.pencolor("pink")
bob.begin_fill()
bob.fillcolor(46, 120, 112)
i: int = 0
while (i < 3):
    bob.forward(200)
    bob.left(120)
    i = i + 1
bob.end_fill()

bob.hideturtle()


done()