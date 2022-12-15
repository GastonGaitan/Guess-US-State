from turtle import Turtle

class Writter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

class ScreenInformationWriter(Writter):
    def __init__(self):
        super().__init__()
        self.goto(0,250)
        self.font = ("Arial", 20)
    
    def answer_positive_feedback(self, answer):
        self.clear()
        self.write(f"{answer} exists! :D", align="center", font=self.font)

    def answer_negative_feedback(self, answer):
        self.clear()
        self.write(f"{answer} does not exist... :(", align="center", font=("Arial", 20))

    def end_game(self):
        self.clear()
        self.write(f"You have guessed all states! You win!", align="center", font=self.font)

    def data_input_closed(self):
        self.clear()
        self.write(f"Game closed :/", align="center", font=self.font)

class StateWriter(Writter):
    def __init__(self):
        super().__init__()
        self.font = ("Arial", 10)
    
    def write_state(self,answer, x, y):
        self.goto(x, y)
        self.write(f"{answer}", align="center", font=self.font)
    
    