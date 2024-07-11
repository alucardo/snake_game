from turtle import Turtle, Screen


class GameScreen():

    def __init__(self):
        self.screen = Screen()
        self.score = -1
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.refresh_score()
        self.screen.tracer(0)
        self.screen.listen()

    def exit_game(self):
        self.screen.exitonclick()

    def set_score(self, score):
        self.screen.title(f"Score: {score}")

    def update_screen(self):
        self.screen.update()

    def key_up(self, action):
        self.screen.onkey(action, "Up")
        self.screen.onkey(action, "w")

    def key_down(self, action):
        self.screen.onkey(action, "Down")
        self.screen.onkey(action, "s")

    def key_left(self, action):
        self.screen.onkey(action, "Left")
        self.screen.onkey(action, "a")

    def key_right(self, action):
        self.screen.onkey(action, "Right")
        self.screen.onkey(action, "d")

    def refresh_score(self):
        self.score += 1
        self.screen.title(f"Score: {self.score}")