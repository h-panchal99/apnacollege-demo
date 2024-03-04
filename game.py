import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake
snake_block = 10
snake_speed = 10
snake_list = []
snake_length = 1

# Food
food_block = 10
food_x = random.randrange(0, WIDTH - food_block, food_block)
food_y = random.randrange(0, HEIGHT - food_block, food_block)

# Direction
direction = "RIGHT"

clock = pygame.time.Clock()

# Draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(WIN, GREEN, [x[0], x[1], snake_block, snake_block])

# Game over screen
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

# Game loop
def game_loop():
    global direction, snake_length, snake_list, food_x, food_y

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -snake_block
                    y_change = 0
                    direction = "a"
                elif event.key == pygame.K_d:
                    x_change = snake_block
                    y_change = 0
                    direction = "d"
                elif event.key == pygame.K_w:
                    x_change = 0
                    y_change = -snake_block
                    direction = "w"
                elif event.key == pygame.K_s:
                    x_change = 0
                    y_change = snake_block
                    direction = "s"

                elif event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                    direction = "DOWN"

        # Boundary conditions
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over()

        # Update snake position
        x += x_change
        y += y_change

        WIN.fill(WHITE)
        pygame.draw.rect(WIN, RED, [food_x, food_y, food_block, food_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over()

        draw_snake(snake_block, snake_list)

        # Collision detection with food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - food_block, food_block)
            food_y = random.randrange(0, HEIGHT - food_block, food_block)
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

# Start the game loop
game_loop()