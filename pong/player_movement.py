class PlayerMovement:
    def __init__(self, player_paddle):
        self.player_paddle = player_paddle

    def player_up(self):
        y = self.player_paddle.ycor()
        if y < 440:  # added boundary check
            y += 40
            self.player_paddle.sety(y)

    def player_down(self):
        y = self.player_paddle.ycor()
        if y > -440:  # added boundary check
            y -= 40
            self.player_paddle.sety(y)