from food import Food
from game_screen import GameScreen
from snake import Snake

game_screen = GameScreen()
snake = Snake(game_screen)
food = Food(game_screen)
game_is_on = True

while game_is_on:
    game_screen.update_screen()
    snake.move()
    if snake.food_collision(food):
        food.refresh()
game_screen.exit_game()
