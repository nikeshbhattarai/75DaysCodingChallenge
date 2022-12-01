from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100, steps=200)
        t.setheading(t.heading() + 10)

draw_spirograph(5)


screen.exitonclick()