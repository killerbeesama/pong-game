from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-200,260)
        self.write(f"SCORE:{self.left_score}",align='center',font=('Arial', 25, 'normal'))
        self.goto(200,260)
        self.write(f"SCORE:{self.right_score}",align='center',font=('Arial', 25, 'normal'))


    def l_score(self):
        self.left_score += 1
        self.update_score()


    def r_score(self):
        self.right_score += 1
        self.update_score()
