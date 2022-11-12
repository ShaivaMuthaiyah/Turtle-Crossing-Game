from turtle import Turtle
import random
FONT = ("Comic Sans MS", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270, -270)
        self.update_level()

    def level_increase(self):
        self.level += 1

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"You got squished!", align="center", font=("Comic Sans MS", 30, "bold"))
        self.goto(0 ,-50)
        self.write("GAME OVER", align="center", font=("Comic Sans MS", 24, "normal"))

