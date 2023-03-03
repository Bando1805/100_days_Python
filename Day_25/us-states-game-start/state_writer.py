from turtle import Turtle 

class StateWriter(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        
    def write_state(self, state: str, location: tuple) -> None:
        self.goto(location)
        self.write(state)
    

