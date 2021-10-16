import turtle as t

from random import choice,randint

rgb_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 
50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


print(rgb_colors)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
t.colormode(255)
tim.goto(-250,-250)

for _ in range(10):
    for _ in range(10):
        tim.color(choice(rgb_colors))
        tim.forward(50)
        tim.dot(20)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

tim.hideturtle()
screen = t.Screen()
screen.exitonclick()   
