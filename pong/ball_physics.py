class BallPhysics:
    def __init__(self, ball):
        self.ball = ball
        self.ball_speed_x = 2
        self.ball_speed_y = 2
        self.speed_multiplier = 1.05

    def move_ball(self, player_paddle, computer_paddle):
        self.ball.setx(self.ball.xcor() + self.ball_speed_x)
        self.ball.sety(self.ball.ycor() + self.ball_speed_y)

        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.ball_speed_y *= -1

        if self.ball.xcor() < -340 and self.ball.ycor() < player_paddle.ycor() + 50 and self.ball.ycor() > player_paddle.ycor() - 50:
            self.ball_speed_x *= -1
            self.increase_speed()
        elif self.ball.xcor() > 340 and self.ball.ycor() < computer_paddle.ycor() + 50 and self.ball.ycor() > computer_paddle.ycor() - 50:
            self.ball_speed_x *= -1
            self.increase_speed()

        if self.ball.xcor() < -400 or self.ball.xcor() > 400:
            self.ball.goto(0, 0)
            self.ball_speed_x = 2
            self.ball_speed_y = 2

        return self.check_win(player_paddle, computer_paddle)

    def increase_speed(self):
        self.ball_speed_x *= self.speed_multiplier
        self.ball_speed_y *= self.speed_multiplier

    def check_win(self, player_paddle, computer_paddle):
        if self.ball.xcor() < -400:
            return "Player 2"
        elif self.ball.xcor() > 400:
            return "Player 1"
        else:
            return None