import pygame

from constants import *

class Button():
    def __init__(self, color, center, font, text='', border_width=None):
        self.color = color
        self.font = font
        self.center = center
        self.text = self.font.render(text, True, (0,0,0))
        if border_width == None:
            self.border_width = self.text.get_width() * 1.2
        else:
            self.border_width = border_width
        self.height = self.text.get_height() * 1.1
        self.x = self.center[0] - (self.border_width/2)
        self.y = self.center[1] - (self.height/2)

        self.active = False

    def draw(self, screen, outline=None, outlineWidth=0):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-outlineWidth,self.y-outlineWidth,self.border_width+(2*outlineWidth),self.height+(2*outlineWidth)),0)

        pygame.draw.rect(screen, self.color, (self.x,self.y,self.border_width,self.height), 0)
        
        if self.text != '':
            screen.blit(self.text, (self.x + (self.border_width/2 - self.text.get_width()/2), self.y + (self.height/2 - self.text.get_height()/2)))

    def hover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.border_width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def clicked(self, pos, mouse_buttons):
        if self.hover(pos) and mouse_buttons[0]:
            return True
        return False
    
    def update(self, pos, mouse_buttons):
        if self.hover(pos):
            self.color = LIGHT_GREY
        else:
            self.color = WHITE
        if self.clicked(pos, mouse_buttons):
            return True
        return False
