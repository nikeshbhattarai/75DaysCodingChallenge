import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_axis = -240
y_axis = -170
all_turtles = []

for clr in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(clr)
    new_turtle.penup()
    y_axis += 50
    new_turtle.goto(x=x_axis, y=y_axis)
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on =  False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!!! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()