from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.colormode(255)
screen.setup(600, 400)
screen.title("Shri's Ping Pong Table")
screen.bgpic("woodenbg.gif")
screen.listen()
screen.onkey("Up")
screen.onkey("Down")
user_paddle = Paddle()


screen.exitonclick()
