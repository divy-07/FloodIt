import pygame
import random

from constants import *
from tile import Tile

class Grid():
    """
    Handels the grid, contains all the tiles
    """
    def __init__(self, size, num_colors):
        self.size = size
        self.num_colors = num_colors
        self.grid = self.generate_grid()
        self.color = self.grid[0][0].color
    
    def generate_grid(self) -> list:
        """
        Generates a 2D array of size = self.size
        Each entry is a Tile with color chosen by self.choose_color()
        Returns the grid as a 2D array
        """
        grid = []
        for i in range(self.size):
            grid.append([])
            for j in range(self.size):
                grid[i].append([])
        
        for i in range(self.size):
            for j in range(self.size):
                color = self.choose_color()
                grid[i][j] = Tile(i, j, color, PLAY_WIDTH/self.size)
        return grid
    
    def choose_color(self) -> int:
        """
        Returns a random color
        The range of colors is based on self.num_colors
        """
        color = random.randint(1,self.num_colors)
        match color:
            case 1: color = RED
            case 2: color = GREEN
            case 3: color = YELLOW
            case 4: color = PALE
            case 5: color = PURPLE
            case 6: color = CYAN
            case 7: color = BLUE
            case 8: color = PINK
        return color
    
    def draw(self, screen) -> None:
        for row in range(len(self.grid)):
            for tile in self.grid[row]:
                tile.draw(screen)
            
        # draw lines
        row_spacing = SCREEN_HEIGHT/self.size
        col_spacing = PLAY_WIDTH/self.size
        for i in range(1, self.size+1):
            pygame.draw.line(screen, LIGHT_GREY, (0, i*row_spacing), (PLAY_WIDTH, i*row_spacing), 3)
            pygame.draw.line(screen, LIGHT_GREY, (i*col_spacing, 0), (i*col_spacing, SCREEN_HEIGHT), 3)
    
    def clicked(self, mouse_pos) -> bool:
        """
        Call this method when the grid is clicked
        Updates the grid with new colors depending on the clicked tile
        Returns whether the grid updated the colors (True if new color)
        """
        col = int(self.size * (mouse_pos[0] / PLAY_WIDTH))
        row = int(self.size * (mouse_pos[1] / SCREEN_HEIGHT))
        old_color = self.color
        self.color = self.grid[row][col].color
        if self.color != old_color:
            self.grid[0][0].color = self.color
            checked_cells = []
            self.flood(old_color, 0, 0, checked_cells)
        return self.color != old_color
        
    def flood(self, old_color, row, col, checked_cells: list) -> None:
        """
        Flood the grid with clicked color
        Uses recursion
        """
        if [row, col] not in checked_cells:
            checked_cells.append([row, col])
            # right
            if col < self.size - 1:
                if self.grid[row][col+1].color == old_color:
                    self.grid[row][col+1].color = self.color
                    self.flood(old_color, row, col+1, checked_cells)
            # bottom
            if row < self.size - 1:
                if self.grid[row+1][col].color == old_color:
                    self.grid[row+1][col].color = self.color
                    self.flood(old_color, row+1, col, checked_cells)
            # left
            if col > 0:
                if self.grid[row][col-1].color == old_color:
                    self.grid[row][col-1].color = self.color
                    self.flood(old_color, row, col-1, checked_cells)
            # top
            if row > 0:
                if self.grid[row-1][col].color == old_color:
                    self.grid[row-1][col].color = self.color
                    self.flood(old_color, row-1, col, checked_cells)
    
    def check_full(self) -> bool:
        """
        Checks if the user has completed th egame
        i.e. if the grid is all the same color
        returns True if all same color
        """
        for row in range(len(self.grid)):
            for tile in self.grid[row]:
                if tile.color != self.color:
                    return False
        return True
