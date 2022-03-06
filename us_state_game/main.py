from tkinter import font
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(image)

answer_cnt = 0

# get 50 states name
states_data = pd.read_csv("50_states.csv")
state_names = states_data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    # get user's input
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # state_to_learn.csv
        state_to_learn = [state for state in state_names if state not in guessed_state]

        df = pd.DataFrame(state_to_learn)
        df.to_csv("state_to_learn.csv")


        break

    # compare user's answer and 50 state name 
    # if user's answer is correct, display city name on map
    if answer_state in state_names:
        x_cor = states_data[states_data.state == answer_state].x
        y_cor = states_data[states_data.state == answer_state].y
        guessed_state.append(answer_state)

        screen.tracer(0)
        s_name = Turtle()
        s_name.hideturtle()
        s_name.penup()
        s_name.goto(int(x_cor), int(y_cor))
        s_name.write(answer_state)
        screen.update()
        answer_cnt += 1
        
    # if not -> get user's input again

