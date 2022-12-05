from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed("fastest")
t.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

rgb_colors = []
for _ in range(30):
    rgb_colors.append(random_color())

t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    t.dot(20, random.choice(rgb_colors))
    t.penup()
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(90)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen.exitonclick()