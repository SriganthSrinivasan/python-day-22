from turtle import Turtle

class Paddle:
    def __init__(self):
        self.x_position = -280
        self.y_position = 0
        self.new_paddle()

    def new_paddle(self):
        created_paddle = []
        for i in range(3):
           segment = Turtle("square")
           segment.penup()
           segment.speed(0)
           segment.color("white")
           segment.shapesize(1.0, 1.0, 1.0)
           segment.setposition(self.x_position, self.y_position)
           self.y_position += 20
           created_paddle.append(segment)
        print(created_paddle)

    def paddle_movement(self):
        