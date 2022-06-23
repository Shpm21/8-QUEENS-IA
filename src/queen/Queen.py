import pygame


class Queen:
    def __init__(self, pos: list) -> None:
        self.path = "resources/img/queen.png"
        self.image = pygame.image.load(self.path)
        self.new_image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.new_image.get_rect()
        self.pos = pos
        self.update_pos(self.pos[0], self.pos[1])
        
    def set_pos(self, pos: list) -> None:
        self.pos = pos
        self.update_pos(self.pos[0], self.pos[1])
        
    def update_row(self, row: int) -> None:
        self.rect.y = 80 * row
                
    def update_column(self, column: int) -> None:
        self.rect.x = 80 * column
        
    def update_pos(self, row: int, column: int) -> None:
        self.update_row(row)
        self.update_column(column)