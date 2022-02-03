from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=5)
        self.left(90)
        self.goto(position)
        
    
    def up(self):
        self.forward(20)


    def down(self):
        self.backward(20)