from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.player_score = 0
        self.write("Score " + str(self.player_score), move=True, align='center', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.goto(x=0, y=250)
        self.player_score += 1
        self.write("Score " + str(self.player_score), move=True, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=True, align='center', font=('Arial', 20, 'normal'))
