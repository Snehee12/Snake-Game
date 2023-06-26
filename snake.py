from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
class Snake():
    def __init__ (self):
       
       self.segments=[]
       self.create_snake()
       self.head=self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)
             
    def add_segments(self,position):
        new_segment=Turtle()
        new_segment.shape("square")
        new_segment.color("lime green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def enlarge_snake(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x_cor=self.segments[seg_num-1].xcor()
            y_cor=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_cor,y_cor)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
        
    
    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)
    
    def right(self):
        self.head.setheading(0)
        
    def left(self):
        self.head.setheading(180)
    
