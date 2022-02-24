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


bob.left(100)


done()