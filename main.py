from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
race_is_on = True

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle came first!")
            else:
                print(f"You've lost! The {winning_color} turtle came first!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()


