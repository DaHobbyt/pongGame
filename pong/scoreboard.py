import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score = {"Player 1": 0, "Player 2": 0}
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Player 1: {self.score['Player 1']}  Player 2: {self.score['Player 2']}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self, player):
        self.score[player] + 1
        self.update_scoreboard()

    def display_winscreen(self, winner):
        self.clear()
        self.write(f"{winner} wins!", align="center", font=("Arial", 24, "normal"))