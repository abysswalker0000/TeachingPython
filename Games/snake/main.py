import pygame
from game import SnakeGame
from settings import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    field = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    game = SnakeGame()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        game.update()
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (95, 95, FIELD_WIDTH + 10, FIELD_HEIGHT + 10), 5)
        game.draw(field)
        screen.blit(field, (100, 100))
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()