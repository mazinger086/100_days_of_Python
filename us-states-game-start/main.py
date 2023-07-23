import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pd.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []  # Lista para los estados incorrectamente adivinados

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another states names?")

    if answer_state is not None:
        answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Crear archivo CSV con los estados incorrectamente adivinados
if missing_states:
    new_list = pd.DataFrame(missing_states, columns=["Missing States"])
    new_list.to_csv("missing_states.csv", index=False)