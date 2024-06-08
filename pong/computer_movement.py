class ComputerMovement:
    def __init__(self):
        self.computer_speed = 2

    def move_computer_paddle(self, computer_paddle, ball):
        if ball.xcor() > 0:
            if ball.ycor() < computer_paddle.ycor() - 20:
                computer_paddle.sety(computer_paddle.ycor() - self.computer_speed)
            elif ball.ycor() > computer_paddle.ycor() + 20:
                computer_paddle.sety(computer_paddle.ycor() + self.computer_speed)