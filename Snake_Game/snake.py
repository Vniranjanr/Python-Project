from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOV_DIST=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self,position):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        t.goto(position)
        self.segments.append(t)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for j in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[j - 1].xcor()
            new_y = self.segments[j - 1].ycor()
            self.segments[j].goto(new_x, new_y)
        self.segments[0].forward(MOV_DIST)
    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def move_rt(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def move_dn(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def move_lt(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)