from turtle import Turtle, goto
FONT = ("Courier", 6, "normal")

class Guesses(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def correct_guess(self, guess, x, y):
        self.goto(x, y)
        self.write(guess, align="center", font=FONT)