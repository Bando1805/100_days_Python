from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.level = 1
    
    def show_level(self):
        self.clear()
        self.write(arg= f'level {self.level}',align = 'center', font= FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', align = 'center', font = FONT)

