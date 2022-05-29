import os
import sys

import pygame

from constants import *
from grid import Grid
from menu import Menu

# GLOBAL VARIABLES
global size, color, replay, score
size, color = 14, 5     # starting size and colors
replay = False
score = 0

def main(size, num_colors):
    """
    SETUP section - preparing everything before the main loop runs
    """
    pygame.init()
    grid = Grid(size, num_colors)
    menu = Menu(SCREEN_WIDTH-PLAY_WIDTH, size, num_colors)

    # Creating the screen and the clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.set_alpha(0)  # Make alpha bits transparent
    clock = pygame.time.Clock()

    super_loop(screen, clock, grid, menu)

def super_loop(screen, clock, grid, menu):
    win = False
    lose = False

    while True:
        """
        EVENTS section - how the code reacts when users do things
        """
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        event_list = pygame.event.get()
        
        for event in event_list:
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                global replay
                replay = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_pos[0] < PLAY_WIDTH:
                    if grid.clicked(mouse_pos):
                        # what to do when a tile is clicked
                        global score
                        score += 1
                        menu.score = score
                        full = grid.check_full()
        
        selected_size = menu.size_menu.update(event_list)
        if selected_size >= 0:
            menu.size_menu.main = menu.size_menu.options[selected_size]
        selected_color = menu.color_menu.update(event_list)
        if selected_color >= 0:
            menu.color_menu.main = menu.color_menu.options[selected_color]
        
        # check if won or lost
        global size, color
        target_score = SCORE[str(size)+'x'+str(size)+','+str(color)]
        if score <= target_score and grid.check_full():
            win = True
        elif score > target_score:
            lose = True

        """
        UPDATE section - manipulate everything on the screen
        """
        # if this is true, play again is clicked
        if menu.play_again.update(mouse_pos, mouse_buttons):
            # put 6 lines in one, don't touch please
            size = int("".join([x for x in menu.size_menu.main[:int(len(menu.size_menu.main)/2)] if x.isdigit()]))
            color = int(menu.color_menu.main)
            replay = True
            break
        
        """
        DRAW section - make everything show up on screen
        """
        screen.fill(BLACK)  # Fill the screen with black colour

        grid.draw(screen)
        menu.draw(screen, size, color, win, lose)

        pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
        clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

if __name__ == "__main__":
    main(size, color)

while replay:
    score = 0
    main(size, color)
