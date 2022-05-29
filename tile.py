import pygame

class Tile():
    def __init__(self, row, col, color, size) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.size = size
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.size*self.col, self.size*self.row, self.size, self.size))