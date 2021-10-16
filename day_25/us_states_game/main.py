from os import stat
import turtle
import guesses
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"day_25\us_states_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guesses = guesses.Guesses()
data = pandas.read_csv(r"day_25\us_states_game\50_states.csv")

states = data.state.to_list()
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        break
    
    if answer_state in states and answer_state not in correct_states:
        correct_states.append(answer_state)
        del(states[states.index(answer_state)])
        guesses.correct_guess(answer_state, float(data[data.state == answer_state].x), float(data[data.state == answer_state].y))

df = pandas.DataFrame(states)
df.to_csv(r"day_25\us_states_game\to_study.csv")
