from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score=0   
        self.highscore=0     
        with open("./highscore.txt","r") as getting_score:
            hs=getting_score.read()
            if hs:
                self.highscore=int(hs)

        self.hideturtle()   
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.game_score} High Score: {self.highscore}",move=False, align="center",font=("Arial",15,"normal") )
        
    def increase_score(self):
        self.game_score+=1 
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     self.write("GAME OVER",align="center",font=("Arial",20,"bold"))

    def reset(self):
        
            
        if self.game_score>self.highscore:
            self.highscore=self.game_score
            with open("./highscore.txt","w") as file:
                
                file.write(f"{self.highscore}")
        self.game_score=0
        self.update_scoreboard()

