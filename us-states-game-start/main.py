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

while len(guessed_states) < 50:

    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another states names?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_list = pd.DataFrame(missing_states)
        new_list.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        # If they got it right
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # Create a turtle to write the name of the state's x and y coord
        t.write(answer_state)  # podrias usar el .item() para solo tomar el dato sin el index


# States to learn.csv
# lista_filtrada = list(set(all_states) - set(guessed_states))
# states_to_learn = pd.DataFrame(lista_filtrada)
# states_to_learn.to_csv("states_left_to_learn.csv")























# game_is_on = True
# correct_answers = 0
#
# while game_is_on:
#     screen.update()
#
#     if correct_answers == 0:
#         answer_state = turtle.textinput(title="Guess the State", prompt="What's another states names?")
#     else:
#         answer_state = turtle.textinput(title=f"{correct_answers}/{len(state_dict)} State Correct", prompt="What's another states names?")
#
#
#     # Si el usuario escribe 'exit', finalizar el juego
#     if answer_state.lower() == 'exit':
#         game_is_on = False
#     else:
#         # Comprobar si la respuesta del usuario es correcta
#         for s in state_dict:
#             state_name = s[0]
#             state_coord = (s[1], s[2])
#
#             if answer_state.title() == state_name:
#                 s_state = ShowState(state_name, state_coord)
#                 correct_answers += 1
















# Permite obtener los valores de
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

# Mantiene la ventana abierta al igual que el exit onclick
turtle.mainloop()


# screen.exitonclick()
