from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.colormode(255)
screen.setup(600, 400)
screen.title("Shri's Ping Pong Table")
screen.bgpic("woodenbg.gif")
screen.listen()
paddle = Paddle()
screen.onkey(paddle.paddle_up, "Up")
screen.onkey(paddle.paddle_down, "Down")



screen.exitonclick()
