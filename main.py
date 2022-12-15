import turtle
import pandas
from display import ScreenInformationWriter, StateWriter


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

answer_feedback = ScreenInformationWriter()
state_writer = StateWriter()

state_list = data["state"].to_list()

while len(guessed_states) < 50:

    answer = screen.textinput(title = f"{len(guessed_states)}/50 correct answers", prompt="What's another state's name").title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer in state_list:

        answer_feedback.answer_positive_feedback(answer)
        guessed_states.append(answer)
        state_row = data[data["state"] == answer]
        x_cor = int(state_row['x'])
        y_cor = int(state_row['y'])
        state_writer.write_state(answer, x_cor, y_cor)

    else:
        answer_feedback.answer_negative_feedback(answer)

# states_to_learn.csv
if(len(guessed_states) == 50):
    answer_feedback.end_game()
else:
    answer_feedback.data_input_closed()

screen.exitonclick()