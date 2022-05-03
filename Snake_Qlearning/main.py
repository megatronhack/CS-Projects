import pygame
import random
from game import Apple, Snake_RL_Use
from Qlearning import QLearing
import matplotlib.pyplot as plt
pygame.init()
white = (0, 0, 0)
black = (255, 255, 255)
red = (255, 0, 0)
green = (0, 155, 0)
game_width = 250  #game
game_height = 250 #game
gameDisplay = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("SnakeGame")
clock = pygame.time.Clock()
icon = pygame.image.load("red.png")
pygame.display.set_icon(icon)
img = pygame.image.load('Shead.png')
mySecondImage = pygame.image.load('red.png')
pygame.display.flip()
my_blockSize = 10
FPS = 20
actions = ["up", "left", "right"]
snake_agent = QLearing(actions, e = 0.10)
snake_agent.loadQ()
def my_game_train(times = 5000):
    s = []
    for i in range(times):
        print(i)
        pygame.event.pump()
        snakeDead = False
        lead_x = 70
        lead_y = 70
        snake = Snake_RL_Use(gameDisplay, game_width, game_height, img, lead_x, lead_y)
        apple = Apple(gameDisplay, game_width, game_height, my_blockSize, mySecondImage, snake.snake_list)
        a_x, a_y = apple.get_apple_pos()
        old_state = snake.get_state([a_x, a_y])
        action = "up"
        while not snakeDead:
            a_x, a_y = apple.get_apple_pos()
            snake.update_snake_list(a_x, a_y)
            reward = -0.1
            if snake.is_alive() is False:
                snakeDead = True
                reward = -1
                s.append(snake.snake_length-1)
            gameDisplay.fill(white)
            if snake.eaten is True:
                apple.update_apple_pos(snake.snake_list)
                reward = 0
            state = snake.get_state([a_x, a_y])
            snake_agent.updateQ(tuple(old_state), action, tuple(state), reward)
            snake_agent.saveQ()
            a_x, a_y = apple.get_apple_pos()
            old_state = snake.get_state([a_x, a_y])
            action = snake_agent.getA(tuple(state))
            snake.set_direction_by_action(action)
            apple.display()
            snake.eaten = False
            snake.display()
            snake.display_score()
            pygame.display.update()
            clock.tick(FPS)
    print("Average score is: {}".format(sum(s)/len(s)))
if __name__ == "__main__":
    my_game_train()

