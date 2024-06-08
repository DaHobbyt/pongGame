import turtle
from ball_physics import BallPhysics
from computer_movement import ComputerMovement

class PVCGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("PvC Pong")
        self.screen.bgcolor("black")
        self.screen.setup(800, 600)

        self.player_paddle = turtle.Turtle()
        self.player_paddle.shape("square")
        self.player_paddle.color("white")
        self.player_paddle.shapesize(5, 1)
        self.player_paddle.penup()
        self.player_paddle.goto(-350, 0)

        self.computer_paddle = turtle.Turtle()
        self.computer_paddle.shape("square")
        self.computer_paddle.color("white")
        self.computer_paddle.shapesize(5, 1)
        self.computer_paddle.penup()
        self.computer_paddle.goto(350, 0)

        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.speed(1)

        self.ball_physics = BallPhysics(self.ball)
        self.computer_movement = ComputerMovement()

        self.screen.listen()
        self.screen.onkey(self.move_up, "w")
        self.screen.onkey(self.move_down, "s")

    def move_up(self):
        y = self.player_paddle.ycor()
        y += 20
        self.player_paddle.sety(y)

    def move_down(self):
        y = self.player_paddle.ycor()
        y -= 20
        self.player_paddle.sety(y)

    def play(self):
        while True:
            self.screen.update()
            self.ball_physics.move_ball(self.player_paddle, self.computer_paddle)
            self.computer_movement.move_computer_paddle(self.computer_paddle, self.ball)

            # Check for collision with paddles
            result = self.ball_physics.move_ball(self.player_paddle, self.computer_paddle)
            if result == "Player 1":
                print("Player 1 wins!")
                break
            elif result == "Player 2":
                print("Computer wins!")
                break