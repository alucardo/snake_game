from turtle import Turtle

MOVE_DISTANCE = 20

class Snake():
    def __init__(self, game_screen):
        self.segments = []
        self.create_snake()
        game_screen.key_up(self.up)
        game_screen.key_down(self.down)
        game_screen.key_left(self.left)
        game_screen.key_right(self.right)
        self.game_screen = game_screen

    def create_snake(self):
        for i in range(3):
            self.segments.append(Turtle('square'))
            self.segments[i].color('white')
            self.segments[i].penup()
            self.segments[i].goto(-(i * MOVE_DISTANCE), 0)

    def move(self):
        limit = len(self.segments) - 1
        for seg_num in range(limit, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)