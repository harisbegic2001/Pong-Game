from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.7, stretch_len=3)
        self.sety(0)
        self.setheading(90)
        self.penup()

    def position(self, coordinate):
        self.setx(coordinate)


    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.back(20)