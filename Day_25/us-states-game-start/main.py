import turtle as t
import pandas as pd
from state_writer import StateWriter
from csv_manager import CsvManager

csv_manager = CsvManager('50_states.csv')
state_writer = StateWriter()
screen = t.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

game_completed = False
guessed_states = []
while game_completed == False:

    answer_state = screen.textinput( title = f'Guess the state ({csv_manager.states_guessed}/{csv_manager.number_of_states})', prompt = "What's another state name?")
    
    if answer_state == 'Exit':
        all_states = csv_manager.data.state.to_list()
        all_states = [item.lower() for item in all_states]
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('missing_states.csv')
        break

    if csv_manager.guess_checker(answer_state):
        guessed_states.append(answer_state.lower())
        csv_manager.states_guessed += 1
        location = csv_manager.get_location(answer_state)
        state_writer.write_state(answer_state,location)

    if csv_manager.states_guessed == csv_manager.number_of_states:
        game_completed = True


print( missing_states)


