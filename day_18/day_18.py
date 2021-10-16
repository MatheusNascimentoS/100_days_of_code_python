from turtle import Turtle, Screen
from random import choice
screen = Screen()
tim = Turtle()
tim.pensize(5)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for angle in range(3, 9):
    tim.pencolor(choice(colours))
    for sides in range(0, angle):
        tim.forward(100)
        tim.right(360 / angle)
   
screen.exitonclick()