from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        #self.write(f"{self.score}")


    def go_to(self, position1, position2):
        self.goto(x=position1, y=position2)

    def tell(self):
        self.write(f"{self.score}", align="center", font=("Arial", 24, "normal"))

    def point_scored(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 24, "normal"))