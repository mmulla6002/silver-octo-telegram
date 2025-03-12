from Config import *
class 2P_Menu():
    def __init__(self):
        self.active = False

    def run():
        MAIN.screen.fill((0,128,256))
        if Play_button.draw(MAIN.screen):
            self.active = False
            MAIN.2_Player_Game.active = True
        elif Back_button.draw(MAIN.screen):
            self.active = False
            MAIN.Main_Menu.active = True


Play_button = button.Button(x,y,width,height)
Back_button = button.Button(x,y,width,height)
