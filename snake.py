from turtle import Turtle
import time

MOVE_TIME = 0.1
MOVE_DISTANCE = 20
FOOD_COLLISION_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self, game_screen):
        self.segments = []
        self.create_snake()
        game_screen.key_up(self.up)
        game_screen.key_down(self.down)
        game_screen.key_left(self.left)
        game_screen.key_right(self.right)
        self.game_screen = game_screen
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.segments.append(Turtle('square'))
            self.segments[i].color('white')
            self.segments[i].penup()
            self.segments[i].goto(-(i * MOVE_DISTANCE), 0)

    def move(self):
        limit = len(self.segments) - 1
        time.sleep(0.1)
        for seg_num in range(limit, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def food_collision(self, object):
        if self.head.distance(object) < FOOD_COLLISION_DISTANCE:
            self.add_segment()
            return True
        else:
            return False

    def wall_collision(self):
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        return head_x > 280 or head_x < -280 or head_y > 280 or head_y < -280

    def add_segment(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        x = self.head.xcor()
        y = self.head.ycor()
        new_segment.goto(x, y)
        self.segments.append(new_segment)