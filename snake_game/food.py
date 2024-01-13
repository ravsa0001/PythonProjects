from turtle import Turtle
import random


Font = ("Arial", 24, "normal")

class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align = "center", font = Font)
        self.hideturtle()
        
    def update_sc(self):
        self.write(f"Score: {self.score}", align = "center", font = Font)
        
    def game_over(self):
        self.write("Game Over", align = "center", font= Font)
        
    def incsc(self):
        self.score += 1
        self.clear()
        self.update_sc()