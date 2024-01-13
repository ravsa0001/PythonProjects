from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
mdist = 20
up, down, left, right = 90, 270, 180, 0

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
          
        for position in starting_positions:
            self.add_seg(position)
            
            
    def add_seg(self, position):
        new_segm = Turtle("square")
        new_segm.color("white")
        new_segm.penup()
        new_segm.goto(position)
        self.segments.append(new_segm)
        
    def extend(self):
        self.add_seg(self.segments[-1].position())
            
    def move(self):
        for segn in range(len(self.segments)-1, 0, -1):                       #range(start = , stop = , step = )
            newx = self.segments[segn - 1].xcor()
            newy = self.segments[segn - 1].ycor()
            self.segments[segn].goto(newx, newy)
            self.segments[0].forward(mdist)
            
            
    def up(self):
        if self.head.heading() != down:
            self.segments[0].setheading(up)
        
    def down(self):
        if self.head.heading() != up:
            self.segments[0].setheading(down)
        
    def left(self):
        if self.head.heading() != right:
            self.segments[0].setheading(left)
    
    def right(self):
        if self.head.heading() != left:
            self.segments[0].setheading(right)