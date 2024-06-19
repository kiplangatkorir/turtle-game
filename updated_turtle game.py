import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("lightgreen")

# Draw the finish line
finish_line = 200
line = turtle.Turtle()
line.penup()
line.goto(finish_line, -150)
line.left(90)
line.pendown()
line.forward(300)
line.hideturtle()

# Draw the starting line
start_line = -200
line = turtle.Turtle()
line.penup()
line.goto(start_line, -150)
line.left(90)
line.pendown()
line.forward(300)
line.hideturtle()

# Create turtles
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "violet"]
turtles = []

start_x = start_line
start_y = -100

for color in colors:
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.penup()
    racer.goto(start_x, start_y)
    start_y += 30
    turtles.append(racer)

# Add a decorative sun
sun = turtle.Turtle()
sun.penup()
sun.goto(-300, 200)
sun.color("yellow")
sun.shape("circle")
sun.shapesize(5)
sun.stamp()

# Add clouds
cloud = turtle.Turtle()
cloud.penup()
cloud.goto(-150, 150)
cloud.color("white")
cloud.shape("circle")
cloud.shapesize(3)
cloud.stamp()
cloud.goto(-100, 160)
cloud.stamp()
cloud.goto(-50, 150)
cloud.stamp()
cloud.hideturtle()

# Race function
def race():
    while True:
        for racer in turtles:
            distance = random.randint(1, 5)  # Adjusted speed
            racer.forward(distance)

            # Check for winner
            if racer.xcor() >= finish_line:
                print(f"The winner is the {racer.color()[0]} turtle!")
                return

# Start the race
race()

# Finish the program
turtle.done()
