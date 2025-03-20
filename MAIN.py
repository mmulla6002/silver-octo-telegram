import pygame
import MAIN_MENU
pygame.init()
screen = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)#creates pygame window, scales to fullscreen
clock = pygame.time.Clock()#clock object to handle time
if __name__ == "__main__":
    Main_Menu = MAIN_MENU.Main_Menu()
    Main_Menu.run(screen, clock)
