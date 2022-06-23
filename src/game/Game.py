import time

import pygame
from algorithm.Algorithm import Algorithm
from queen.Queen import Queen
from utility.constants import CELL, N_OF_CELL, SIZE
from utility.functions import get_init

# def get_solutions() -> list:
#     return [
#         (6, 4, 2, 0, 5, 7, 1, 3),
#         (7, 1, 4, 2, 0, 6, 3, 5),
#         (7, 1, 3, 0, 6, 4, 2, 5),
#         (4, 7, 3, 0, 6, 1, 5, 2),
#         (3, 7, 0, 4, 6, 1, 5, 2),
#         (5, 7, 1, 3, 0, 6, 4, 2)
#     ]

class Game:
    def __init__(self) -> None:
        self.init = get_init()
        self.algorithm = Algorithm()
        self.window = pygame.display.set_mode((SIZE, SIZE))
        pygame.display.set_caption("8 queens")
        self.fps = pygame.time.Clock()
        self.queens = self.create_queens()
        
    def draw_cell(self):
        count = 0
        for i in range(N_OF_CELL):
            for j in range(N_OF_CELL):
                if count % 2 == 0:
                    self.draw(pygame.Rect(i, j, CELL, CELL), pygame.Color(230, 237, 229), border=True)
                else:
                    self.draw(pygame.Rect(i, j, CELL, CELL), pygame.Color(21, 136, 0), border=True)
                count += 1
            count += 1
        
    def draw(self, element, color, border=False):
        x = int(element.x * CELL)
        y = int(element.y * CELL)
        body_rect = pygame.Rect(x, y, CELL, CELL)
        pygame.draw.rect(self.window, color, body_rect)
        if border:
            pygame.draw.rect(self.window, (CELL, CELL, CELL+1), body_rect, 3)
    
    def draw_queens(self) -> None:
        for q in self.queens:
            self.window.blit(q.new_image, q.rect)
        
    def create_queens(self):
        queens = []
        for i in range(N_OF_CELL):
            queens.append(Queen([0, i]))
        return queens
    
    def update_queens(self, mov: tuple) -> None:
        for i in range(len(self.queens)):
            self.queens[i].update_pos(mov[i], i)
    
    def __run__(self):
        while True:
            solution = self.algorithm.evaluate_path(self.init)
            self.window.fill(pygame.Color(255, 255, 255))
            self.draw_cell()
            self.draw_queens()
            self.update_queens(solution.board)
            time.sleep(0.5)
            self.init = solution.board
            pygame.display.flip()
            self.fps.tick(24)
