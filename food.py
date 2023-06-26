from turtle import Turtle
from random import randint
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.create_food()

    def create_food(self):
        random_x=randint(-285,285)
        random_y=randint(-285,285)
        self.goto(random_x,random_y)