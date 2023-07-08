import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states["state"]:
            if state not in guessed_states:
                missing_states.append(state)
        data = pandas.DataFrame(missing_states)
        data.to_csv("missing_states.csv")
        break
    if answer_state in states["state"].to_list():
        state = states[states["state"] == answer_state]
        writer.goto(int(state["x"]), int(state["y"]))
        writer.write(answer_state, align="center", font=("Ariel", 8, "normal"))
        guessed_states.append(answer_state)