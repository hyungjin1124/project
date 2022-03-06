from turtle import Turtle, home

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200, 250)
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_score()