import pandas as pd

class CsvManager():

    def __init__(self, csv_file : str) -> None:
        self.data = pd.read_csv(csv_file)
        self.number_of_states = len(self.data)
        self.states_guessed = 0

    def guess_checker(self,guess : str) -> bool:
        right_guess = False
        guess = guess.lower()
        states_list = self.data.state.to_list()
        states_list = [item.lower() for item in states_list]
        if guess in states_list:
            right_guess = True        
        return right_guess
    
    def get_location(self, state: str) -> tuple:
        X = int(self.data[ self.data.state.str.lower() == state.lower() ].x)
        Y = int(self.data[ self.data.state.str.lower() == state.lower() ].y)
        return (X,Y)
    

        


  