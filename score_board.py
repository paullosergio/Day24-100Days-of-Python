from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)
