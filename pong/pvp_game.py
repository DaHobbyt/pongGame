# pvp_game.py
import turtle
import time
from scoreboard import Scoreboard

class PVPGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Pong Game")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        self.scoreboard = Scoreboard()

        # Initialize paddles and ball
        self.paddle_a = turtle.Turtle()
        self.paddle_b = turtle.Turtle()
        self.ball = turtle.Turtle()

        # Initialize game variables
        self.ball_speed_x = 0.5
        self.ball_speed_y = 0.5
        self.paddle_a_score = 0
        self.paddle_b_score = 0

        self.play()

    def play(self):
        self.window.listen()
        self.window.onkeypress(self.paddle_a_up, "w")
        self.window.onkeypress(self.paddle_a_down, "s")
        self.window.onkeypress(self.paddle_b_up, "Up")
        self.window.onkeypress(self.paddle_b_down, "Down")

        while True:
            self.window.update()
            self.ball.setx(self.ball.xcor() + self.ball_speed_x)
            self.ball.sety(self.ball.ycor() + self.ball_speed_y)

            if self.ball.ycor() > 290:
                self.ball_speed_y *= -1
            if self.ball.ycor() < -290:
                self.ball_speed_y *= -1
            if self.ball.xcor() > 390:
                self.ball_speed_x *= -1
                self.paddle_b_score += 1
                self.scoreboard.increase_score("Player 2")
            if self.ball.xcor() < -390:
                self.ball_speed_x *= -1
                self.paddle_a_score += 1
                self.scoreboard.increase_score("Player 1")

            if self.ball.xcor() < -350 and self.ball.ycor() < self.paddle_b.ycor() + 50 and self.ball.ycor() > self.paddle_b.ycor() - 50:
                self.ball_speed_x *= -1
            if self.ball.xcor() > 350 and self.ball.ycor() < self.paddle_a.ycor() + 50 and self.ball.ycor() > self.paddle_a.ycor() - 50:
                self.ball_speed_x *= -1

            if self.paddle_a_score > 10:
                self.scoreboard.display_winscreen("Player 1")
                time.sleep(2)
                break
            if self.paddle_b_score > 10:
                self.scoreboard.display_winscreen("Player 2")
                time.sleep(2)
                break

        self.window.bye()