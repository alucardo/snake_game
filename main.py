import time
from game_screen import GameScreen
from snake import Snake

game_screen = GameScreen()
snake = Snake(game_screen)
game_is_on = True

while game_is_on:
    game_screen.update_screen()
    time.sleep(0.1)
    snake.move()

game_screen.exit_game()
