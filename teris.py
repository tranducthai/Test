import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 60
DROP_INTERVAL = 500  # Milliseconds between automatic Tetromino drops

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255), # Cyan
    (255, 255, 0), # Yellow
    (255, 165, 0), # Orange
    (0, 0, 255),   # Blue
    (128, 0, 128), # Purple
    (0, 128, 0),   # Green
    (255, 0, 0)    # Red
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],                    # I
    [[1, 1], [1, 1]],                  # O
    [[0, 1, 0], [1, 1, 1]],            # T
    [[1, 0, 0], [1, 1, 1]],            # L
    [[0, 0, 1], [1, 1, 1]],            # J
    [[0, 1, 1], [1, 1, 0]],            # S
    [[1, 1, 0], [0, 1, 1]]             # Z
]

# Utility functions
def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if y + off_y >= len(board) or x + off_x >= len(board[y + off_y]) or x + off_x < 0 or board[y + off_y][x + off_x]:
                    return True
    return False

def remove_line(board, line):
    del board[line]
    return [[0] * GRID_WIDTH] + board

def new_board():
    return [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Tetromino class
class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = rotate(self.shape)

# Main game function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    last_drop_time = pygame.time.get_ticks()

    board = new_board()
    current_tetromino = Tetromino()
    next_tetromino = Tetromino()
    score = 0
    game_over = False

    def draw_board():
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if board[y][x]:
                    pygame.draw.rect(screen, COLORS[board[y][x] - 1], 
                                     (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        for y, row in enumerate(current_tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, current_tetromino.color, 
                                     ((current_tetromino.x + x) * GRID_SIZE, 
                                      (current_tetromino.y + y) * GRID_SIZE, 
                                      GRID_SIZE, GRID_SIZE))

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_tetromino.x -= 1
                    if check_collision(board, current_tetromino.shape, (current_tetromino.x, current_tetromino.y)):
                        current_tetromino.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_tetromino.x += 1
                    if check_collision(board, current_tetromino.shape, (current_tetromino.x, current_tetromino.y)):
                        current_tetromino.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_tetromino.y += 1
                    if check_collision(board, current_tetromino.shape, (current_tetromino.x, current_tetromino.y)):
                        current_tetromino.y -= 1
                elif event.key == pygame.K_UP:
                    current_tetromino.rotate()
                    if check_collision(board, current_tetromino.shape, (current_tetromino.x, current_tetromino.y)):
                        for _ in range(3):  # Rotate back to the original orientation
                            current_tetromino.rotate()

        if pygame.time.get_ticks() - last_drop_time > DROP_INTERVAL:
            last_drop_time = pygame.time.get_ticks()
            current_tetromino.y += 1
            if check_collision(board, current_tetromino.shape, (current_tetromino.x, current_tetromino.y)):
                current_tetromino.y -= 1
                for y, row in enumerate(current_tetromino.shape):
                    for x, cell in enumerate(row):
                        if cell:
                            board[current_tetromino.y + y][current_tetromino.x + x] = COLORS.index(current_tetromino.color) + 1
                lines_cleared = 0
                for y in range(GRID_HEIGHT):
                    if 0 not in board[y]:
                        board = remove_line(board, y)
                        lines_cleared += 1
                score += lines_cleared ** 2
                current_tetromino = next_tetromino
                next_tetromino = Tetromino()
                if check_collision(board, current_tetromino.shape, (current_tetromino.x, current_tetromino.y)):
                    game_over = True

        screen.fill(BLACK)
        draw_board()
        pygame.display.flip()
        clock.tick(FPS)

    print(f"Game Over! Your score: {score}")
    pygame.quit()

if __name__ == "__main__":
    main()
