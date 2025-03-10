import GAME
import MAIN_MENU

from Config import pygame
Game = GAME.game()
Main_Menu = MAIN_MENU.Main_Menu()

game_event_files = [Game, Main_Menu]

class window():
    def __init__(self):
        pygame.init()
        global screen 
        screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)#creates pygame window, scales to fullscreen
        global clock
        clock = pygame.time.Clock()#clock object to handle time
def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit(); sys.exit()
        for active_file in game_event_files:
            if active_file.active = True:
                active_file.run()
        clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    Main_Menu.active = True
    run()
