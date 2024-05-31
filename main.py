import turtle
import pandas
from map_text import MapText

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
new_dict = {details.state: (details.x, details.y) for index, details in data.iterrows()}
all_states = [key for key, _ in new_dict.items()]

guessed = 0
keep_going = True
while keep_going:
    answer_state = screen.textinput(title=f"Guessed: {guessed}/{len(data)}", prompt="What's another state's name? ")
    if answer_state is None:  # Cancel - Button pressed
        keep_going = False
        pandas.DataFrame(all_states).to_csv('states_to_learn.csv')
    else:
        for state, coords in new_dict.items():
            if answer_state.lower() == state.lower() and answer_state.title() in all_states:
                label = MapText(answer_state.title(), coords[0], coords[1])
                all_states.remove(answer_state.title())
                guessed += 1
                if guessed >= len(data):
                    turtle.write("Congratulations!", align="center", font=("Courier", 24, "bold"))
                    pandas.DataFrame([]).to_csv('states_to_learn.csv')
                    keep_going = False

screen.exitonclick()
