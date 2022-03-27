from turtle import Screen, Turtle
from players import Player
from ball import Ball
from score import ScoreBoard
#Creating our screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")


#Creating Player 1
player_1 = Player()
player_1.position(-380)



#Creating Player 2
player_2 = Player()
player_2.position(380)

#Moving
screen.listen()
screen.onkeypress(player_2.go_up, "w")
screen.onkeypress(player_2.go_down, "s")


screen.listen()
screen.onkeypress(player_1.go_up, "Up")
screen.onkeypress(player_1.go_down, "Down")

#Creating the ball
lopta = Ball()


#Creating scoreboards
player1_score = ScoreBoard()
player1_score.go_to(-50,260)
player1_score.tell()

player2_score = ScoreBoard()
player2_score.go_to(50,260)
player2_score.tell()


#Creating line in the middle
line = Turtle("square")
line.color("white")
line.penup()
line.speed("fastest")
line.shapesize(stretch_wid=0.2, stretch_len=1)
line.setx(0)
line.sety(-280)
line.setheading(90)

while line.xcor() != 280:
    line.stamp()
    line.forward(40)


game_is_on = True




screen.exitonclick()