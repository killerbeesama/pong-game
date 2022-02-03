from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

left_paddle = Paddle((-360,0))
right_paddle = Paddle((360,0))

ball = Ball()
scoreboard = ScoreBoard()



screen.onkeypress(left_paddle.up,'w')
screen.onkeypress(left_paddle.down,'s')
screen.onkeypress(right_paddle.up,'Up')
screen.onkeypress(right_paddle.down,'Down')


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 350 or ball.distance(left_paddle) < 60 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score()
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score()



   

screen.exitonclick()
screen.mainloop()