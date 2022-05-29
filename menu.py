import pygame

from constants import *
from button import Button
from dropdown import DropDown

class Menu():
    """
    To display the menu on the right side of the screen
    Currently incudes: Play button and dropdowns for size and colors
    """
    def __init__(self, width, current_size, current_color):
        self.width = width
        self.x = PLAY_WIDTH
        self.score = 0
        
        # menu items - specific for this game
        self.font_medium = pygame.font.Font(None, int(SCREEN_HEIGHT/12))
        self.font_small = pygame.font.Font(None, int(SCREEN_HEIGHT/14))
        self.title = self.font_medium.render("Flood It!", True, WHITE)
        self.name = self.font_medium.render("Divy Patel", True, WHITE)
        self.win_text = self.font_medium.render("You Win", True, WHITE)
        self.lose_text = self.font_medium.render("You Lose", True, WHITE)
        color_list = [WHITE for x in range(8)]
        self.size_menu = DropDown(color_list, [WHITE, GREY], 
                                  PLAY_WIDTH+self.width*1/6, SCREEN_HEIGHT*2/7,
                                  (SCREEN_WIDTH-PLAY_WIDTH)*2/3, SCREEN_HEIGHT/15,
                                  self.font_small, str(current_size)+"x"+str(current_size),
                                  ["2x2","6x6","10x10","14x14","18x18","22x22","26x26"])
        self.color_menu = DropDown(color_list, [WHITE, GREY],
                                   PLAY_WIDTH+self.width*1/6, SCREEN_HEIGHT*3/7,
                                   (SCREEN_WIDTH-PLAY_WIDTH)*2/3, SCREEN_HEIGHT/15,
                                   self.font_small, str(current_color),
                                   ["3","4","5","6","7","8"])
        self.play_again = Button(WHITE, (PLAY_WIDTH+self.width*0.5,SCREEN_HEIGHT*1/5),
                                 self.font_small, "Play Again")

    def draw(self, screen, size, color, win=False, lose=False):
        """
        To draw each item from the menu onto the screen
        Call this method for each frame
        """
        # Divy Patel text
        screen.blit(self.name, (self.x + self.width/2 - self.name.get_width()/2, SCREEN_HEIGHT*7/8))
        
        # floodIt text
        screen.blit(self.title, (self.x + self.width/2 - self.title.get_width()/2, SCREEN_HEIGHT*1/15))
        
        # score text
        target_score = SCORE[str(size)+'x'+str(size)+','+str(color)]
        self.score_text = self.font_medium.render(str(self.score)+"/"+str(target_score), True, WHITE)
        screen.blit(self.score_text, (self.x + self.width/2 - self.score_text.get_width()/2, SCREEN_HEIGHT*3/5))
        
        # win/lose text
        if win:
            screen.blit(self.win_text, (self.x + self.width/2 - self.win_text.get_width()/2, SCREEN_HEIGHT*7/10))
        elif lose:
            screen.blit(self.lose_text, (self.x + self.width/2 - self.lose_text.get_width()/2, SCREEN_HEIGHT*7/10))
        
        # play again button
        self.play_again.draw(screen, BLACK, 3)
        
        # color dropdown - 2,3,4,5,6,7,8
        self.color_menu.draw(screen)
        
        # size dropdown - 2,6,10,14,18,22,26
        self.size_menu.draw(screen)
