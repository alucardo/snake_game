import time
from turtle import Turtle

from game_screen import GameScreen

game_screen = GameScreen()
game_screen.set_screen()
segments = []

for i in range(3):
    segments.append(Turtle('square'))
    segments[i].color('white')
    segments[i].penup()
    segments[i].goto(-(i * 20), 0)

game_is_on = True

while game_is_on:
    game_screen.update_screen()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

game_screen.exit_game()
