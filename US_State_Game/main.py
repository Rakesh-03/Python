import turtle
from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("50_states.csv")

screen = Screen()
turtle.title("U.S state game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
all_states = data.state.to_list()
guessed_states=[]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states corrct", prompt="what's the another state name?").title()

    if answer_state == "Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_missing")
        print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()
