from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def get_score(self, side):
        if side == 'right':
            self.r_score += 1
        else:
            self.l_score += 1

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font = FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font = FONT)
