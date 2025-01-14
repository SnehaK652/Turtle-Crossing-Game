
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.v=0
        self.levels()
        self.scores()
    def levels(self):

        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-270,260)
        self.write(f"Level:{self.v}",font=(FONT))

    def scores(self):

        self.v+=1



    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write("Game Over:", font=(FONT))
