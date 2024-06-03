import turtle
import pandas
from map_text import MapText

OUTPUT_FILE = 'states_to_learn.txt'

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
new_dict = {details.state: {'x': details.x, 'y': details.y} for index, details in data.iterrows()}
all_states = [key for key, _ in new_dict.items()]

# Create an empty output file
open(OUTPUT_FILE, 'w').close()

guessed = 0
keep_going = True
while keep_going:
    answer_state = screen.textinput(title=f"Guessed: {guessed}/{len(data)}", prompt="What's another state's name?")
    if answer_state is None:  # Cancel - Button pressed
        keep_going = False
        # write states that were not guessed to output file
        output_text = f"You didn't guess these {len(all_states)} states:\n{'\n'.join(all_states)}\n"
        print(output_text)
        with open(OUTPUT_FILE, 'a') as f:
            f.write(output_text)
    else:
        state = answer_state.title()
        if state in all_states:
            label = MapText(state, new_dict[state]['x'], new_dict[state]['y'])
            all_states.remove(state)
            guessed += 1
            if guessed >= len(data):
                turtle.write("Congratulations!", align="center", font=("Courier", 24, "bold"))
                keep_going = False

screen.exitonclick()
