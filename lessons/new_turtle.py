from turtle import Turtle, colormode, done
colormode(255)
bob: Turtle = Turtle()

bob.left(100)
left = 15
bob.begin_fill()
for i in range(41):
    bob.left(6)
    bob.forward(21.7)
    left += 1
bob.end_fill()

done()