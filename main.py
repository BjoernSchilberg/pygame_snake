import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
FG_COLOR = (255, 255, 255)
BG_COLOR = (0, 125, 255)

# Block size for the snake and food
BLOCK_SIZE = 20

# Clock to control game speed
clock = pygame.time.Clock()
SNAKE_SPEED = 10

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


def draw_snake(snake_body):
    """Draw the snake on the screen."""
    for block in snake_body:
        pygame.draw.rect(screen, FG_COLOR, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])


def draw_food(food_position):
    """Draw the food on the screen."""
    pygame.draw.rect(
        screen, FG_COLOR, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE]
    )


# Initial snake setup
snake_body = [[100, 100], [90, 100], [80, 100]]  # Initial snake with 3 blocks
snake_direction = "RIGHT"
change_to = snake_direction

# Initial food position
food_position = [
    random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE),
    random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE),
]

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
            # Exit with ESC or q
            elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    # Update direction
    snake_direction = change_to

    # Move the snake
    if snake_direction == "UP":
        new_head = [snake_body[0][0], snake_body[0][1] - BLOCK_SIZE]
    elif snake_direction == "DOWN":
        new_head = [snake_body[0][0], snake_body[0][1] + BLOCK_SIZE]
    elif snake_direction == "LEFT":
        new_head = [snake_body[0][0] - BLOCK_SIZE, snake_body[0][1]]
    elif snake_direction == "RIGHT":
        new_head = [snake_body[0][0] + BLOCK_SIZE, snake_body[0][1]]

    # Add new head to the snake body
    snake_body.insert(0, new_head)

    # Check if the snake eats the food
    if snake_body[0] == food_position:
        score += 1
        food_position = [
            random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE),
            random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE),
        ]
    else:
        snake_body.pop()

    # Check for collisions
    if (
        snake_body[0][0] < 0
        or snake_body[0][0] >= SCREEN_WIDTH
        or snake_body[0][1] < 0
        or snake_body[0][1] >= SCREEN_HEIGHT
        or snake_body[0] in snake_body[1:]
    ):
        running = False

    # Update the screen
    screen.fill(BG_COLOR)
    draw_snake(snake_body)
    draw_food(food_position)

    # Display the score
    font = pygame.font.Font("Ac437_Amstrad_PC.ttf", 35)
    score_text = font.render(f"Score: {score}", True, FG_COLOR)
    screen.blit(score_text, [10, 10])

    pygame.display.flip()
    clock.tick(SNAKE_SPEED)
