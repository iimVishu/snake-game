import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up direction constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        x, y = head
        if self.direction == UP:
            new_head = (x, y - CELL_SIZE)
        elif self.direction == DOWN:
            new_head = (x, y + CELL_SIZE)
        elif self.direction == LEFT:
            new_head = (x - CELL_SIZE, y)
        elif self.direction == RIGHT:
            new_head = (x + CELL_SIZE, y)

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        x, y = tail
        if self.direction == UP:
            new_tail = (x, y + CELL_SIZE)
        elif self.direction == DOWN:
            new_tail = (x, y - CELL_SIZE)
        elif self.direction == LEFT:
            new_tail = (x + CELL_SIZE, y)
        elif self.direction == RIGHT:
            new_tail = (x - CELL_SIZE, y)

        self.body.append(new_tail)

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Main function
def main():
    # Set up display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')

    # Initialize clock
    clock = pygame.time.Clock()

    # Initialize snake and food
    snake = Snake()
    food = Food()

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        # Move snake
        snake.move()

        # Check for collisions with food
        if snake.body[0] == food.position:
            snake.grow()
            food = Food()

        # Check for collisions with walls
        if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
                snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT):
            running = False

        # Check for collisions with itself
        for segment in snake.body[1:]:
            if snake.body[0] == segment:
                running = False

        # Drawing
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

        # FPS
        clock.tick(10)

    # Quit
    pygame.quit()

if __name__ == "__main__":
    main()
