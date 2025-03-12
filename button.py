import pygame
class Button():
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.topleft = (x,y)
        self.clicked = False
        self.hover = False
    def draw(self,screen):
        button_clicked = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                button_clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        pygame.draw.rect(screen,(colour),self)
        return button_clicked
