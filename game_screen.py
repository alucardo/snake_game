from turtle import Turtle, Screen


class GameScreen():

    def set_screen(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor('black')
        screen.title(f"Score: 0")
        screen.tracer(0)
        self.screen = screen

    def exit_game(self):
        self.screen.exitonclick()

    def set_score(self, score):
        self.screen.title(f"Score: {score}")

    def update_screen(self):
        self.screen.update()
