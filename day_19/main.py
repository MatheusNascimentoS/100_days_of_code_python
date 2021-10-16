from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def turn_clockwise():
    tim.right(5)

def turn_conterclockwise():
    tim.left(5)

def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_conterclockwise, "a")
screen.onkeypress(turn_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
