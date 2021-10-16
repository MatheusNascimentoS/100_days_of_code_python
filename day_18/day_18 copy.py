import turtle as t
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

# angles = [0, 90, 180, 270]
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(choice(angles))

for angle in range(0, 360, 4):
    t.color(random_color())
    t.circle(80)
    t.right(4)

screen = t.Screen()
screen.exitonclick()   
