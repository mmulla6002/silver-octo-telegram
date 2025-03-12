from Config import *
class Main_Menu():
    def __init__(self):
        self.active = False

    def run():
        MAIN.screen.fill((0,128,256))
        if 1P_button.draw(MAIN.screen):
            self.active = False
            MAIN.1P_Menu.active = True
        elif 2P_button.draw(MAIN.screen):
            self.active = False
            MAIN.2P_Menu.active = True
        elif Endless_button.draw(MAIN.screen):
            self.active = False
            MAIN.Endless_Menu.active = True
        elif Quit_button.draw(MAIN.screen):
            pygame.quit(); sys.exit()


1P_buton = button.Button(x,y,width,height)
2P_button = button.Button(x,y,width,height)
Endless_button = button.Button(x,y,width,height)
Quit_button = button.Button(x,y,width,height)
      
