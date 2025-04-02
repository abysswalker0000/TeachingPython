import pygame
import random
from settings import * 


class SnakeGame: 
    def __init__(self):
        self.snake = [(WINDOW_WIDTH // 2 , WINDOW_HEIGHT // 2 )]
        self.direction = (GRID_SIZE, 0)
        self.food = self.spawn_food()
        self.game_over = False

    def spawn_food(self):
        x = random.randrange(0, WINDOW_WIDTH, GRID_SIZE)
        y = random.randrange(0, WINDOW_HEIGHT, GRID_SIZE)
        return(x,y)
    
    def update(self):
        if self.game_over:
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.direction != (0, GRID_SIZE):
            self.direction = (0, -GRID_SIZE)
        if keys[pygame.K_DOWN] and self.direction != (0, -GRID_SIZE):
            self.direction = (0, GRID_SIZE)
        if keys[pygame.K_LEFT] and self.direction != (GRID_SIZE, 0):
            self.direction = (-GRID_SIZE, 0)
        if keys[pygame.K_RIGHT] and self.direction != (-GRID_SIZE,0):
            self.direction = (GRID_SIZE, 0)
        
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.snake.insert(0,new_head)

        if new_head == self.food:
            self.food =self.spawn_food()
        else :
            self.snake.pop()
        
        if (new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or
            new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT):
            self.game_over = True

        if new_head in self.snake[1:]:
            self.game_over = True

    def draw(self, screen):
        screen.fill(BLACK)

        for segment in self.snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, RED, (self.food[0], self.food[1], GRID_SIZE, GRID_SIZE))
