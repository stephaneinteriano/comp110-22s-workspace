"""A sweet treat that is inedible."""

__author__ = "730391348"

from turtle import Turtle, colormode, done
import random
colormode(255)
drawing: Turtle = Turtle()
drawing.hideturtle()


def main() -> None:
    """The entrypoint for my scene."""
    drawing: Turtle = Turtle()
    draw_triangle(drawing, 90, -20)
    draw_circle(drawing, 40, -50)
    draw_circle(drawing, -65, -50)
    draw_circle(drawing, -10, 40)
    cherry_topping(drawing, -10, 170)
    sprinkles_topping(drawing, 5, -20)

    done()


def draw_triangle(cone: Turtle, x: float, y: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    cone.penup()
    cone.goto(x, y) 
    cone.setheading(180)
    cone.pendown()
    cone.pencolor("pink")
    cone.fillcolor(173, 114, 79)
    cone.begin_fill()
    i: int = 0
    while (i < 3):
        cone.forward(210)
        cone.left(120)
        i = i + 1
    cone.end_fill()


def draw_circle(scoop_icecream: Turtle, on: float, top: float) -> None: 
    """Creating the shape & number of scoops of icecream."""
    scoop_icecream.penup()
    scoop_icecream.goto(on, top) 
    scoop_icecream.setheading(0.0)
    scoop_icecream.pendown()

    scoop_icecream.pencolor(185, 227, 176)
    scoop_icecream.begin_fill()
    scoop_icecream.fillcolor(185, 227, 176)

    scoop_icecream.circle(radius=67, extent=None, steps=None)
    scoop_icecream.end_fill()


def sprinkles_topping(sprinkle: Turtle, x: float, y: float) -> None:
    """Adding random colored sprinkles to the icecream."""
    sprinkle.penup()
    sprinkle.goto(x, y)
    sprinkle.pendown()
    sprinkle.setheading(0.0)
    colors = ["red", "blue", "light green", "pink", "purple", "orange", "yellow"]
    sprinkle.color(random.choice(colors))
    sprinkle.begin_fill()
    i: int = 0
    while i < 1:
        sprinkle.forward(10)
        sprinkle.right(90)
        sprinkle.forward(5)
        sprinkle.right(90)
        i += 1
    sprinkle.end_fill() 

    
def cherry_topping(fruit: Turtle, stem: float, red: int) -> None:
    """Adding a cherry ice-cream topping."""
    fruit.penup()
    fruit.goto(stem, red) 
    fruit.setheading(0.0)
    fruit.pendown()
    fruit.color("red")
    fruit.begin_fill()
    fruit.circle(radius=20, extent=None, steps=None)
    fruit.end_fill()


if __name__ == "__main__":
    main()