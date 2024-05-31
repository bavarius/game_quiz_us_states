from turtle import Turtle


class MapText(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.penup()
        self.hideturtle()
        self.goto(self.x, self.y)
        self.write(name, align='center')
