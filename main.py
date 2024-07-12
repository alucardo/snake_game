from food import Food
from game_screen import GameScreen
from snake import Snake
from scoreboard import Scoreboard

game_screen = GameScreen()
snake = Snake(game_screen)
food = Food(game_screen)
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    game_screen.update_screen()
    snake.move()
    if snake.food_collision(food):
        food.refresh()
        scoreboard.increase_score()

    if snake.wall_collision() or snake.tail_collision():
        game_is_on = False
        scoreboard.game_over()

game_screen.exit_game()
