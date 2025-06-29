from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-20,270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score : {self.score}",False,"center",font=("Arial",15,"normal"))

    def increase_scoreboard(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",font=("Arial",30,"normal"))
        self.goto(0,-30)
        self.update_scoreboard()