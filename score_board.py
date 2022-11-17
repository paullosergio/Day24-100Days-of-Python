from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Hight Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.score += 1
        self.update_score()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)
